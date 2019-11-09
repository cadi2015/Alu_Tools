import os
import time
import datetime

nowTime=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
os.popen("adb shell monkey -p com.cmcm.shorts -v -v -v --throttle 150 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --pct-touch 30 --pct-motion 20 --pct-nav 0 --pct-majornav 15 --pct-appswitch 15 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 1 999999 >./MonkeyLog_" + nowTime + " 2>&1 &")







