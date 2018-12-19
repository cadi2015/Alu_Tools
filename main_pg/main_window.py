#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Hello World, but with more meat
没招，不加UTF-8，中文编译不过去  作用是设置源文件编码格式为:UTF-8
"""

import wx

VERSION = "1.0"

class MainActivity(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self):

        super(MainActivity, self).__init__(parent = None,title = "首页", size = (800, 400))
        self.Centre()
        self.initMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("Alu Tools")

        pnl = wx.Panel(self)

        firstTxt = wx.StaticText(pnl, label="Hello World", style = wx.ALIGN_CENTRE)
        secondBtn = wx.Button(pnl, label = "second")
        thirdBtn = wx.Button(pnl, label = "second Button")

        rootHorizontalSizer = wx.BoxSizer(wx.HORIZONTAL)
        operateZoneVerticalSizer = wx.BoxSizer(wx.VERTICAL)
        operateZoneVerticalSizer.Add(firstTxt,0,wx.EXPAND, 20) #哥啊，实例方法怎么都是大写字母开头，我好生不适应
        operateZoneVerticalSizer.Add(secondBtn,0, wx.EXPAND)
        operateZoneVerticalSizer.Add(thirdBtn,0,wx.ALIGN_CENTER_HORIZONTAL)

        baseInfoTxt = wx.StaticText(pnl, label = "连接设备:")
        resultInfoTxt = wx.StaticText(pnl, label = "结果")

        baseInfoZoneVertical = wx.BoxSizer(wx.VERTICAL)
        baseInfoZoneVertical.Add(baseInfoTxt,0,wx.EXPAND)

        resultInfoZoneVertical = wx.BoxSizer(wx.VERTICAL)
        resultInfoZoneVertical.Add(resultInfoTxt,0,wx.EXPAND)


        showZoneVerticalSizer = wx.BoxSizer(wx.VERTICAL)
        showZoneVerticalSizer.Add(baseInfoZoneVertical,1)
        showZoneVerticalSizer.Add(resultInfoZoneVertical,1)

        rootHorizontalSizer.Add(operateZoneVerticalSizer,1)
        rootHorizontalSizer.Add(showZoneVerticalSizer,1)
        pnl.SetSizer(rootHorizontalSizer)

    def initMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.

        """


        settingMenu = wx.Menu()
        settingPackageNameItem = settingMenu.Append(-1, "设置包名",
                "在这里设置应用的包名")
        settingMenu.AppendSeparator()

        aboutMenu = wx.Menu()
        versionItem = aboutMenu.Append(-1,"版本","版本号")


        menuBar = wx.MenuBar()
        menuBar.Append(settingMenu, "设置")
        menuBar.Append(aboutMenu, "关于")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, MainActivity.OnSettingPackageNameClick, settingPackageNameItem)
        self.Bind(wx.EVT_MENU, self.OnAboutVersionClick, versionItem)


    @staticmethod
    def OnSettingPackageNameClick(event):
        """Say hello to the user."""
        wx.MessageBox("设置包名")

    @staticmethod
    def OnAboutVersionClick(event):
        """Display an version dialog"""
        wx.MessageBox("当前版本:" + str(VERSION))


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MainActivity()
    frm.Show()
    app.MainLoop()