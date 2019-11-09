import os

import time
import datetime

nowTime=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))

os.popen("adb logcat | grep com.cmcm.shorts > ./MonkeyWithLogcat_" + nowTime)




