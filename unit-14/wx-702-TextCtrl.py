import wx

class TextCtrlFrame(wx.Frame):
    def __init__(self, parent=None, title="Control Create"):
        wx.Frame.__init__(self,parent=parent,title=title, size=(640,480))
        self.CreateControl()

        self.Show()


    def CreateControl(self):
        btn=wx.Button(self, id=wx.ID_OK)

    def ShowInfo(self):
        pass


app=wx.App()
frame=TextCtrlFrame()
frame.Show()
app.MainLoop()