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

        (self.driver, flag) = chrome_browser()
        self.assertTrue(flag)
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
        flag = True
        try:
            username = get_login_username(006)
            password = get_login_password(006)
            self.user_login_(username, password)
            logger.info(u"正在尝试登录中...")
            return flag
        except Exception as e:
            logger.error(u"登录操作异常！")
            logger.error(u"系统抛出异常:%s" % str(e))
            flag = False
            return flag

    def user_normal_login(self, casenumber):
        """
        定义传参数的通用登录方法
        :param casenumber:
        :return:
        """
        flag = True
        try:
            username = get_login_username(casenumber)
            password = get_login_password(casenumber)
            self.user_login_(username, password)
            logger.info(u"正在尝试登录中... ")
            return flag
        except Exception as e:
            logger.error(u"登录操作异常！")
            logger.error(u"系统抛出异常:%s" % str(e))
            flag = False
            return flag

    def tearDown(self):
        """
        每个测试用例执行完成后关闭掉driver
        :return:
        """
        try:
            self.driver.quit()
        except Exception as e:
            logger.error(u"浏览器关闭操作异常！！")
            logger.error(u"系统抛出异常:%s" % str(e))

'''
@author Mavis

'''