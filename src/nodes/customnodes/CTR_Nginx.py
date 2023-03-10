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

from tkinter import SEL
import numpy as np
from gimelstudio import api
import docker
from joblib import Parallel, delayed

def slice_from_string(slice_string):
    slices = slice_string.split(',')
    if len(slices) > 1:
        return [slice_from_string(s.strip()) for s in slices]
        return slice(*[int(x) for x in slice_string.split(':')])

def __init__(self, nodegraph, _id):
    api.Node.__init__(self, nodegraph, _id)

class NginxNode(api.Node):
    @property
    
    def NodeMeta(self):
        meta_info = {
            "label": "Select a docker image",
            "author": "Gameplex Software",
            "version": (0, 5, 0),
            "category": "TRANSFORM",
            "description": "Controls docker containers",
        }
        return meta_info
    
    def NodeInitProps(self):        
        client = docker.from_env()
        query="nginx"
        #results = client.images.search(query, limit=2)
        #image_list = []
        #for result in results:
        #    image_list.append(result["name"])

        imageid = api.ChoiceProp(
            idname="dockerImage",
            default="nginx",
        #    choices=image_list,
            choices=[
                "Normal", "Darken", "Multiply", "Color Burn", 
                "Lighten", "Screen", "Color Dodge", "Add",
                "Overlay", "Soft Light", "Difference", "Subtract",
                "Divide", "Reflect", "Glow", "Average", "Exclusion"
                ],
            fpb_label="Docker Image"
        )
        self.NodeAddProp(imageid)
        port = api.PositiveIntegerProp(
            idname="port",
            default=8080,
            min_val=1000,
            max_val=10000,
            show_p=False,
            fpb_label="Container Port 1"
        )
        self.NodeAddProp(port)
        port2 = api.PositiveIntegerProp(
            idname="port2",
            default=8080,
            min_val=1000,
            max_val=10000,
            show_p=False,
            fpb_label="Container Port 2"
        )
        self.NodeAddProp(port2)        
        port3 = api.PositiveIntegerProp(
            idname="port3",
            default=8080,
            min_val=1000,
            max_val=10000,
            show_p=False,
            fpb_label="Container Port 3"
        )
        self.NodeAddProp(port3)        
        port4 = api.PositiveIntegerProp(
            idname="port4",
            default=8080,
            min_val=1000,
            max_val=10000,
            show_p=False,
            fpb_label="Container Port 4"
        )
        self.NodeAddProp(port4)              

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
        print("Nginx Eval called")

api.RegisterNode(NginxNode, "Nginx_Node")
