import os
import time
import datetime

nowTime=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))

deviceStr = ""
optionStr = ""
commandBase = "adb%s%s shell monkey -p com.cmcm.shorts -v -v -v --throttle 150 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --pct-touch 30 --pct-motion 20 --pct-nav 0 --pct-majornav 15 --pct-appswitch 15 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 1 999999 >./MonkeyLog_%s_%s 2>&1 &"

def launchMonkey():
    global optionStr
    global deviceStr
    currentPhoneList = getDevicesList()
    devicesSize = len(currentPhoneList)
    if(devicesSize > 1):
        optionStr = " -s "
        for count in range(devicesSize):
            deviceStr = currentPhoneList[count]
            commandMonkey = commandBase % (optionStr, deviceStr,deviceStr, nowTime)
            os.popen(commandMonkey)
    else:
        commandMonkey = commandBase % (optionStr, deviceStr,deviceStr, nowTime)
        os.popen(commandMonkey)




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
    launchMonkey()
