import wx

class myApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        self.InitFrame()
    
    def InitFrame(self):
        frame = myFrame(parent = None, title = "Widgets", pos = (100, 200))
        frame.Show()


class myFrame(wx.Frame):
    def __init__(self, parent, title, pos=(100, 200)):
        super().__init__(parent = parent, title = title, pos = pos)
        self.OnInit()

    def OnInit(self):
        panel = myPanel(parent = self)

class myPanel(wx.Panel):
    def __init__(self, parent, fps = 15):
        super().__init__(parent = parent)
        text1 = wx.StaticText(self, id = wx.ID_ANY, label = "TextCtrl")
        textbox = wx.TextCtrl(self, id = wx.ID_ANY, value = "Your Input")


        text2 = wx.StaticText(self, id = wx.ID_ANY, label = "RadioButton")
        radio_button = wx.RadioButton(self, id = wx.ID_ANY, label = "RadioButton1")
        radio_button2 = wx.RadioButton(self, id = wx.ID_ANY, label = "RadioButton2")
        
        text3 = wx.StaticText(self, id = wx.ID_ANY, label = "CheckBox")
        checkbox1 = wx.CheckBox(self, id = wx.ID_ANY, label = "CheckBox1")
        checkbox2 = wx.CheckBox(self, id = wx.ID_ANY, label = "CheckBox2")


        text4 = wx.StaticText(self, id = wx.ID_ANY, label = "Button/ToggleButton") 
        button = wx.Button(self, id = wx.ID_ANY, label = "Button")
        toggle_button = wx.ToggleButton(parent = self, label = "ToggleButton")
        
        text5 = wx.StaticText(self, id = wx.ID_ANY, label = "Choice")
        choice = wx.Choice(self, id = wx.ID_ANY, choices = ['New', 'None', 'C'])
        
        text6 = wx.StaticText(self, id = wx.ID_ANY, label = "ListBox")
        list_box = wx.Choice(self, id = wx.ID_ANY, choices = ['New', 'None', 'C'])
        
        ## Layout
        
        sizer1 = wx.BoxSizer(wx.HORIZONTAL)

        sizer1.Add(text1)
        sizer1.Add(textbox)

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2.Add(text2)
        sizer2.Add(radio_button)
        sizer2.Add(radio_button2)

        sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer3.Add(text3)
        sizer3.Add(checkbox1)
        sizer3.Add(checkbox2)


        sizer4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer4.Add(text4)
        sizer4.Add(button)
        sizer4.Add(toggle_button)

        sizer5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer5.Add(text5)
        sizer5.Add(choice)

        sizer6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer6.Add(text6)
        sizer6.Add(list_box)

        sizer7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer7.Add(text7)
        sizer7.Add(list_control)
        

        
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        main_sizer.Add(sizer1)
        main_sizer.Add(sizer2)
        main_sizer.Add(sizer3)
        main_sizer.Add(sizer4)
        main_sizer.Add(sizer5)
        main_sizer.Add(sizer6)

        self.SetSizer(main_sizer)

        

if __name__ == "__main__":
    app = myApp()
    app.MainLoop()
