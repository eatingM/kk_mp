#!usr/bin/python
# coding:utf-8

from mp.test_model.page_obj.base_page import *
from page_function import *
from mp.test_model.models.my_logger import *


class LoginPage(Page):

    """
    用户登录界面
    """
    url = "/login.jsp"

    """
    Element loc
    登录界面的所有元素的定位信息

    """
    logger = logging.getLogger("main.loginpage")


    # Action

    def input_login_username(self, username):
        """
        向登录的用户名输入框输入内容
        :param username:
        :return:
        """
        # input login_name

        login_input = self.find_element(self.get_element_loc("mp_login_usr_loc"))
        logger.info(u"向登录的用户名输入框输入：%s" % username)
        login_input.send_keys(username)

    def input_login_password(self, password):
        """
        向登录的密码输入框输入密码
        :param password:
        :return:
        """
        # input password
        self.find_element(self.get_element_loc("mp_login_usr_paw_loc")).send_keys(password)
        logger.info(u"向登录的密码输入框输入 %s" % password)

    def click_login_button(self):
        """
        点击登录界面的登录按钮
        :return:
        """
        self.find_element(self.get_element_loc("mp_login_btn_loc")).click()

    def get_login_button(self):
        """
        返回用户登录按钮元素
        :return:
        """
        result = self.find_element(self.get_element_loc("mp_login_btn_loc"))
        return result

    def get_usr_error_hint(self):
        """
        返回用户名错误提示内容
        :return:
        """
        result = self.find_element(self.get_element_loc("mp_usr_error_hint_loc")).text
        return result

    def get_pwd_error_hint(self):
        """
        返回登录密码错误提示内容
        :return:
        """
        return self.find_element(self.get_element_loc("mp_pwd_error_hint_loc")).text

    def get_usr_empty_hint(self):
        """
        返回登录用户名为空的提示内容
        :return:
        """

        return self.find_element(self.get_element_loc("mp_usr_empty_hint_loc")).text

    def get_pwd_empty_hint(self):
        """
        返回登录密码为空的提示内容
        :return:
        """
        return self.find_element(self.get_element_loc("mp_pwd_empty_hint_loc")).text

    def get_unbound_user_hint(self):
        """
        返回用户未绑定公众号的提示内容
        :return:
        """
        return self.find_element(self.get_element_loc("mp_unbound_user_hint_loc")).text

    def get_invalid_usr_hint(self):
        """
        返回当前用户无效的提示内容
        :return:
        """
        return self.find_element(self.get_element_loc("mp_invalid_usr_hint_loc")).text

    def get_login_success_hint(self):
        """
        返回登录成功的提示内容
        :return:
        """
        return self.find_element(self.get_element_loc("mp_login_success_hint_loc")).text

    def mp_user_login(self, username, password):
        """
        构造一个方法，完成：
        1、打开浏览器
        2、输入用户名
        3、输入密码
        4、点击登录按钮

        :param username:
        :param password:
        :return:
        """

        self.open(self.url)
        logger.info(u"打开浏览器: %s"% self.url)
        self.input_login_username(username)
        logger.info(u"输入用户名: %s" % username)
        self.input_login_password(password)
        logger.info(u"输入密码: %s"% password)
        self.click_login_button()
        logger.info(u"点击登录按钮...")


if __name__ == "__main__":

    dr = chrome_browser()
    a=LoginPage(dr)
    a.mp_user_login("0609a4" , "1")




'''
@author Mavis

'''