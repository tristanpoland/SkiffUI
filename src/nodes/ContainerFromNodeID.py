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
from nodes import container_generator
from shiphelm import helmdocker
import docker

hd = docker.from_env()
try:
    def main(containerImageID):
        container = hd.containers.run(image=containerImageID, detach=True)
        containerid = container.id
        container_generator.main(containerid, containerImageID)
except:
    raise Exception("Unable to connect to docker")