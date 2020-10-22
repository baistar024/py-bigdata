import wx

class Appcliation(wx.Frame):
    def __init__(self, parent = None, title = "Demo about Frame"):
        wx.Frame.__init__(self, parent = parent, title = title, size = (640, 480))
        self.txteditor = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.menubar = wx.MenuBar()

        filemenu = wx.Menu()
        filemenu.Append(wx.ID_OPEN, u"打开", u"打开一个文本文件")
        filemenu.Append(wx.ID_ABOUT, u"关于", u"关于本软件的说明")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, u"退出",u"退出本软件系统")

        editmenu = wx.Menu()
        editmenu.Append(wx.ID_COPY, u"复制",u"将内容复制到剪贴板")
        editmenu.Append(wx.ID_CUT, u"剪贴",u"将内容剪贴到剪贴板")
        editmenu.Append(wx.ID_PASTE, u"粘贴",u"自剪贴板粘贴到光标处")
        editmenu.Append(wx.ID_DELETE, u"删除",u"自剪贴板粘贴到光标处")

        self.menubar.Append(filemenu,u"文件")
        self.menubar.Append(editmenu, u"编辑")
        self.menubar

        self.SetMenuBar(self.menubar)
        self.Show()
        self.Bind(wx.EVT_MENU, self.onExit)

    def onExit(self, e):
        self.Close()


app = wx.App()
win = Appcliation()
app.MainLoop()