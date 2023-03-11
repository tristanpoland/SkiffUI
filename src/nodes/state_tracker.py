import threading
import time
import json
import docker

def build_docker_state():
    print('[Debbug] Got docker state')
    client = docker.from_env()
    nodes = []
    for container in client.containers.list():
        node = {"name": container.name, "id": container.id}
        nodes.append(node)
    json_data = {"nodes": nodes}
    with open("gimelstudio.skf", "w") as f:
        json.dump(json_data, f)
        print('[Debug] Built Docker state map')

    # Rescan Docker every 2 seconds
    threading.Timer(2.0, build_docker_state).start()

if __name__ == "__main__":
    # Run on a separate thread
    t = threading.Thread(target=build_docker_state)
    t.start()
