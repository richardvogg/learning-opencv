import wx
import wx.lib.scrolledpanel as sp
import threading
import traceback

class EditorPane(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnSize(self, event):
        print('editorpane:', event.GetSize())

class Editor(sp.ScrolledPanel):
    def __init__(self, parent):
        sp.ScrolledPanel.__init__(self, parent)
        self.SetupScrolling()

        # editor pane (Panel) in vertical box sizer
        self.pane = EditorPane(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        self.sizer.Add(self.pane)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnSize(self, event):
        viewSize = event.GetSize()
        scale = wx.Size(1, 3)
        size =wx.Size(viewSize.x*scale.x, viewSize.x*scale.y)
        print(viewSize, scale, size)
        self.pane.SetMinSize(size)
        event.Skip()

class AppFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "tsan")
        self.SetBackgroundColour(wx.Colour(180, 180, 180))

        # editor(ScrolledPanel) in vertical box sizer
        vsizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vsizer)
        hexEditor = Editor(self)
        hexEditor.SetBackgroundColour(wx.Colour(255, 255, 255))
        vsizer.Add(hexEditor, 1, wx.EXPAND)
       
app = wx.PySimpleApp()
frame = AppFrame()
frame.Show()
app.MainLoop()