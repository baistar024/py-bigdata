import wx

class NoteBook(wx.Frame):
    def __init__(self, parent = None, title = "NoteBook"):
        wx.Frame.__init__(self, parent = parent, title = title, size = (640, 480))
        self.txtContent = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        # create Menu
        # s1  创建菜单条
        menuBar = wx.MenuBar()
        # s2 创建菜单
        fileMenu = wx.Menu()
        # s3 创建菜单命令
        fileMenu.Append(wx.ID_ABORT, u"关于", u"关于程序信息")
        fileMenu.Append(wx.ID_EXIT, u"退出",u"终止应用程序")
        # s4 将菜单放入菜单条
        menuBar.Append(fileMenu, u"文件")
        # s5 将菜单加入应用程序窗口
        self.SetMenuBar(menuBar)



        #add other controls
        self.CreateStatusBar()


        self.Show()
app = wx.App(False)
frame = NoteBook()
app.MainLoop()


