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


currentRootPath = ""

def file_name(file_path):
    global currentRootPath
    for root, dirs, files in os.walk(file_path):
        print(root) #当前目录路径
        print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件
        currentRootPath = root
        returnStr = ""
        for item in files:
            if not item.startswith(".",0,1):
                returnStr = item
        return returnStr


class MainAc(object):
    
    def __init__(self):
        self.windowWidthMin = 400
        self.windowHeightMin = 300
        self.windowWidthMax = 600
        self.windowHeightMax = 400
        self.root = Tkinter.Tk()
        self.root.title("Alu测试组工具合集_v1.0")
        self.root.maxsize(self.windowWidthMax, self.windowHeightMax)
        self.root.minsize(self.windowWidthMin, self.windowHeightMin)
        self.root.wm_attributes('-topmost',1) #窗口置顶
        center_window(self.root, self.windowWidthMin, self.windowHeightMin)
        self.btn_start = Tkinter.Button(self.root, command = self.startBtn, text = "Monkey所有设备开始")
    
        self.btn_stop = Tkinter.Button(self.root , text = "Monkey所有设备停止",command=self.stopBtn)
    
        self.btn_pull_anr = Tkinter.Button(self.root, text = "拉取ANR traces.txt（单设备）", command=self.pullTraces)
    
        self.btn_uninstall = Tkinter.Button(self.root, text = "卸载所有设备的Alu", command=self.uninstallApp)
        
        self.btn_install = Tkinter.Button(self.root, text = "为所有设备安装Alu", command=self.installApp)
        
        
        self.box_list()
    
    
    def box_list(self):
        self.box_variable = Tkinter.StringVar(self.root)
        self.box_variable.set("选取安装包") # default value
        self.installAppPaths = file_name(os.getcwd() + "/apk")
        self.box_list= Tkinter.OptionMenu(self.root, self.box_variable, self.installAppPaths)

    # 完成布局
    def gui_arrang(self):
        self.btn_start.pack() #完成start Btn
        self.btn_stop.pack()  #完成stop Btn
        self.btn_pull_anr.pack() #完成pull Btn
        self.btn_uninstall.pack()
        self.box_list.pack()
        self.btn_install.pack()
    
    def startBtn(self):
        os.popen("python launchMonkey_v1.4_crush.py")

    def stopBtn(self):
        os.popen("python killMonkey_v1.1_crush.py")

    def pullTraces(self):
        os.popen("adb pull /data/anr/traces.txt ./ANR_" + nowTime)

    def uninstallApp(self):
        os.popen("python uninstall_app_v1.0_crush.py")
    
    def installApp(self):
        global currentRootPath
        alu_path = self.box_variable.get()
        full_alu_path = currentRootPath + "/" + alu_path
        os.popen("python install_app_v1.0_crush.py %s" % (full_alu_path))



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


