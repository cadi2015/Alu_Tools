import os

optionStr = ""
deviceStr = ""
processId = ""
processIdStr = ""
processBase = "adb%s%s shell ps | grep monkey |grep -v grep | awk '{print $2}'"
killCommandBase = "adb%s%s shell kill "


def launchKill():
    global optionStr
    global deviceStr
    currentPhoneList = getDevicesList()
    devicesSize = len(currentPhoneList)
    if (devicesSize > 1):
        optionStr = " -s "
        for item in range(devicesSize):
            deviceStr = currentPhoneList[item]
            getProcessIdCommand = processBase % (optionStr, deviceStr)
            processId = os.popen(getProcessIdCommand)
            processIdStr = processId.read()
            killCommand = killCommandBase % (optionStr,deviceStr)
            os.popen(killCommand + processIdStr)
    else:
        getProcessIdCommand = processBase % (optionStr,deviceStr)
        processId = os.popen(getProcessIdCommand)
        processIdStr = processId.read()
        killCommand = killCommandBase % (optionStr,deviceStr)
        os.popen(killCommand + processIdStr)




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
    launchKill()
