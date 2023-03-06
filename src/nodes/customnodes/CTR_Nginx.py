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

import numpy as np
from gimelstudio import api


class NginxNode(api.Node):
    def __init__(self, nodegraph, _id):
        api.Node.__init__(self, nodegraph, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Nginx",
            "author": "Gameplex Software",
            "version": (0, 5, 0),
            "category": "TRANSFORM",
            "description": "Controls an Nginx container",
        }
        return meta_info

    def NodeInitProps(self):
        flip_direction = api.ChoiceProp(
            idname="direction",
            default="Vertically",
            choices=["Vertically", "Horizontally"],
            fpb_label="Flip Direction"
        )
        self.NodeAddProp(flip_direction)
        imageid = api.ChoiceProp(
            idname="dockerImage",
            default="test/testimage",
            choices=["text/testimage", "test/testimage2"],
            fpb_label="Docker Image"
        )
        self.NodeAddProp(imageid)

    def NodeInitParams(self):
        port0 = api.RenderImageParam("port0", "Port 1092")
        port1 = api.RenderImageParam("port1", "Port 1093")
        port2 = api.RenderImageParam("port2", "Port 1094")
        port3 = api.RenderImageParam("port3", "Port 1095")

        self.NodeAddParam(port0)
        self.NodeAddParam(port1)
        self.NodeAddParam(port2)
        self.NodeAddParam(port3)

    def MutedNodeEvaluation(self, eval_info):
        return self.EvalMutedNode(eval_info)

    def NodeEvaluation(self, eval_info):
        flip_direction = self.EvalProperty(eval_info, "direction")
        image1 = self.EvalParameter(eval_info, "port")

        image = api.RenderImage()
        img = image1.Image("numpy")

        if flip_direction == "Vertically":
            output_img = np.flipud(img)
        elif flip_direction == "Horizontally":
            output_img = np.fliplr(img)

        image.SetAsImage(output_img)
        return image


api.RegisterNode(NginxNode, "Nginx_Node")
