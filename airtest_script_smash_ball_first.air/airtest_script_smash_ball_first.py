# -*- encoding=utf8 -*-
__author__ = "wp"

from airtest.core.api import *

for item in range(5):
    if exists(Template(r"tpl1545648737895.png", record_pos=(0.022, 0.487), resolution=(1440, 2880))):
        touch(Template(r"tpl1545648746413.png", record_pos=(0.019, 0.486), resolution=(1440, 2880)))
    
    sleep(5)

    if exists(Template(r"tpl1545648484572.png", record_pos=(0.208, 0.299), resolution=(1440, 2880))) :
        touch(Template(r"tpl1545648495989.png", record_pos=(0.21, 0.29), resolution=(1440, 2880)))
        sleep(5)

    if exists(Template(r"tpl1545649918759.png", record_pos=(0.001, 0.454), resolution=(1440, 2880))):
        touch(Template(r"tpl1545649987974.png", record_pos=(0.004, 0.448), resolution=(1440, 2880)))

        sleep(5)

        
    touch(Template(r"tpl1545647218462.png", record_pos=(-0.397, 0.567), resolution=(1440, 2880)))

    sleep(20)
    swipe(Template(r"tpl1545647892674.png", record_pos=(0.172, 0.522), resolution=(1440, 2880)), vector=[0.0838, -0.0451])

    sleep(20)

    swipe(Template(r"tpl1545648012805.png", record_pos=(-0.21, 0.378), resolution=(1440, 2880)), vector=[-0.1415, -0.0714])


    sleep(20)

    swipe(Template(r"tpl1545649178010.png", record_pos=(-0.037, 0.282), resolution=(1440, 2880)), vector=[0.1441, 0.0463])
    
    sleep(20)
    
    
    if exists(Template(r"tpl1545649356131.png", record_pos=(0.395, 0.66), resolution=(1440, 2880))):
        swipe(Template(r"tpl1545649356131.png", record_pos=(0.395, 0.66), resolution=(1440, 2880)), vector=[0.0837, 0.0085])
        sleep(20)

