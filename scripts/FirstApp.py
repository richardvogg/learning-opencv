import wx

class myApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        self.InitFrame()
    
    def InitFrame(self):
        frame = myFrame(parent = None, title = "Labelling", pos = (100, 200))
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
        self._dont_show = False

        welcomeText = wx.StaticText(self, id = wx.ID_ANY, label = "To see the R-Vogg-Blog click below", pos = (20,20))
        self._textbox = wx.TextCtrl(parent = self, value = "Enter name here: ", pos = (20, 50))

        

        self._button = wx.Button(parent = self, label = "Done!", pos = (20, 80))
        self._button.Bind(event = wx.EVT_BUTTON, handler = self.OnSubmit)

        

    def ShowDialog(self):

        if self._dont_show == True:
            return None

        dlg = wx.RichMessageDialog(parent = None,
                                message = "Hellochen",
                                caption = "Piu Piu",
                                style = wx.YES_NO|wx.CANCEL|wx.CENTER)
        dlg.ShowCheckBox("Click here to never show message again")
        dlg.ShowModal()

        if dlg.IsCheckBoxChecked():
            self._dont_show = True


    def OnSubmit(self, event):
        #open webbrowser
        #
        print(self._textbox.GetValue())

        self.ShowDialog()



if __name__ == "__main__":
    app = myApp()
    app.MainLoop()
