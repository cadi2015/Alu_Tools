import os
import time
import datetime

nowTime=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))




text = os.popen("adb shell monkey -p com.cmcm.shorts -v -v -v --throttle 200 --ignore-crashes --ignore-timeouts --pct-touch 30 --pct-motion 20 --pct-nav 20 --pct-majornav 15 --pct-appswitch 5 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 0 --bugreport 999999 >./MonkeyLog_" + nowTime)


os.popen("adb pull /data/anr/traces.txt ./ANR_" + nowTime)



