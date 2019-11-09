#coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '11.4'
desired_caps['deviceName'] = 'iPhone 7 Plus'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = '/Users/wp/Library/Developer/Xcode/DerivedData/Hello_World-bbonmuesaybnyuctshxqzmrqehjy/Build/Products/Debug-iphonesimulator/Hello World.app'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("普通Button").click()



