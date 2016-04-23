#!/user/bin/python
# -*- coding:utf-8 -*-


import wx
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(
                parent=None,
                id = -1,
                title = 'Panel',
                pos = (100,100),
                size = (300,600),
                style = wx.DEFAULT_FRAME_STYLE,
                name = "admin"
                )
        panel = wx.Panel(frame,-1)
        frame.Show() 
        return True

app = MyApp()
app.MainLoop()


'''
app = wx.PySimpleApp()
frame = wx.Frame(parent=None,title='Hello,wxpython')
frame.Show(True)
app.MainLoop()

'''












