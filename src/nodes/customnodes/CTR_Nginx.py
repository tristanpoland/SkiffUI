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

from tkinter import SEL, image_types
import numpy as np
from gimelstudio import api
import docker
import os
import json
from collections import OrderedDict

# Initialize Docker client
client = docker.from_env()

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
        # Set cache directory
        cache_dir = 'image_cache'
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

        # Set cache size
        max_cache_size = 20

        # Define cache class
        class LRUCache:
            def __init__(self, maxsize):
                self.cache = OrderedDict()
                self.maxsize = maxsize

            def __getitem__(self, key):
                # Move item to end of cache to indicate recent use
                value = self.cache.pop(key)
                self.cache[key] = value
                return value

            def __setitem__(self, key, value):
                # Add item to cache, removing oldest item if necessary
                if len(self.cache) >= self.maxsize:
                    self.cache.popitem(last=False)
                self.cache[key] = value

            def __contains__(self, key):
                return key in self.cache

        # Initialize cache
        cache_file = os.path.join(cache_dir, 'cache.json')
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                cache = LRUCache(max_cache_size)
                cache.cache = OrderedDict(json.load(f))
        else:
            with open(cache_file, 'w') as f:
                f.write('{}')
            cache = LRUCache(max_cache_size)
        
        # Define search function
        def search_images(query, max_results=20):
            try:
                result
            except:
                result=[]
            # Check if results are in cache
            if query in cache.cache:
                for section in cache.cache[query]:
                    result.append(section['name'])
                else:
                    # Search Docker Hub
                    results = client.images.search(query, limit=max_results)
                    # Cache results
                    cache[query] = results
                    # Update cache file
                    with open(cache_file, 'w') as f:
                        json.dump(list(cache.cache.items()), f)
            # Output list of image names
            for r in result:
                return result
            return result
        

        searchresult=search_images("nginx")
        print(searchresult)
        imageid = api.ChoiceProp(
            idname="dockerImage",
            default="nginx",
            choices=searchresult,
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
