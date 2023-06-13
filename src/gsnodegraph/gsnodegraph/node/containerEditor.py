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

import wx, subprocess
from shiphelm import helm

helm = helm.helm()

class ContainerEditor(wx.Dialog):
    def __init__(self, id):
        super().__init__(None, title="Container Editor", size=(600, 700))
        ContainerEditor.id = id  # store the ID of the container to be edited

        # Get volume data (for now this is a placeholder)
        self.data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Gender': ['Female', 'Male', 'Male']}

        self.SetBackgroundColour('#1E1E1E')  # set the background color to dark

        # create a notebook and tabs
        self.notebook = wx.Notebook(self)
        self.general_tab = wx.Panel(self.notebook)
        self.volumes_tab = wx.Panel(self.notebook)
        self.ports_tab = wx.Panel(self.notebook)
        self.environment_tab = wx.Panel(self.notebook)
        self.command_tab = wx.Panel(self.notebook)

        self.notebook.AddPage(self.general_tab, "General")
        self.notebook.AddPage(self.volumes_tab, "Volumes")
        self.notebook.AddPage(self.ports_tab, "Ports")
        self.notebook.AddPage(self.environment_tab, "Environment")
        self.notebook.AddPage(self.command_tab, "Command")

    # General tab
        # Add a static box with some widgets

        # Container Name
        self.container_name_label = wx.StaticText(self.general_tab, label="Container Name:")
        self.container_name_label.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.container_name_label.SetForegroundColour(wx.WHITE)
        ContainerEditor.container_name_text = wx.TextCtrl(self.general_tab, value=str(helm.get_container_by_id(ContainerEditor.id).name))

        # Container Image
        self.container_image_label = wx.StaticText(self.general_tab, label="Container Image:")
        self.container_image_label.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.container_image_label.SetForegroundColour(wx.WHITE)
        choices = ['Gameplex-Software/Nginx', 'Gameplex-Software/BusyBox', 'Gameplex-Software/Apache', 'Gameplex-Software/NginxPlus']
        ContainerEditor.container_image_text = wx.ComboBox(self.general_tab, choices=choices)

        # create a sizer for the General tab
        static_box = wx.StaticBox(self.general_tab, label="Container Details")
        general_sizer = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        # Container name sizers
        static_box_sizer.Add(self.container_name_label, 0, wx.ALL | wx.LEFT, 5)
        static_box_sizer.Add(ContainerEditor.container_name_text, 0, wx.ALL | wx.EXPAND, 5)

        # Container image sizers
        static_box_sizer.Add(self.container_image_label, 0, wx.ALL | wx.LEFT, 5)
        static_box_sizer.Add(self.container_image_text, 0, wx.ALL | wx.EXPAND, 5)

        general_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.general_tab.SetSizer(general_sizer)

    # Volumes tab

        # create a sizer for the Volumes tab
        volume_sizer = wx.BoxSizer(wx.VERTICAL)

        # Add a static box with some widgets
        static_box = wx.StaticBox(self.volumes_tab, label="Container Volumes:")
        static_box.SetForegroundColour(wx.WHITE)  # Set label color to white
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        volume_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.volumes_tab.SetSizer(volume_sizer)

    # ports tab

        # create a sizer for the Ports tab
        port_sizer = wx.BoxSizer(wx.VERTICAL)

        # Add a static box with some widgets
        static_box = wx.StaticBox(self.ports_tab, label="Container Ports")
        static_box.SetForegroundColour(wx.WHITE)  # Set label color to white
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        port_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.ports_tab.SetSizer(port_sizer)

    # Environment tab

        # create a sizer for the Environment tab
        environment_sizer = wx.BoxSizer(wx.VERTICAL)

        # Add a static box with some widgets
        static_box = wx.StaticBox(self.environment_tab, label="Container Environment Variables")
        static_box.SetForegroundColour(wx.WHITE)  # Set label color to white
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        environment_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.environment_tab.SetSizer(environment_sizer)

    # Command tab

        # create a sizer for the Command tab
        command_sizer = wx.BoxSizer(wx.VERTICAL)

        # Add a static box with some widgets
        static_box = wx.StaticBox(self.command_tab, label="Container docker Run Command")
        static_box.SetForegroundColour(wx.WHITE)  # Set label color to white
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        command_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.command_tab.SetSizer(command_sizer)

        self.container_command_label = wx.StaticText(self.command_tab, label="Container Command:")
        static_box.SetForegroundColour(wx.WHITE)  # Set label color to white
        self.container_command_label.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.container_command_label.SetForegroundColour(wx.WHITE)
        helm.set_engine_manual('docker')
        ContainerEditor.container_command_text = wx.TextCtrl(self.command_tab, value=str(helm.get_run_command(container_id=ContainerEditor.id)))

        # create a sizer for the General tab
        static_box = wx.StaticBox(self.command_tab, label="Container Details")
        static_box.SetForegroundColour(wx.WHITE)  # Set label color to white
        command_sizer = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        # Container name sizers
        static_box_sizer.Add(self.container_command_label, 0, wx.ALL | wx.LEFT, 5)
        static_box_sizer.Add(ContainerEditor.container_command_text, 0, wx.ALL | wx.EXPAND, 5)

        command_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.command_tab.SetSizer(command_sizer)

    # End of tabs
        #Dialog footer
        # create the buttons
        self.cancel_button = wx.Button(self, label="Cancel")
        self.save_button = wx.Button(self, label="Save")
        self.apply_button = wx.Button(self, label="Apply")

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.cancel_button, 0, wx.ALL, 5)
        button_sizer.Add(self.save_button, 0, wx.ALL, 5)
        button_sizer.Add(self.apply_button, 0, wx.ALL, 5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.EXPAND)
        sizer.Add(button_sizer, 0, wx.CENTRE)

        self.SetSizer(sizer)
        self.Layout()

        # bind events to buttons
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save)
        self.apply_button.Bind(wx.EVT_BUTTON, self.on_apply)

    def on_apply(self, event):
        # retrieve values from UI elements
        container_name = self.container_name_text.GetValue()
        container_image = self.container_image_text.GetValue()

        # apply changes to container with matching id
        helm.rename_container(str(ContainerEditor.id), str(container_name))  # implement this function to get the container by ID
        print("Applied changes to container", self.id)

    def on_save(self, event):
        # Do the same thing as apply
        self.on_apply()
        print("Saved", ContainerEditor.id)
        # close the dialog
        self.EndModal(wx.ID_CANCEL)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)
