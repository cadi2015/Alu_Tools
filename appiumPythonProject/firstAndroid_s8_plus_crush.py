#coding=utf-8
from appium import webdriver
import time
import homeCase

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0'
desired_caps['deviceName'] = '98895a364d4f47334c'
desired_caps['appPackage'] = 'com.crush.gogo'
desired_caps['appActivity'] = 'com.crush.gogo.login.activity.SplashActivity'
desired_caps['noReset'] = 'true'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

