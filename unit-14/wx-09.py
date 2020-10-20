import wx

class NoteBook(wx.Frame):
    def __init__(self, parent = None, title = "NoteBook"):
        wx.Frame.__init__(self, parent = parent, title = title, size = (640, 480))

        # create MenuBar
        menubar = wx.MenuBar()
        # create file menu
        menufile = wx.Menu()
        menuopen = menufile.Append(wx.ID_OPEN, u"打开",u"打开文件")
        menufile.AppendSeparator()
        menuaboutme = menufile.Append(wx.ID_ABORT,u"关于", u"关于一个简单的记事本")
        menuexit = menufile.Append(wx.ID_EXIT, u"退出", u"退出记事本应用程序")
        menubar.Append(menufile, u"文件")

        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.onOpenfile, menuopen)
        self.Bind(wx.EVT_MENU, self.onAboutme, menuaboutme)
        self.Bind(wx.EVT_MENU, self.onExit, menuexit)

        #create a Multiline text to edit
        self.txteditor = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        #create a status bar
        self.CreateStatusBar()

        self.Show(True)




    def onAboutme(self, event):
        print("open a onAboutme messagebox")

    def onExit(self, event):
        print("onExit application")
        self.Close()

    def onOpenfile(self, event):
        print("open a file to edit")


app = wx.App(False)
win = NoteBook()
app.MainLoop()
