import os
import time
import device_util


nowTime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))

device_str = ""
option_str = ""
model_str = ""
command_base = "adb%s%s shell monkey -p com.crush.gogo -v -v -v --throttle 200 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --pct-touch 30 --pct-motion 20 --pct-nav 0 --pct-majornav 10 --pct-appswitch 20 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 1 29999 >./log/MonkeyLog_%s_%s 2>&1 &"

process_id = ""
processId_str = ""
command_process_base = "adb%s%s shell ps | grep monkey |grep -v grep | awk '{print $2}'"
kill_command_base = "adb%s%s shell kill "


def launch_start():
    global option_str
    global device_str
    global model_str
    current_phone_list = device_util.get_serial_and_model_list()
    device_size = len(current_phone_list)
    if device_size > 1:
        option_str = " -s "
        for count in range(device_size):
            device_and_model = current_phone_list[count]
            split_index = device_and_model.index("$")
            device_str = device_and_model[0:split_index]
            model_str = device_and_model[split_index:]
            command_monkey = command_base % (option_str, device_str, model_str, nowTime)
            os.popen(command_monkey)
    else:
        option_str = ""
        device_str = ""
        first_ele = current_phone_list[0]
        split_index = first_ele.index("$")
        model_str = first_ele[split_index + 1:]
        command_monkey = command_base % (option_str, device_str, model_str, nowTime)
        os.popen(command_monkey)


def launch_kill():
    global option_str
    global device_str
    global process_id
    current_phone_list = device_util.get_serial_and_model_list()
    device_size = len(current_phone_list)
    if device_size > 1:
        option_str = " -s "
        for item in range(device_size):
            device_str = current_phone_list[item]
            get_process_id_command = command_process_base % (option_str, device_str)
            process_id = os.popen(get_process_id_command)
            process_id_str = process_id.read()
            kill_command = kill_command_base % (option_str, device_str)
            os.popen(kill_command + process_id_str)
    else:
        option_str = ""
        device_str = ""
        get_process_id_command = command_process_base % (option_str, device_str)
        process_id = os.popen(get_process_id_command)
        process_id_str = process_id.read()
        kill_command = kill_command_base % (option_str, device_str)
        os.popen(kill_command + process_id_str)


if __name__ == "__main__":
    launch_kill()
