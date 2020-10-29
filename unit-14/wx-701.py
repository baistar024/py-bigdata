import wx

class StaticTextFrame(wx.Frame):
    def __init__(self, parent=None,Id=-1, title="Static Text Example",size=(400,400)):
        wx.Frame.__init__(self, parent=parent, id=Id, title=title,size=size)
        self.pnlmain=wx.Panel(self, -1)
        self.lblreversedcol = wx.StaticText(self.pnlmain, -1, "Static Text with reversed colors",(100,10))
        self.lblreversedcol.SetForegroundColour('white')
        self.lblreversedcol.SetBackgroundColour("black")

        self.lblcenter=wx.StaticText(self.pnlmain, -1, "align Center", (100,30),(160,30), wx.ALIGN_CENTER)
        self.lblright=wx.StaticText(self.pnlmain, -1, "align right", (100,50),(160,-1), wx.ALIGN_RIGHT)
        self.lblfont=wx.StaticText(self.pnlmain, -1, "align font", (100,50), (160,-1), wx.ALIGN_RIGHT)

        self.Show()
    def createLabel(self,parent=None,info="", ):
        pass
app=wx.App()
frame=StaticTextFrame()
app.MainLoop()
