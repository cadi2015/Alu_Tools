#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import utils.device_util

optionStr = ""
deviceStr = ""

command_uninstall = "adb%s%s uninstall com.crush.gogo"


def launch_uninstall():
    global optionStr
    global deviceStr
    current_phone_list = utils.device_util.get_serial_list()
    devices_size = len(current_phone_list)
    if devices_size > 1:
        optionStr = " -s "
        for item in range(devices_size):
            deviceStr = current_phone_list[item]

            execute_command = command_uninstall % (optionStr, deviceStr)
            os.popen(execute_command)
    else:

        execute_command = command_uninstall % (optionStr, deviceStr)
        os.popen(execute_command)


if __name__ == "__main__":
    launch_uninstall()

