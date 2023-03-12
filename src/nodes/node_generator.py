# ----------------------------------------------------------------------------
# SkiffUI Copyright 2020-2023 by Gameplex Software and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

import os
import json
import docker
from hashlib import md5
from jinja2 import Template
from gimelstudio import api
from gimelstudio import core


def main():
    # Get the path of the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the path of the template file
    template_path = os.path.join(script_dir, "docker_node_template.py")

    # Read the template file
    with open(template_path) as f:
        template_content = f.read()

    # Create a Jinja2 template object from the template content
    template = Template(template_content)

    # Initialize the Docker client
    client = docker.from_env()

    # Iterate through each container
    for container in client.containers.list():

        # Generate the content for the Docker node file
        node_content = template.render(
            container_id=container.id[:12],
            container_name=container.name,
            container_status=container.status,
            container_image=container.image.tags[0] if container.image.tags else "Unknown"
        )

        # Generate an MD5 hash of the content
        content_hash = md5(node_content.encode("utf-8")).hexdigest()

        # Construct the filename for the Docker node file
        filename = f"{container.id[:12]}.py"
        node_file_path = os.path.join(script_dir, filename)

        # Check if the file already exists and has the same content
        if os.path.exists(node_file_path):
            with open(node_file_path) as f:
                existing_content = f.read()
            existing_hash = md5(existing_content.encode("utf-8")).hexdigest()
            if existing_hash == content_hash:
                print(f"{filename} already exists and has not been modified.")
                continue
            else:
                core.registry.UnregisterNode(container.id)
                core.RegisterNode(node=container.id, idname=container.id)

        # Write the content to the Docker node file
        with open(node_file_path, "w") as f:
            f.write(node_content)

        # Print a message indicating that the file has been created
        print(f"Created {filename}.")