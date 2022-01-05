import wx
import os

class myApp(wx.App):
    def __init__(self):
        super().__init__()
        
        frame = myFrame(parent = None, title = "Labelling")
        frame.Show()


class myFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent = parent, title = title, size = (500,500), pos=(100, 100))
        self.InitUI()

    def InitUI(self):
        
        menuBar = wx.MenuBar()


        fileMenu = FileMenu(parentFrame=self)
        menuBar.Append(fileMenu, '&File')
        
        editMenu = EditMenu(parentFrame = self)
        menuBar.Append(editMenu, '&Edit')


        self.SetMenuBar(menuBar)
        self.Center()

        self.panel = myForm(parent = self)


class FileMenu(wx.Menu):
    def __init__(self, parentFrame):
        super().__init__()
        self.OnInit()
        self.parentFrame = parentFrame
    
    def OnInit(self):
        newItem = wx.MenuItem(parentMenu = self, id = wx.ID_NEW, text = "&New\tCTRL+N")
        self.Append(newItem)
        self.Bind(event = wx.EVT_MENU, handler = self.OnNew, source = newItem)

        openItem = wx.MenuItem(parentMenu = self, id = wx.ID_OPEN, text = "&Open")
        self.Append(openItem)
        self.Bind(event = wx.EVT_MENU, handler = self.OnOpen, source = openItem)

        saveItem = wx.MenuItem(parentMenu = self, id = wx.ID_SAVE, text = "&Save")
        self.Append(saveItem)
        self.Bind(event = wx.EVT_MENU, handler = self.OnSave, source = saveItem)

        quitItem = wx.MenuItem(parentMenu = self, id = wx.ID_EXIT, text = "&Quit")
        self.Append(quitItem)
        self.Bind(event = wx.EVT_MENU, handler = self.OnQuit, source = quitItem)

    def OnNew(self):
        print("New Item")

    def OnOpen(self, event):
        wildcard = "TXT files (*.txt)|*.txt"
        dialog = wx.FileDialog(self.parentFrame, "Open Text Files", wildcard,
                                style = wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)
        
        if dialog.ShowModal() == wx.ID_CANCEL:
            return None

        path = dialog.GetPath()
        if os.path.exists(path):
            with open(path) as myfile:
                for line in myfile:
                    self.parentFrame.panel.input1.WriteText(line)
    
    def OnSave(self, event):
        dialog = wx.FileDialog(self.parentFrame, "Save your data", defaultFile = "test.txt",
                                style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        
        if dialog.ShowModal() == wx.ID_CANCEL:
            return None

        path = dialog.GetPath()
        data = self.parentFrame.text.GetValue()
        print(data)
        data = data.split("\n")
        with open(path, "w+") as myfile:
            for line in data:
                myfile.write(line+"\n")

    def OnQuit(self, event):
        self.parentFrame.Close()


class EditMenu(wx.Menu):
    def __init__(self, parentFrame):
        super().__init__()
        self.parentFrame = parentFrame
        self.OnInit()
        

    def OnInit(self):
        cutItem = wx.MenuItem(parentMenu = self, id = wx.ID_CUT, text = "&Cut\tCTRL+X")
        self.Append(cutItem)

        copyItem = wx.MenuItem(parentMenu = self, id = wx.ID_COPY, text = "&Copy\tCTRL+C")
        self.Append(copyItem)

        pasteItem = wx.MenuItem(parentMenu = self, id = wx.ID_PASTE, text = "&Paste\tCTRL+V")
        self.Append(pasteItem)




class myForm(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.InitForm()

    def InitForm(self):
        
        bmp = wx.ArtProvider.GetBitmap(id = wx.ART_FIND,
                                        client = wx.ART_OTHER, size = (16,16))

        titleIco = wx.StaticBitmap(parent = self, id = wx.ID_ANY, bitmap = bmp)
        title = wx.StaticText(parent = self, id = wx.ID_ANY, label = "Monkeys")

        input1Ico = wx.StaticBitmap(parent = self, id = wx.ID_ANY, bitmap = bmp)
        label1 = wx.StaticText(parent = self, id = wx.ID_ANY, label = "Text Control")
        self.input1 = wx.TextCtrl(self, wx.ID_ANY, value = "Your text here")

        input2Ico = wx.StaticBitmap(parent = self, id = wx.ID_ANY, bitmap = bmp)
        label2 = wx.StaticText(parent = self, id = wx.ID_ANY, label = "Spin Control")
        self.input2 = wx.SpinCtrl(self, wx.ID_ANY, value = "0", min = 0, max = 390)

        input3Ico = wx.StaticBitmap(parent = self, id = wx.ID_ANY, bitmap = bmp)
        label3 = wx.StaticText(parent = self, id = wx.ID_ANY, label = "Choices")
        self.input3 = wx.Choice(self, wx.ID_ANY, choices = ['Macaques', 'Baboons', 'Lemurs'])

        input4Ico = wx.StaticBitmap(parent = self, id = wx.ID_ANY, bitmap = bmp)
        label4 = wx.StaticText(parent = self, id = wx.ID_ANY, label = "Checkboxes")
        self.input4_1 = wx.CheckBox(self, label = "Label Activities")
        self.input4_2 = wx.CheckBox(self, label = "Change Boxes")
        self.input4_3 = wx.CheckBox(self, label = "Redraw")

        okBtn = wx.Button(self, wx.ID_ANY, label = "OK")
        cancelBtn = wx.Button(self, wx.ID_ANY, label = "Cancel")


        mainSizer = wx.BoxSizer(wx.VERTICAL)
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        input1Sizer = wx.BoxSizer(wx.HORIZONTAL)
        input2Sizer = wx.BoxSizer(wx.HORIZONTAL)
        input3Sizer = wx.BoxSizer(wx.HORIZONTAL)
        input4Sizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        titleSizer.Add(window = titleIco, proportion = 0, flag = wx.ALL, border = 5)
        titleSizer.Add(window = title, proportion = 0, flag = wx.ALL, border = 5)

        input1Sizer.Add(window = input1Ico, proportion = 0, flag = wx.ALL, border = 5)
        input1Sizer.Add(window = label1, proportion = 0, flag = wx.ALL, border = 5)
        input1Sizer.Add(window = self.input1, proportion = 1, flag = wx.ALL|wx.EXPAND, border = 5)

        input2Sizer.Add(window = input2Ico, proportion = 0, flag = wx.ALL, border = 5)
        input2Sizer.Add(window = label2, proportion = 0, flag = wx.ALL, border = 5)
        input2Sizer.Add(window = self.input2, proportion = 0, flag = wx.ALL, border = 5)

        input3Sizer.Add(window = input3Ico, proportion = 0, flag = wx.ALL, border = 5)
        input3Sizer.Add(window = label3, proportion = 0, flag = wx.ALL, border = 5)
        input3Sizer.Add(window = self.input3, proportion = 0, flag = wx.ALL, border = 5)

        input4Sizer.Add(window = input4Ico, proportion = 0, flag = wx.ALL, border = 5)
        input4Sizer.Add(window = label4, proportion = 0, flag = wx.ALL, border = 5)
        input4Sizer.Add(window = self.input4_1, proportion = 0, flag = wx.ALL, border = 5)
        input4Sizer.Add(window = self.input4_2, proportion = 0, flag = wx.ALL, border = 5)
        input4Sizer.Add(window = self.input4_3, proportion = 0, flag = wx.ALL, border = 5)

        btnSizer.Add(window = okBtn, proportion = 0, flag = wx.ALL, border = 5)
        btnSizer.Add(window = cancelBtn, proportion = 0, flag = wx.ALL, border = 5)

        mainSizer.Add(titleSizer, 0, flag=wx.CENTER|wx.ALL, border=5)
        mainSizer.Add(input1Sizer, 1, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(input2Sizer, 0, wx.ALL, 5)
        mainSizer.Add(input3Sizer, 0, wx.ALL, 5)
        mainSizer.Add(input4Sizer, 0, wx.ALL, 5)
        mainSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        self.Layout()

if __name__ == "__main__":
    app = myApp()
    app.MainLoop()
