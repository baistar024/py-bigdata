# wx-12
# about button example

import wx
class Control(wx.Frame):
    def __int__(self, parent=None, title="Hello, button"):
        wx.Frame.__init__(self,parent=parent, title=title)
        self.btn01=wx.Button()

        self.Show()
    def showInfo(self):
        print(self.__str__())

app=wx.App()
frame=Control()
app.MainLoop()