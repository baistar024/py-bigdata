import wx

class NoteBook(wx.Frame):
    def __init__(self, parent = None, title = "NoteBook"):
        wx.Frame.__init__(self, parent = parent, title = title, size = (640, 480))
        self.txtContent = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.Show()
app = wx.App(False)
frame = NoteBook()
app.MainLoop()


