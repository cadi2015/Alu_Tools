#!/usr/bin/python
#-*-coding:utf-8-*-
#读取文件、写入文件
#过滤日志
#对Monkey Log的处理写到一个类里好了



class MonkeyLogFilter:
    CRASH_KEY = "// CRASH"
    ANR_KEY = "ANR in"
    
    def __init__(self):
        '''构造方法
            注释多行'''
        self.crashCount = 0
        self.startCollectCrashLog = False #开始收集的标志位
        self.CrashStringsfilted = []

    
    def readLog(self, fileUri):
        with open(sourceFile,'r') as fileData:
            for everyLine in fileData:
                 actionWithCrash(everyLine)

    def actionWithCrash(self, contentLine):
        if contentLine.startsWith(MonkeyLogFilter.CRASH_KEY):
            self.crashCount += 1
            self.startCollectCrashLog = True
        
        if self.startCollectCrashLog and contentLine.startsWith("//"):
            print contentLine,
        else:
            self.startCollectCrashLog = False


    def writeCrashLogForFile(self, targetFile):

    def getCrashCount(self):
        return self.crashCount



