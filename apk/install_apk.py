#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import utils.device_util

alu_path = sys.argv[1]

print alu_path

optionStr = ""
deviceStr = ""

command_install = "adb%s%s install %s"


def launch_install():
    global optionStr
    global deviceStr
    current_serial_nums = utils.device_util.get_serial_list()
    device_size = len(current_serial_nums)
    if device_size > 1:
        optionStr = " -s "
        for item in range(device_size):
            deviceStr = current_serial_nums[item]
            command_execute = command_install % (optionStr, deviceStr, alu_path)
            os.popen(command_execute)
    else:
        command_execute = command_install % (optionStr, deviceStr, alu_path)
        os.popen(command_execute)


if __name__ == "__main__":
    launch_install()

