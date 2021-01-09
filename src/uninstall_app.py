#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from src.adb_helper import get_device_list

KILL_COMMAND = "adb -s %s uninstall %s"


def launch_uninstall(package_name):
    if not package_name:
        raise RuntimeError("package_name must")
    current_phone_list = get_device_list()
    for item in current_phone_list:
        kill_command = KILL_COMMAND % (item, package_name)
        os.popen(kill_command)


if __name__ == "__main__":
    launch_uninstall("com.google.mm")
