import os
import logging

DEVICE_COMMAND = "adb devices"


def get_device_list():
    rt = os.popen(DEVICE_COMMAND).readlines()
    device_list = []
    rt.pop(0)
    rt.pop()
    for item in rt:
        device = item.split()[0]
        device_list.append(device)
    return device_list


logging.basicConfig(level=logging.DEBUG)
model_str = "model:"
command_device_detail = "adb devices -l"
command_device = "adb devices"
split_char = "$"


def execute_command_with_read(command) -> list:
    rt = os.popen(command).readlines()
    logging.debug(type(rt))
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
