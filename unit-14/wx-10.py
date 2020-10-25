import wx, os

class MessageCenter(wx.Frame):
    def __init__(self, parent=None, title="Demo about NoteBook"):
        wx.Frame.__init__(self, parent=parent, title=title, size=(640, 480))

        self.menubar=wx.MenuBar()
        filemenu= wx.Menu()
        filemenu.Append( wx.ID_OPEN, u"打开", u"打开一个文本文件")
        filemenu.Append(wx.ID_ABOUT, u"关于", u"关于本应用程序的说明")
        self.menubar.Append(filemenu,u"文件")
        self.SetMenuBar(self.menubar)


        self.CreateStatusBar()
        self.Show()

app=wx.App(False)
frame=MessageCenter()
app.MainLoop()