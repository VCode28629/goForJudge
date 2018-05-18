#!usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'VCode'

import wx
from src import search

class MainWindow(wx.Frame):
    def __init__(self, parent, title, size):
        wx.Frame.__init__(self, parent=parent, title=title, size=size)

def choose_contest():
    dlg = wx.SingleChoiceDialog(None, '选择比赛', 'go for judge - contests', search.search_contests(), wx.ID_OK)
    if dlg.ShowModal() == wx.ID_OK: 
        contest = dlg.GetStringSelection()
    dlg.Destroy()
    return contest



def main():
    def score_init():
        main_panel.SetSizer(main_sizer)
        main_sizer.Add(wx.Button(main_panel, label = '刷新', size = (20, 10)), 0, wx.EXPAND)
        main_panel.SetSizer(main_sizer)
        for problem in problems:
            main_sizer.Add(wx.StaticText(main_panel, -1, label = problem), 0, wx.EXPAND)
            main_panel.SetSizer(main_sizer)
        main_sizer.Add(wx.StaticText(main_panel, -1, label = '总分'), 0, wx.EXPAND)
        main_panel.SetSizer(main_sizer)
        for student in students:
            main_sizer.Add(wx.StaticText(main_panel, -1, label = student), 0, wx.EXPAND)
            main_panel.SetSizer(main_sizer)
            for scores in problems:
                main_sizer.Add(wx.StaticText(main_panel, -1, label = '0'), 0, wx.EXPAND)
                main_panel.SetSizer(main_sizer)
            main_sizer.Add(wx.StaticText(main_panel, -1, label = '0'), 0, wx.EXPAND)
            main_panel.SetSizer(main_sizer)
    def Refresh():
        pass
    def reselect_conteset():
        pass
    def judge():
        pass
    
    app = wx.App(False)

    contest = choose_contest()
    problems = search.search_problems(contest)
    students = search.search_students(contest)

    win = MainWindow(None, 'go for judge', (70 * (len(problems) + 2), 50 * (len(students) + 1)))

    main_panel = wx.Panel(win)
    main_sizer = wx.GridSizer(rows = len(students) + 1, cols = len(problems) + 2, vgap = 5, hgap = 5)

    score_init()

    win.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
