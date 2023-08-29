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

##############################################################################
# THIS FILE WAS CREATED AUTOMATICALLY, DO NOT CHANGE IT UNLESS YOU KNOW WHAT #
#                                 YOU ARE DOING                              #
##############################################################################

from gimelstudio import api

class DockerNode(api.Node):
    def __init__(self, nodegraph, _id):
        api.Node.__init__(self, nodegraph, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "<Image: 'itzg/minecraft-server:latest'>",
            "author": "Gameplex Software",
            "version": (0, 0, 1),
            "category": "FILTER",
            "description": "Show <Image: 'itzg/minecraft-server:latest'> image on the node graph",
        }
        return meta_info

    def NodeInitProps(self):
        image_id = api.LabelProp(
            idname="image_id",
            default="6796d7fe811db65622e9fb4d08349258d4879022f98e6701decae0f1a6f51a78",
            fpb_label="Image ID"
        )
        self.NodeAddProp(image_id)

        image_status = api.LabelProp(
            idname="image_status",
            default="On host disk",
            fpb_label="Status"
        )
        self.NodeAddProp(image_status)

    def NodeInitParams(self):
        pass

    def MutedNodeEvaluation(self, eval_info):
        return self.EvalMutedNode(eval_info)

    def NodeEvaluation(self, eval_info):
        render_image = api.RenderImage()
        return render_image

api.RegisterNode(DockerNode, "6796d7fe811db65622e9fb4d08349258d4879022f98e6701decae0f1a6f51a78")