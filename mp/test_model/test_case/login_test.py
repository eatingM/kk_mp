#!usr/bin/python
# coding:utf-8

from mp.test_model.models.my_unittest import *
from mp.test_model.page_obj.loginPage import *
from mp.test_model.page_obj.page_function import *
from mp.test_model.models.my_logger import *


class LoginTest(MyTest):
    """ mp 登录用户名和密码测试 """

    def get_login_page(self):
        """
        返回LoginPage实例对象
        :return:
        """
        return LoginPage(self.driver)

    def test_001_login(self):
        """ 用例编号001：mp登录-用户名、密码为空 """
        logger.info(u"开始执行测试用例：用例编号001：mp登录-用户名、密码为空")
        logger.info(u"开始登录操作...")
        self.user_normal_login(001)
        expected_value = get_expected_value(001)
        title = get_image_title(001)
        self.assertEqual(self.get_login_page().get_usr_empty_hint(), expected_value)
        logger.info(u"测试判断:%s 是否等于:%s" % (self.get_login_page().get_usr_empty_hint(), expected_value))
        insert_img(self.driver, title)

    def test_002_login(self):
        """ 用例编号002：mp登录-用户名正确、密码为空 """
        logger.info(u"开始执行测试用例：用例编号002：mp登录-用户名正确、密码为空")
        logger.info(u"开始登录操作...")
        self.user_normal_login(002)
        expected_value = get_expected_value(002)
        self.assertEqual(self.get_login_page().get_pwd_empty_hint(), expected_value)
        logger.info(u"测试判断:%s 是否等于:%s" % (self.get_login_page().get_pwd_empty_hint(), expected_value))
        title = get_image_title(002)
        insert_img(self.driver,title)

    def test_003_login(self):
        """ 用例编号003：mp登录-用户名正确、未绑定公众号 """
        logger.info(u"开始执行测试用例：用例编号003：mp登录-用户名正确、未绑定公众号")
        logger.info(u"开始登录操作...")
        self.user_normal_login(003)
        expected_value = get_expected_value(003)
        self.assertEqual(self.get_login_page().get_unbound_user_hint(), expected_value)
        logger.info(u"测试判断:%s 是否等于:%s" %(self.get_login_page().get_unbound_user_hint(), expected_value))
        title = get_image_title(003)
        insert_img(self.driver,title)

    def test_004_login(self):
        """ 用例编号004：mp登录-运营人员不存在 """
        logger.info(u"开始执行测试用例：用例编号004：mp登录-运营人员不存在")
        logger.info(u"开始登录操作...")
        self.user_normal_login(004)
        expected_value = get_expected_value(004)
        self.assertEqual(self.get_login_page().get_invalid_usr_hint(), expected_value)
        logger.info(u"测试判断:%s 是否等于:%s" %(self.get_login_page().get_invalid_usr_hint(), expected_value))
        title = get_image_title(004)
        insert_img(self.driver,title)

    def test_005_login(self):
        """ 用例编号005：mp登录-用户名或密码错误 """
        logger.info(u"开始执行测试用例：用例编号005：mp登录-用户名或密码错误 ")
        logger.info(u"开始登录操作...")
        self.user_normal_login(005)
        expected_value = get_expected_value(005)
        self.assertEqual(self.get_login_page().get_pwd_error_hint(), expected_value)
        logger.info(u"测试判断:%s 是否等于:%s" %(self.get_login_page().get_pwd_error_hint(), expected_value))
        title = get_image_title(005)
        insert_img(self.driver,title)

    def test_006_login(self):
        """ 用例编号006：mp登录-用户名密码正确，且绑定了公众号 """
        logger.info(u"开始执行测试用例：用例编号006：mp登录-用户名密码正确，且绑定了公众号 ")
        logger.info(u"开始登录操作...")
        self.user_normal_login(006)
        expected_value = get_expected_value(006)
        self.assertEqual(self.get_login_page().get_login_success_hint(), expected_value)
        logger.info(u"测试判断:%s 是否等于:%s" %(self.get_login_page().get_login_success_hint(), expected_value))
        title = get_image_title(006)
        insert_img(self.driver,title)

'''
@author Mavis

'''
