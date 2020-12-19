import os
import time

nowTime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))

deviceStr = ""
optionStr = ""
commandBase = "adb%s%s shell monkey -p com.crush.gogo -v -v -v --throttle 200 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --pct-touch 30 --pct-motion 20 --pct-nav 0 --pct-majornav 10 --pct-appswitch 20 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 1 29999 >./MonkeyLog_%s_%s 2>&1 &"


def launchMonkey():
    global optionStr
    global deviceStr
    currentPhoneList = getDevicesList()
    devicesSize = len(currentPhoneList)
    if (devicesSize > 1):
        optionStr = " -s "
        for count in range(devicesSize):
            deviceAndModel = currentPhoneList[count]
            splitIndex = deviceAndModel.index("$")
            deviceStr = deviceAndModel[0:splitIndex]
            modelStr = deviceAndModel[splitIndex:]
            commandMonkey = commandBase % (optionStr, deviceStr, deviceStr + modelStr, nowTime)
            os.popen(commandMonkey)
    else:
        commandMonkey = commandBase % (optionStr, deviceStr, deviceStr, nowTime)
        os.popen(commandMonkey)


def getDevicesList():
    rt = os.popen("adb devices -l").readlines()
    devicesList = []
    rt.pop(0)
    rt.pop()
    for item in rt:
        itemList = item.split()
        deviceAndModel = itemList[0]
        for everyStr in itemList:
            if ("model" in everyStr):
                deviceAndModel = deviceAndModel + "$" + everyStr
        devicesList.append(deviceAndModel)
    return devicesList


if __name__ == "__main__":
    launchMonkey()
