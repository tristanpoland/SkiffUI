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

import docker


class Shiphelm:
    client = docker.from_env()

    def get_running_containers(self):
        return self.client.containers.list()

    def get_container_stats(self, container_id):
        container = self.client.containers.get(container_id)
        return container.stats(stream=False)

    def get_container_ports(self, container_id):
        container = self.client.containers.get(container_id)
        return container.ports

    def search_containers(self, term):
        return self.client.containers.list(filters={'name': term})

    def stop_container(self, container_id):
        container = self.client.containers.get(container_id)
        container.stop()

    def start_container(self, container_id):
        container = self.client.containers.get(container_id)
        container.start()

    def update_container_ports(self, container_id, new_port_bindings):
        container = self.client.containers.get(container_id)
        container.stop()
        container.reload()
        container.update(port_bindings=new_port_bindings)
        container.start()
