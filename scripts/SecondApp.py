import wx
from wx.core import ID_ANY


class myFrame(wx.Frame):
    def __init__(self, parent, title, pos=(500, 500)):
        super().__init__(parent = parent, title = title, pos = pos)
        self.OnInit()

    def OnInit(self):
        panel = myForm(parent = self)

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
    app = wx.App(clearSigInt=True)
    frame = myFrame(parent = None, title = "labelling", pos = (100, 200))
    frame.Show()
    app.MainLoop()
