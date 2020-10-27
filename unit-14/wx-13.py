import wx

class MyFrame(wx.Frame):
    def __init__(self, parent=None, title="wxpython Demo"):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.Show()





app=wx.App(False)
frame=MyFrame()
app.MainLoop()