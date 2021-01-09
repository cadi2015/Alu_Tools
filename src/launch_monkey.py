import os
import time

import src.adb_helper

deviceStr = ""
COMMAND_BASE = "adb -s %s shell monkey -p com.crush.gogo -v -v -v --throttle 200 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --pct-touch 30 --pct-motion 20 --pct-nav 0 --pct-majornav 10 --pct-appswitch 20 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 1 29999 >./MonkeyLog_%s_%s 2>&1 &"


def launch_monkey():
    global deviceStr
    current_phone_list = src.adb_helper.get_device_list()

    for device_sn in current_phone_list:
        now_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        command_monkey = COMMAND_BASE % (device_sn, device_sn, now_time)
        os.popen(command_monkey)


if __name__ == "__main__":
    launch_monkey()
