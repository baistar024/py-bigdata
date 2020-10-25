import wx


app=wx.App(False)
frame = wx.Frame(None,wx.ID_ANY,"Hello world")
txteditor = wx.TextCtrl(frame, style=wx.TE_MULTILINE)
frame.Show()
app.MainLoop()