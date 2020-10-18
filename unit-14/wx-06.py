import wx

class MyControl(wx.Frame):
    def __init__(self, parent = None, title = "My Control"):
        wx.Frame.__init__(self, parent = parent, title = title, size = (640, 480))
        # 多选文本框
        self.txteditor = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # 单行文本框
        self.txtsimple = wx.TextCtrl(self, style= wx.TE_LEFT)
        # 




        self.Show(True)


app = wx.App(False)
win = MyControl()
app.MainLoop()
