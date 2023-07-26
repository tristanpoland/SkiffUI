import wx
import wx.grid
from shiphelm import helm

#function shortcuts
helm = helm.helm()

#Color Shortcuts
space_gray = '#3F4146'
dark_charcoal = '#242528'
accent_color = '#5173b5'

#TODO: Make this automatically select the proper engine
helm.set_engine_manual(engine_select="docker")

#Table controls for posts tab
class PortsTable(wx.grid.Grid):
    def __init__(self, parent):
        super().__init__(parent)
        self.CreateGrid(1, 3)

        self.SetColLabelValue(0, "Internal Port")
        self.SetColLabelValue(1, "External Port")
        self.SetColLabelValue(2, "Remove port")

        self.SetColSize(0, 100)
        self.SetColSize(1, 100)
        self.SetColSize(2, 100)

        self.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_left_click)

        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.on_label_left_click)

        self.SetRowLabelSize(0)
        self.AutoSize()

    def on_left_click(self, event):
        row = event.GetRow()
        col = event.GetCol()
        if col == 2:
            self.DeleteRows(row)

    def on_label_left_click(self, event):
        col = event.GetCol()
        if col == 2:
            for row in range(self.GetNumberRows()):
                self.DeleteRows(row)

#Table controls for Volumes tab
class VolumesTable(wx.grid.Grid):
    def __init__(self, parent):
        super().__init__(parent)
        self.CreateGrid(1, 3)

        self.SetColLabelValue(0, "Host Path")
        self.SetColLabelValue(1, "Virtual Path")
        self.SetColLabelValue(2, "Remove Volume")

        self.SetColSize(0, 100)
        self.SetColSize(1, 100)
        self.SetColSize(2, 100)

        self.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_left_click)

        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.on_label_left_click)

        self.SetRowLabelSize(0)
        self.AutoSize()

    def on_left_click(self, event):
        row = event.GetRow()
        col = event.GetCol()
        if col == 2:
            self.DeleteRows(row)

    def on_label_left_click(self, event):
        col = event.GetCol()
        if col == 2:
            for row in range(self.GetNumberRows()):
                self.DeleteRows(row)

