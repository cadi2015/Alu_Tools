import os

proceessId = os.popen("adb shell ps | grep monkey |grep -v grep | awk '{print $2}'")

killCommand = "adb shell kill " + proceessId.read()

os.popen(killCommand)

print 'success'




