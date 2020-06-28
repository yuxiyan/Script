# coding=utf-8

from appium import webdriver
import time
import unittest
from AppiumServer import AppiumServer

import os
#import HTMLTestRunner


class LoginTestLizi(unittest.TestCase):

    @classmethod
    # 所有test运行前运行一次
    def setUpClass(self):  # class级别，全局
        self.appiumServer=AppiumServer.start_server()


    @classmethod
    # 所有test运行完后运行一次
    def tearDownClass(cls):
        print('所有用例执行完毕')



    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '8.0.0'  # 设备系统版本
        desired_caps['deviceName'] = '2a38154b'  # 设备名称
        desired_caps['appPackage'] = 'com.xueqiu.android'  # 测试app包名
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'  # 测试appActivity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app

    def test_login(self):
        driver = self.driver
        # 进入首页后点击‘我的’按钮
        driver.find_element_by_xpath("//android.widget.TextView[@text='行情']").click()
        time.sleep(2)



        # 添加断言，若昵称不正确，则打印错误信息
        try:
            assert 'No_matter' in name
            print  (loginUser is right)
        except AssertionError as e:
            print (loginUser is Error)



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
