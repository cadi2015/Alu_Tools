#coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'e8bcd435'
desired_caps['appPackage'] = 'com.cmcm.shorts'
desired_caps['appActivity'] = 'com.cmcm.cmlive.activity.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.quit()

