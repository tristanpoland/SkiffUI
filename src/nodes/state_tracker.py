import json
import docker
import time
import threading
import uuid

def generate_node_id():
    return str(uuid.uuid4())

def get_node_data():
    print("Started generating Docker state")
    client = docker.from_env()
    containers = client.containers.list()
    nodes = {}
    for container in containers:
        node_id = generate_node_id()
        node = {
            "idname": "DockerNode",
            "pos": [
                0,
                0
            ],
            "muted": False,
            "selected": False,
            "active": False,
            "expanded": False,
            "parameters": {},
            "properties": {
                "name": {
                    "idname": "name",
                    "value": container.name
                },
                "status": {
                    "idname": "status",
                    "value": container.status
                }
            }
        }
        nodes[node_id] = node

    node_graph = {
        "nodes": nodes
    }

    data = {
        "application": "SkiffUI",
        "file_type": "SkiffUI Network Map",
        "app_version": "0.0.1",
        "app_version_tag": " pre-alpha 1",
        "app_version_full": "0.0.1 pre-alpha 1",
        "node_graph": node_graph
    }

    return data

def write_json():
    data = get_node_data()
    formatted_json = json.dumps(data, indent=4)
    with open('docker_state.skf', 'w') as f:
        f.write(formatted_json)
        print("Docker state built")

    # Schedule the function to run again after 2 seconds
    threading.Timer(2.0, write_json).start()

write_json()