class DarkModeTab(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour(dark_charcoal)

class ContainerEditor(wx.Dialog):
    def __init__(self, id):
        super().__init__(None, title="Container Editor", size=(610, 800))

        # store the ID of the container to be edited
        ContainerEditor.id = id

        # Get volume data (for now this is a placeholder)
        self.data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Gender': ['Female', 'Male', 'Male']}

        # set the background color to dark
        self.SetBackgroundColour(dark_charcoal)

        # create a notebook and tabs
        self.notebook = wx.Notebook(self)
        self.general_tab = DarkModeTab(self.notebook)
        self.volumes_tab = DarkModeTab(self.notebook)
        self.ports_tab = DarkModeTab(self.notebook)
        self.environment_tab = DarkModeTab(self.notebook)
        self.command_tab = DarkModeTab(self.notebook)

        #Font shortcuts
        tab_label_font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Set dark mode colors for tabs and larger font for labels
        self.notebook.SetBackgroundColour(dark_charcoal)
        tabs = [
            ("General", self.general_tab),
            ("Volumes", self.volumes_tab),
            ("Ports", self.ports_tab),
            ("Environment", self.environment_tab),
            ("Command", self.command_tab)
        ]
        for label, tab in tabs:
            self.notebook.AddPage(tab, label)
            tab.SetBackgroundColour(dark_charcoal)
            self.notebook.SetFont(tab_label_font)

        # General tab
        self.container_name_label = wx.StaticText(self.general_tab, label="Container Name:")
        self.container_name_label.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.container_name_label.SetForegroundColour(wx.WHITE)
        ContainerEditor.container_name_text = wx.TextCtrl(self.general_tab,
                                                          value=str(helm.get_container_by_id(ContainerEditor.id).name))

        self.container_image_label = wx.StaticText(self.general_tab, label="Container Image:")
        self.container_image_label.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.container_image_label.SetForegroundColour(wx.WHITE)
        choices = ['Gameplex-Software/Nginx', 'Gameplex-Software/BusyBox', 'Gameplex-Software/Apache',
                   'Gameplex-Software/NginxPlus']
        ContainerEditor.container_image_text = wx.ComboBox(self.general_tab, choices=choices)

        static_box = wx.StaticBox(self.general_tab, label="Container Details")
        general_sizer = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        static_box_sizer.Add(self.container_name_label, 0, wx.ALL | wx.LEFT, 5)
        static_box_sizer.Add(ContainerEditor.container_name_text, 0, wx.ALL | wx.EXPAND, 5)

        static_box_sizer.Add(self.container_image_label, 0, wx.ALL | wx.LEFT, 5)
        static_box_sizer.Add(self.container_image_text, 0, wx.ALL | wx.EXPAND, 5)

        general_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.general_tab.SetSizer(general_sizer)

        # Volumes tab
        self.ports_table = VolumesTable(self.volumes_tab)
        self.add_volume_row_button = wx.Button(self.volumes_tab, label="Add Mount")
        self.add_volume_row_button.Bind(wx.EVT_BUTTON, self.on_add_volumes_row)

        self.ports_table.SetGridLineColour(wx.Colour(64, 64, 64))

        volumes_sizer = wx.BoxSizer(wx.VERTICAL)
        volumes_sizer.Add(self.ports_table, 1, wx.EXPAND | wx.ALL, 5)
        volumes_sizer.Add(self.add_volume_row_button, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.ports_tab.SetSizer(volumes_sizer)

        # Ports tab
        self.ports_table = PortsTable(self.ports_tab)
        self.add_port_row_button = wx.Button(self.ports_tab, label="Add Rule")
        self.add_port_row_button.Bind(wx.EVT_BUTTON, self.on_add_ports_row)

        self.ports_table.SetGridLineColour(wx.Colour(64, 64, 64))

        ports_sizer = wx.BoxSizer(wx.VERTICAL)
        ports_sizer.Add(self.ports_table, 1, wx.EXPAND | wx.ALL, 5)
        ports_sizer.Add(self.add_port_row_button, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.ports_tab.SetSizer(ports_sizer)

        # Environment tab
        environment_sizer = wx.BoxSizer(wx.VERTICAL)

        static_box = wx.StaticBox(self.environment_tab, label="Container Environment Variables")
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        environment_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.environment_tab.SetSizer(environment_sizer)

        # Command tab
        command_sizer = wx.BoxSizer(wx.VERTICAL)

        static_box = wx.StaticBox(self.command_tab, label="Container docker Run Command")
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        command_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.command_tab.SetSizer(command_sizer)

        self.container_command_label = wx.StaticText(self.command_tab, label="Container Command:")
        self.container_command_label.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.container_command_label.SetForegroundColour(wx.WHITE)
        helm.set_engine_manual('docker')

        # = value=str(helm.get_run_command(container_id=ContainerEditor.id))
        ContainerEditor.container_command_text = wx.TextCtrl(self.command_tab,
                                                             value=str("Hello World!"))

        static_box = wx.StaticBox(self.command_tab, label="Container Details")
        command_sizer = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        static_box_sizer.Add(self.container_command_label, 0, wx.ALL | wx.LEFT, 5)
        static_box_sizer.Add(ContainerEditor.container_command_text, 0, wx.ALL | wx.EXPAND, 5)

        command_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.command_tab.SetSizer(command_sizer)

        # End of tabs
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

        self.cancel_button.SetBackgroundColour(space_gray)
        self.save_button.SetBackgroundColour(space_gray)
        self.apply_button.SetBackgroundColour(space_gray)

        self.notebook.SetBackgroundColour(dark_charcoal)

        self.container_name_label.SetBackgroundColour(dark_charcoal)
        self.container_image_label.SetBackgroundColour(dark_charcoal)

        self.container_name_label.SetForegroundColour(wx.WHITE)
        self.container_image_label.SetForegroundColour(wx.WHITE)

        self.container_name_text.SetBackgroundColour(dark_charcoal)
        self.container_image_text.SetBackgroundColour(dark_charcoal)
        self.container_command_text.SetBackgroundColour(dark_charcoal)

        self.ports_table.SetBackgroundColour(space_gray)
        self.add_port_row_button.SetBackgroundColour(space_gray)
        self.add_port_row_button.SetBackgroundColour(space_gray)

        self.SetBackgroundColour(dark_charcoal)

        # Set the text color in textboxes
        self.container_name_text.SetForegroundColour(wx.WHITE)
        self.container_image_text.SetForegroundColour(wx.WHITE)
        self.container_command_text.SetForegroundColour(wx.WHITE)

        self.ports_table.SetForegroundColour(wx.WHITE)

        self.cancel_button.SetForegroundColour(wx.WHITE)
        self.save_button.SetForegroundColour(wx.WHITE)
        self.apply_button.SetForegroundColour(wx.WHITE)

        # bind events to buttons
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save)
        self.apply_button.Bind(wx.EVT_BUTTON, self.on_apply)

    def on_apply(self, event):
        container_name = self.container_name_text.GetValue()
        container_image = self.container_image_text.GetValue()

        helm.rename_container(str(ContainerEditor.id), str(container_name))
        print("Applied changes to container: ", self.id)

    def on_save(self, event):
        self.on_apply()
        print("Saved", ContainerEditor.id)
        self.EndModal(wx.ID_CANCEL)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)

    def on_add_ports_row(self, event):
        num_port_rows = self.ports_table.GetNumberRows()
        self.ports_table.InsertRows(num_port_rows)

    def on_add_volumes_row(self, event):
        num_volume_rows = self.volumes_table.GetNumberRows()
        self.volumes_table.InsertRows(num_volume_rows)