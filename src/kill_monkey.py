#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import src.adb_helper

processBase = "adb -s %s shell ps | grep monkey |grep -v grep | awk '{print $2}'"
killCommandBase = "adb -s %s shell kill "


def launch_kill():
    current_phone_list = src.adb_helper.get_device_list()
    for item in current_phone_list:
        get_pid_command = processBase % item
        process_id = os.popen(get_pid_command)
        process_id_str = process_id.read()
        kill_command = killCommandBase % item
        os.popen(kill_command + process_id_str)


if __name__ == "__main__":
    launch_kill()
