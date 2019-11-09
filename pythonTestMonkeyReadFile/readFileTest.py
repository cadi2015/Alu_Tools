#!/usr/bin/python
#-*-coding:utf-8-*-

import os

crash_info = "// CRASH"
anr_info = "ANR in"

with open("./MonkeyLogBase.txt") as file:
    for everyLine in file:
        #print everyLine,  #很明显，每一行有一个换行字符，不让print打印即可
        if everyLine.startswith(crash_info):
            print everyLine,


class Monkey():
