#!usr/bin/python
# coding:utf-8

import unittest
from mp.test_model.page_obj.loginPage import *
from my_logger import *


class MyTest(unittest.TestCase):

    logger = logging.getLogger("main.my_unittest")

    def setUp(self):
        """
        1、指定启动的浏览器类型
        2、设置隐式等待时间
        3、页面最大化
        :return:
        """

        self.driver = chrome_browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        logger.info("浏览器窗口最大化...")

    def user_login_(self, username, password):
        """
        定义通用登录方法
        :param username:
        :param password:
        :return:
        """
        LoginPage(self.driver).mp_user_login(username, password)

    def user_login_success(self):
        """
        定义登录成方法
        :return:
        """
        try:
            username = get_login_username(006)
            password = get_login_password(006)
            self.user_login_(username, password)
            logger.info(u"正在尝试登录中...")
        except Exception as e:
            logger.error(u"登录失败！")
            logger.error(str(e))

    def user_normal_login(self, casenumber):
        """
        定义传参数的通用登录方法
        :param casenumber:
        :return:
        """
        try:
            username = get_login_username(casenumber)
            password = get_login_password(casenumber)
            self.user_login_(username, password)
            logger.info(u"正在尝试登录中... ")
        except Exception as e:
            logger.error(u"登录失败！")
            logger.error(str(e))

    def tearDown(self):
        """
        每个测试用例执行完成后关闭掉driver
        :return:
        """
        self.driver.quit()


'''
@author Mavis

'''