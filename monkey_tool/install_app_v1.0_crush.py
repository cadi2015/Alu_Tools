#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

alu_path = sys.argv[1]

optionStr = ""
deviceStr = ""

killCommandBase = "adb%s%s install %s"


def launchUninstall():
    global optionStr
    global deviceStr
    currentPhoneList = getDevicesList()
    devicesSize = len(currentPhoneList)
    if (devicesSize > 1):
        optionStr = " -s "
        for item in range(devicesSize):
            deviceStr = currentPhoneList[item]
            
            killCommand = killCommandBase % (optionStr,deviceStr,alu_path)
            os.popen(killCommand)
    else:
        
        killCommand = killCommandBase % (optionStr,deviceStr,alu_path)
        os.popen(killCommand)




def getDevicesList():
    rt = os.popen("adb devices").readlines()
    devicesList = []
    rt.pop(0)
    rt.pop()
    for item in rt:
        device = item.split()[0]
        devicesList.append(device)
    return devicesList


if __name__ == "__main__":
    launchUninstall()

