from gimelstudio import api

class DockerNode(api.Node):
    def __init__(self, nodegraph, _id):
        api.Node.__init__(self, nodegraph, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "ginx-75g3",
            "author": "Gameplex Software",
            "version": (0, 0, 1),
            "category": "FILTER",
            "description": "Show ginx-75g3 container on the node graph",
        }
        return meta_info

    def NodeInitProps(self):
        container_id = api.StringProp(
            idname="container_id",
            default="40c0e31bc4c6",
            show_p=False
        )
        self.NodeAddProp(container_id)

        container_name = api.StringProp(
            idname="container_name",
            default="ginx-75g3",
            show_p=False
        )
        self.NodeAddProp(container_name)

        container_status = api.StringProp(
            idname="container_status",
            default="running",
            show_p=True,
            fpb_label="Status"
        )
        self.NodeAddProp(container_status)

        container_image = api.StringProp(
            idname="container_image",
            default="nginx:latest",
            show_p=True,
            fpb_label="Image"
        )
        self.NodeAddProp(container_image)

    def NodeInitParams(self):
        pass

    def MutedNodeEvaluation(self, eval_info):
        return self.EvalMutedNode(eval_info)

    def NodeEvaluation(self, eval_info):
        render_image = api.RenderImage()
        return render_image

api.RegisterNode(DockerNode, "40c0e31bc4c6")