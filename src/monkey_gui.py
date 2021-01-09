#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
import os
import time
import src.adb_helper

nowTime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)


currentRootPath = ""


def file_name_list(file_path):
    global currentRootPath
    for root, dirs, files in os.walk(file_path):
        """
        root当前目录路径
        dirs当前路径下所有子目录
        files当前路径下所有非目录子文件
        """
        currentRootPath = root
        return files


class MainAc(tkinter.Tk):
    WINDOW_TITLE = "Alu测试组工具合集_v1.0"
    current_workspace_path = os.getcwd()

    def __init__(self):
        self.init_window()
        self.init_views()
        self.complate_views()

    def init_window(self):
        self.windowWidthMin = 500
        self.windowHeightMin = 400
        self.windowWidthMax = 700
        self.windowHeightMax = 500
        self.title(MainAc.WINDOW_TITLE)
        self.maxsize(self.windowWidthMax, self.windowHeightMax)
        self.minsize(self.windowWidthMin, self.windowHeightMin)
        self.wm_attributes('-topmost', 1)
        center_window(self, self.windowWidthMin, self.windowHeightMin)

    def init_views(self):
        self.btn_start = tkinter.Button(self, command=self.startBtn, text="Monkey所有设备开始")
        self.btn_stop = tkinter.Button(self, text="Monkey所有设备停止", command=self.stopBtn)
        self.btn_pull_anr = tkinter.Button(self, text="拉取ANR traces.txt（单设备）", command=self.pullTraces)
        self.btn_uninstall = tkinter.Button(self, text="卸载所有设备的Alu", command=self.uninstallApp)
        self.btn_install = tkinter.Button(self, text="为所有设备安装Alu", command=self.installApp)
        self.box_list()
        self.refresh_btn()
        self.btn_query_devices_init()
        self.label_show_devices_init()

    def box_list(self):
        self.box_variable = tkinter.StringVar(self.root)
        self.box_variable.set("选取安装包")  # default value
        self.installAppPaths = file_name_list(MainAc.current_workspace_path + "/apk")
        self.box_list = tkinter.OptionMenu(self.root, self.box_variable, *(self.installAppPaths),
                                           command=self.box_list_click_lis)
        self.box_list.pack()

    def btn_query_devices_init(self):
        self.btn_query_devices = self.__btn_builder("查询已连接的设备", self.query_devices)

    def label_show_devices_init(self):
        self.lable_devices = tkinter.Label(self.root, text="未知设备情况")

    def __btn_builder(self, btn_name, command_name):
        btn_return = tkinter.Button(self.root, text=btn_name, command=command_name)
        return btn_return

    def refresh_btn(self):
        self.btn_refresh = tkinter.Button(self.root, text="刷新", command=self.refresh_data)

    def query_devices(self):
        devicesArray = src.adb_helper.get_device_list()
        deviceName = ""
        count = len(devicesArray)
        for ele in devicesArray:
            deviceName = deviceName + ele + "\n"
        self.lable_devices.config(text="连接设备数：" + str(count) + "\n" + deviceName)

    # 完成布局
    def complate_views(self):
        self.btn_start.pack()
        self.btn_stop.pack()
        self.btn_pull_anr.pack()
        self.btn_uninstall.pack()
        self.btn_install.pack()
        self.btn_refresh.pack()
        self.btn_query_devices.pack()
        self.lable_devices.pack()

    def startBtn(self):
        os.popen("python launch_monkey.py")

    def stopBtn(self):
        os.popen("python kill_monkey.py")

    def pullTraces(self):
        os.popen("adb pull /data/anr/")

    def uninstallApp(self):
        os.popen("python uninstall_app.py")

    def installApp(self):
        global currentRootPath  # 引入global的重要性
        alu_path = self.box_variable.get()
        full_alu_path = currentRootPath + "/" + alu_path  # currentRootPath在这里如果是局部变量，赋值都还没有
        os.popen("python install_app_v1.0_crush.py %s" % (full_alu_path))

    def box_list_click_lis(self, box_value):
        print(box_value)

    def box_list_new_item_click_lis(self):
        print(self.box_list.get())

    def refresh_data(self):
        self.box_list['menu'].delete(0, 'end')
        new_files = file_name_list(MainAc.current_workspace_path + "/apk")
        for fileName in new_files:
            self.box_list['menu'].add_command(label=fileName, command=self.box_list_new_item_click_lis)


if __name__ == "__main__":
    root = MainAc()
    root.mainloop()
