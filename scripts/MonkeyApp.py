import wx
import cv2
import os

from wx.core import ID_ANY

#from https://stackoverflow.com/questions/62678893/how-do-i-create-a-wxpython-frame-with-opencv-webcam-video-and-other-wx-component

cap = cv2.VideoCapture('/Users/vogg/Documents/Python/learning-opencv/data/VID_20210223_123630_0.mp4')

with open('/Users/vogg/Documents/Python/learning-opencv/data/results.txt') as f:
    lines = f.readlines()



class ImagePanel(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        self.count = 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, self.count)
        ret, self.frame = cap.read()
        height, width = self.frame.shape[:2]
        self.new_w, self.new_h = 800, int(800 * height/width)
    

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

        #Draw Rectangles
        frames = [int(item.split(",")[0]) for item in self.Parent.Parent.lines]
        indices = [i for i, x in enumerate(frames) if x == (self.count +1)]
        dets = [self.Parent.Parent.lines[i] for i in indices]
        
        for det in dets:
            dt = det.split(",")

            i = float(dt[1])
            c1 = float(dt[2])
            c2 = float(dt[3])
            c3 = float(dt[4])
            c4 = float(dt[5])

            color = (i * 100 % 255, i * 75 % 255, i * 50 % 255)

            cv2.rectangle(self.frame, (int(c1), int(c2)), (int(c1 + c3), int(c2 + c4)), color, 4)
            cv2.rectangle(self.frame, (int(c1),int(c2 + 30)), (int(c1 + 30),int(c2)), (255,255,255), cv2.FILLED)
            cv2.putText(self.frame, dt[1], (int(c1 + 5),int(c2 + 25)), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0))

        self.frame = cv2.resize(self.frame, (self.new_w, self.new_h), interpolation = cv2.INTER_AREA)
 
        self.bmp = wx.Bitmap.FromBuffer(self.new_w, self.new_h, self.frame)
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def PriorFrame(self, event):
        self.count = self.count - 1
        cap.set(cv2.CAP_PROP_POS_FRAMES, self.count)
        ret, self.frame = cap.read()
        if ret:
            self.Refresh()
    

    def NextFrame(self, event):
        self.count = self.count + 1
        cap.set(cv2.CAP_PROP_POS_FRAMES, self.count)
        ret, self.frame = cap.read()
        if ret:
            self.Refresh()

    def GoToFrame(self, event, value):
        self.count = value
        cap.set(cv2.CAP_PROP_POS_FRAMES, value)
        ret, self.frame = cap.read()
        if ret:
            self.Refresh()




class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent = parent)

        #Widgets and Panels
        self.image = ImagePanel(self)

        back = wx.Button(self, style = wx.BU_EXACTFIT)
        back.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_GO_BACK)

        forward = wx.Button(self, style = wx.BU_EXACTFIT)
        forward.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD)

        self.slider = wx.Slider(self, id=wx.ID_ANY, value=0, minValue=0, maxValue=390)

        self.find = wx.TextCtrl(self, size = (50,20), value = "Find")
        self.replace = wx.TextCtrl(self, size = (50, 20), value = "Replace")

        replButton = wx.Button(self, style = wx.BU_EXACTFIT, label = "OK")


        
        #Layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(back, 0, wx.ALL, 5)
        sizer.Add(self.slider, 1, wx.ALL|wx.EXPAND, 5)
        sizer.Add(forward, 0, wx.ALL, 5)
        sizer.Add(self.find, 0, wx.ALL|wx.EXPAND, 5)
        sizer.Add(self.replace, 0, wx.ALL|wx.EXPAND, 5)
        sizer.Add(replButton, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.image, 1, wx.EXPAND, 0)
        main_sizer.Add(sizer, 0)

        self.SetSizer(main_sizer)

        #Events
        back.Bind(wx.EVT_BUTTON, self.GoBack)
        forward.Bind(wx.EVT_BUTTON, self.GoForward)
        self.slider.Bind(wx.EVT_SCROLL, self.MoveSlider)
        replButton.Bind(wx.EVT_BUTTON, self.ClickOK)


    def GoBack(self, event):
        self.image.PriorFrame(event)
        self.slider.SetValue(self.slider.GetValue()-1)

    def GoForward(self, event):
        self.image.NextFrame(event)
        self.slider.SetValue(self.slider.GetValue()+1)

    def MoveSlider(self, event):
        value = self.slider.GetValue()
        self.image.GoToFrame(event, value)

    def ClickOK(self, event):
        for i, line in enumerate(self.Parent.lines):
            fields = line.split(",")
            if str(fields[1]) == str(self.find.GetValue()):
                print("Uhu")
                fields[1] = self.replace.GetValue()
            self.Parent.lines[i] = ",".join(fields)
        self.Parent.Refresh()


        




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

    def OnNew(self, event):
        print("New Item")

    def OnOpen(self, event):
        wildcard = "TXT files (*.txt)|*.txt"
        dialog = wx.FileDialog(self.parentFrame, "Open Text Files", wildcard,
                                style = wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)
        
        if dialog.ShowModal() == wx.ID_CANCEL:
            return None

        path = dialog.GetPath()
        if os.path.exists(path):
            with open(path) as f:
                self.parentFrame.lines = f.readlines()
    
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

class MainFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title='Review Video', size = (800, 600))
        self.cap = cap
        self.lines = lines
        MainPanel(self)
        self.Show()

        menuBar = wx.MenuBar()


        fileMenu = FileMenu(parentFrame=self)
        menuBar.Append(fileMenu, '&File')


        self.SetMenuBar(menuBar)


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()