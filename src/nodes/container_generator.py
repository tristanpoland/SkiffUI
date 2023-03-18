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
import docker
from hashlib import md5
from jinja2 import Template
from gimelstudio import api
from gimelstudio import core

try:
    def main(containerid, containerImageID):
        # Get the path of the script directory
        script_dir = os.path.dirname(__file__)

        # Get the path of the template file
        template_path = os.path.join(script_dir, "customnodes", containerImageID + ".py")
        print(template_path)
        # Read the template file
        with open(template_path) as f:
            template_content = f.read()

        # Create a Jinja2 template object from the template content
        template = Template(template_content)

        # Initialize the Docker client
        client = docker.from_env()

        # Iterate through each image

        # Generate the content for the Docker node file
        node_content = template.render(
        image_id=containerid,
        image_status="On host disk",
        image_name=containerid
        )
        # Generate an MD5 hash of the content
        content_hash = md5(node_content.encode("utf-8")).hexdigest()
        # Construct the filename for the Docker node file
        filename = f"{containerid}.py"
        container_file_path = os.path.join(script_dir,'containerinstances', filename)
        print(container_file_path)
        # Construct the ID for the Docker node
        node_id = containerid
        # Check if the file already exists and has the same content
        if os.path.exists(container_file_path):
            with open(container_file_path) as f:
                existing_content = f.read()
            existing_hash = md5(existing_content.encode("utf-8")).hexdigest()
            if existing_hash == content_hash:
                pass
        else:
            # Unregister the existing node
            with open(container_file_path, "w") as f:
                f.write(node_content)
                print(f"Created {filename}.")
except:
    raise Exception("Unable to connect to docker")