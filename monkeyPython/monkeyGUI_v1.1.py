#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
import os
import subprocess
import time

nowTime=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))

def get_screen_size(window):
    return window.winfo_screenwidth(),window.winfo_screenheight()

def get_window_size(window):
    return window.winfo_reqwidth(),window.winfo_reqheight()

def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)



class MainAc(object):
    
    def __init__(self):
        self.windowWidthMin = 400
        self.windowHeightMin = 300
        self.windowWidthMax = 600
        self.windowHeightMax = 400
        self.root = Tkinter.Tk()
        self.root.title("cheez Monkey(本地版)v_1.1")
        self.root.maxsize(self.windowWidthMax, self.windowHeightMax)
        self.root.minsize(self.windowWidthMin, self.windowHeightMin)
        self.root.wm_attributes('-topmost',1) #窗口置顶
        center_window(self.root, self.windowWidthMin, self.windowHeightMin)
        
        self.btn_start = Tkinter.Button(self.root, command = self.startBtn, text = "Monkey开始")
    
        self.btn_stop = Tkinter.Button(self.root , text = "Monkey停止",command=self.stopBtn)
    
        self.btn_pull_anr = Tkinter.Button(self.root, text = "拉取ANR traces.txt", command=self.pullTraces)
    
    
    # 完成布局
    def gui_arrang(self):

        self.btn_start.pack() #完成start Btn
        self.btn_stop.pack()  #完成stop Btn
        self.btn_pull_anr.pack() #完成pull Btn
    
    def startBtn(self):
        os.popen("python launchMonkey_v1.2.py")

    def stopBtn(self):
        os.popen("python killMonkey_v1.1.py")

    def pullTraces(self):
        os.popen("adb pull /data/anr/traces.txt ./ANR_" + nowTime)



def main():
    # 初始化对象
    FL = MainAc()
    # 进行布局
    FL.gui_arrang()
    # 主程序执行
    Tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()


