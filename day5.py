# encoding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',          # 需替换成你的driverName
    'platformVersion': '7.1.2',
    'appPackage': 'com.ss.android.ugc.aweme',
    'appActivity': 'com.ss.android.ugc.aweme.main.MainActivity'
}
driver = webdriver.Remote(server, desired_capabilities)
time.sleep(15)
while True:
    time.sleep(15)
    driver.swipe(462,1140,462,403,200)











