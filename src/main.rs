use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use docker::{CreateContainerOptions, Docker, ListContainersOptions};
use egui::{Align2, CentralPanel, CtxRef, Grid, Key, Label, Pos2, Ui, Window};
use std::sync::{Arc, Mutex};
use tokio::task;

struct AppState {
    docker: Docker,
    containers: Arc<Mutex<Vec<Container>>>,
}

struct Container {
    id: String,
    name: String,
    image: String,
    status: String,
}

struct CreateContainerParams {
    image: String,
}

impl AppState {
    fn new() -> Self {
        let docker = Docker::connect_with_local_defaults().unwrap();
        let containers = Arc::new(Mutex::new(vec![]));

        let cloned_containers = containers.clone();
        task::spawn(async move {
            loop {
                let docker = Docker::connect_with_local_defaults().unwrap();
                let containers = docker.containers().list(&ListContainersOptions::default()).unwrap();

                let new_containers = containers
                    .into_iter()
                    .map(|container| Container {
                        id: container.id,
                        name: container.names.join(", "),
                        image: container.image,
                        status: container.status,
                    })
                    .collect();

                let mut container_lock = cloned_containers.lock().unwrap();
                *container_lock = new_containers;

                tokio::time::sleep(std::time::Duration::from_secs(5)).await;
            }
        });

        Self {
            docker,
            containers,
        }
    }
}

#[get("/")]
async fn index(ctx: web::Data<CtxRef>) -> impl Responder {
    let mut ctx = ctx.write();

    Window::new("Docker Management")
        .collapsible(false)
        .show(&mut *ctx, |ui| {
            ui.vertical(|ui| {
                ui.label("Welcome to the Docker Management System!");
                ui.add(
                    Label::new("Press the button below to list all containers:")
                        .text_style(egui::TextStyle::Heading),
                );
                if ui.button("List Containers").clicked() {
                    ui.output().clicked_widgets.clear();
                    ui.memory().options.undo_limit = 0;
                    ui.memory().options.undo_stack_size = 0;

                    let containers = task::spawn_blocking(move || {
                        let docker = Docker::connect_with_local_defaults().unwrap();
                        let containers = docker.containers().list(&ListContainersOptions::default()).unwrap();

                        containers
                            .into_iter()
                            .map(|container| Container {
                                id: container.id,
                                name: container.names.join(", "),
                                image: container.image,
                                status: container.status,
                            })
                            .collect()
                    })
                    .await
                    .unwrap();

                    let mut container_lock = ctx.app().containers.lock().unwrap();
                    *container_lock = containers;
                }
            });
        });

    HttpResponse::Ok().body("")
}

#[get("/containers")]
async fn list_containers(ctx: web::Data<CtxRef>) -> impl Responder {
    let mut ctx = ctx.write();

    Window::new("List Containers")
        .collapsible(false)
        .scroll(false)
        .show(&mut *ctx, |ui| {
            let container_lock = ctx.app().containers.lock().unwrap();
            let containers = container_lock.iter().map(|c| (c.name.clone(), c)).collect::<Vec<_>>();
            Grid::new("list_containers_grid")
                .striped(true)
                .show(ui, |ui| {
                    for (name, container) in containers {
                        ui.label(name);
                        ui.label(container.id.clone());
                        ui.label(container.image.clone());
                        ui.label(container.status.clone());
                        ui.end_row();
                    }
                });
        });

    HttpResponse::Ok().body("")
}

#[post("/containers")]
async fn create_container(params: web::Json<CreateContainerParams>, ctx: web::Data<CtxRef>) -> impl Responder {
    let docker = ctx.app().docker.clone();
    let params = params.into_inner();

    task::spawn_blocking(move || {
        let mut create_opts = CreateContainerOptions::builder(params.image);
        create_opts = create_opts.name("example_container");

        docker
            .create_container(create_opts.build())
            .unwrap()
            .start()
            .unwrap();
    })
    .await
    .unwrap();

    HttpResponse::Ok().body("")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let app_state = AppState::new();
    let ctx = CtxRef::default();

    HttpServer::new(move || {
        App::new()
            .data(ctx.clone())
            .data(app_state.clone())
            .service(index)
            .service(list_containers)
            .service(create_container)
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}

