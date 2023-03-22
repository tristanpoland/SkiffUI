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

import wx
import docker
import threading
from hashlib import md5
from jinja2 import Template
from gimelstudio import api
from gimelstudio import core
from nodes import container_generator
from shiphelm import helmdocker
from plyer import notification

import wx

def OnRemoteConnect():
    global remote_address, remote_type, remote_security
    # Create wx.App object
    app = wx.App()
    # Create dialog box
    dialog = wx.Dialog(None, title='SkiffUI remote connect setup wizard', size=(400, 150), style=wx.DEFAULT_DIALOG_STYLE)
    # Set dark theme colors
    dialog.SetBackgroundColour(wx.Colour(38, 38, 38))
    dialog.SetForegroundColour(wx.WHITE)
    dialog.Center()
    # Create text entry field
    text = wx.TextCtrl(dialog, style=wx.TE_PROCESS_ENTER)
    text.SetBackgroundColour(wx.Colour(50, 50, 50))
    text.SetForegroundColour(wx.WHITE)
    # Create dropdown boxes
    type_choices = ['Docker', 'Docker Swarm', 'Kubernetes']
    type_dropdown = wx.Choice(dialog, choices=type_choices)
    type_dropdown.SetBackgroundColour(wx.Colour(50, 50, 50))
    type_dropdown.SetForegroundColour(wx.WHITE)
    security_choices = ['TLS', 'None']
    security_dropdown = wx.Choice(dialog, choices=security_choices)
    security_dropdown.SetBackgroundColour(wx.Colour(50, 50, 50))
    security_dropdown.SetForegroundColour(wx.WHITE)
    # Create OK button
    ok_button = wx.Button(dialog, wx.ID_OK)
    ok_button.SetBackgroundColour(wx.Colour(70, 70, 70))
    ok_button.SetForegroundColour(wx.WHITE)
    # Create layout
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    sizer.Add(wx.StaticText(dialog, label='Enter remote address:'), flag=wx.LEFT|wx.TOP, border=30)
    sizer.Add(text, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, border=30)
    sizer.Add(wx.StaticText(dialog, label='Select remote type:'), flag=wx.LEFT|wx.TOP, border=30)
    sizer.Add(type_dropdown, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, border=30)
    sizer.Add(wx.StaticText(dialog, label='Select security:'), flag=wx.LEFT|wx.TOP, border=30)
    sizer.Add(security_dropdown, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, border=30)
    sizer.Add(ok_button, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=30)
    dialog.SetSizer(sizer)
    sizer.Fit(dialog)
    # Show dialog box and wait for user input
    if dialog.ShowModal() == wx.ID_OK:
        # Store values in global variables
        remote_address = text.GetValue()
        remote_type = type_choices[type_dropdown.GetCurrentSelection()]
        remote_security = security_choices[security_dropdown.GetCurrentSelection()]
        print(remote_address, remote_type, remote_security)
    # Destroy dialog box
    dialog.Destroy()
    # Run wxPython event loop
    app.MainLoop()

try:
    hd = docker.from_env()
except:
    OnRemoteConnect()

def main(containerImageID):
    container = hd.containers.run(image=containerImageID, detach=True)
    containerid = container.id
    containername = container.short_id
    notification.notify(title="Skiff: Starting container", message="SkiffUI is starting the container {containername} in the background...", timeout=2)
    container_generator.main(containerid, containerImageID)
    timer = threading.Timer(2.0, main)
    timer.start()
    return timer