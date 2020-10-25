import wx
import wx.adv as adv
app=wx.App(False)
frame=wx.Frame(None,wx.ID_ANY,"adv.calendar")
advcalend=adv.CalendarCtrl(frame, )
frame.Show()
app.MainLoop()