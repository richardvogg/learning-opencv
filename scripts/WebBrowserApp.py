import wx
from wx import html2

class myApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        webbrowser = WebFrame(parent = None, title = "My Web App")
        webbrowser.Show()


class WebFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title = title, pos = (100,100))

        self._browser = html2.WebView.New(self)
        self._browser.LoadURL("www.google.com")

        self._navbar = NavBar(self, self._browser)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._navbar, 0, wx.EXPAND)
        sizer.Add(self._browser, 1, wx.EXPAND)

        self.SetSizer(sizer)


class NavBar(wx.Panel):
    def __init__(self, parent, browser):
        super().__init__(parent)
        self._browser = browser
        self._url = wx.TextCtrl(parent = self, style = wx.TE_PROCESS_ENTER)
        self._url.SetHint("Enter URL address")

        back = wx.Button(self, style = wx.BU_EXACTFIT)
        back.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_GO_BACK)

        forward = wx.Button(self, style = wx.BU_EXACTFIT)
        forward.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(back, 0, wx.ALL, 5)
        sizer.Add(forward, 0, wx.ALL, 5)
        sizer.Add(self._url, 0, wx.ALL, 5)
        
        self.SetSizer(sizer)

    def OnEnter(self, event):
        self.browser.LoadURL(self._url.Value)
    
    def GoBack(self, event):
        event.Enable(self._browser.CanGoBack())
        self._browser.GoBack()

    def GoForward(self, event):
        event.Enable(self._browser.CanGoForward())
        self._browser.GoForward()


if __name__ == "__main__":
    app = myApp()
    app.MainLoop()
