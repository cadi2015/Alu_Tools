# -*- coding:utf-8 -*-

import os

model_str = "model:"
command_device_detail = "adb devices -l"
command_device = "adb devices"
split_char = "$"


def execute_command_with_read(command):
    rt = os.popen(command).readlines()
    return rt


def get_serial_and_model_list():
    rt = execute_command_with_read(command_device_detail)
    devices_list = []
    rt.pop(0)
    rt.pop()
    for item in rt:
        item_list = item.split()
        device_and_model = item_list[0]
        for every_str in item_list:
            if model_str in every_str:
                every_str = every_str[len(model_str):len(every_str)]
                device_and_model = device_and_model + split_char + every_str
                devices_list.append(device_and_model)

    return devices_list


def get_serial_list():
    rt = execute_command_with_read(command_device)
    devices_list = []
    rt.pop(0)
    rt.pop()

    for item in rt:
        item_list = item.split()
        devices_list.append(item_list[0])
    return devices_list


if __name__ == "__main__":
    print get_serial_and_model_list()
