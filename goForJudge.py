#!usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'VCode'

import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title, size):
        wx.Frame.__init__(self, parent=parent, title=title, size=size)
        self.Show(True)

def main():
    app = wx.App(False)
    go_for_judge = MainWindow(None, 'go for judge', (800, 600))
    app.MainLoop()

if __name__ == '__main__':
    main()
