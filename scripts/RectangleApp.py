import wx
# from https://github.com/PythonCHB/wxPythonDemos/blob/3c091176ea0c2385c9eafd599f6139f0bd61215e/test_overlay2.py

class OverlayPanel(wx.Panel):
    def __init__(self, parent):
        super(OverlayPanel, self).__init__(parent)
        self.overlay = wx.Overlay()
        self.permRect = None
        self.selectionStart = None
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        if self.permRect:
            dc.SetBrush(wx.RED_BRUSH)
            dc.DrawRectangle(self.permRect)


    def OnLeftDown(self, evt):
        self.CaptureMouse()
        self.overlay = wx.Overlay()
        self.selectionStart = evt.Position


    def OnLeftUp(self, evt):
        if not self.HasCapture():
            return
        self.ReleaseMouse()
        self.permRect = wx.Rect((self.selectionStart[0], 0), 
                                (evt.Position[0]-self.selectionStart[0],20))

        self.selectionStart = None
        self.Refresh()



if __name__ == '__main__':
    app = wx.App(False)
    f = wx.Frame(None)

    p = OverlayPanel(f)
    f.Show()
    app.MainLoop()