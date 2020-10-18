# step 1. import wx
import wx
# step 2. create an app object
app = wx.App(False)
# step 3. app object create a window (Frame)
# Frame(Parent, Id, Title)
# wx.Frame(Parent, ID, Title, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name="frame")
frame = wx.Frame(None, wx.ID_ANY, "Hello world")
frame.Show()
app.MainLoop()

