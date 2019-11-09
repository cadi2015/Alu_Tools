#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

optionStr = ""
deviceStr = ""

killCommandBase = "adb%s%s uninstall com.crush.gogo"


def launchUninstall():
    global optionStr
    global deviceStr
    currentPhoneList = getDevicesList()
    devicesSize = len(currentPhoneList)
    if (devicesSize > 1):
        optionStr = " -s "
        for item in range(devicesSize):
            deviceStr = currentPhoneList[item]
            
            killCommand = killCommandBase % (optionStr,deviceStr)
            os.popen(killCommand)
    else:
        
        killCommand = killCommandBase % (optionStr,deviceStr)
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

