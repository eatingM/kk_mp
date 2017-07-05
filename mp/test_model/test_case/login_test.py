#!usr/bin/python
# coding:utf-8

from mp.test_model.models.my_unittest import *
from mp.test_model.page_obj.loginPage import *
from mp.test_model.page_obj.page_function import *
from mp.test_model.models.my_logger import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')


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
        logger.info("开始执行测试用例：用例编号001：mp登录-用户名、密码为空")
        logger.info("开始登录mp...")
        self.assertTrue(self.user_normal_login(001))
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value(001)
        logger.info("正在获得截图标题...")
        title = get_image_title(001)

        logger.info("测试判断:%s 是否等于:%s" % (self.get_login_page().get_usr_empty_hint(), expected_value))
        logger.info("生成截图中...")
        insert_img(self.driver, title)

        self.assertEqual(self.get_login_page().get_usr_empty_hint(), expected_value)

    def test_002_login(self):
        """ 用例编号002：mp登录-用户名正确、密码为空 """
        logger.info("开始执行测试用例：用例编号002：mp登录-用户名正确、密码为空")
        logger.info("开始登录mp...")
        self.assertTrue(self.user_normal_login(002))
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value(002)

        logger.info("正在获得截图标题...")
        title = get_image_title(002)
        logger.info("生成截图中...")
        insert_img(self.driver,title)

        logger.info(u"测试判断:%s 是否等于:%s" % (self.get_login_page().get_pwd_empty_hint(), expected_value))
        self.assertEqual(self.get_login_page().get_pwd_empty_hint(), expected_value)

    def test_003_login(self):
        """ 用例编号003：mp登录-用户名正确、未绑定公众号 """
        logger.info(u"开始执行测试用例：用例编号003：mp登录-用户名正确、未绑定公众号")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_normal_login(003))
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value(003)
        actual_value = self.get_login_page().get_unbound_user_hint()
        logger.info("正在获得截图标题...")
        title = get_image_title(003)
        logger.info("生成截图中...")
        insert_img(self.driver,title)
        logger.info(u"测试用例<003>执行后获得的测试实际值为:%s" % actual_value)
        logger.info(u"断言测试用例<003>测试判断:%s 是否等于:%s" % (actual_value, expected_value))

        self.assertEqual(self.get_login_page().get_unbound_user_hint(), expected_value)

    def test_004_login(self):
        """ 用例编号004：mp登录-运营人员不存在 """
        logger.info(u"开始执行测试用例：用例编号004：mp登录-运营人员不存在")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_normal_login(004))

        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value(004)
        logger.info("正在获得截图标题...")
        title = get_image_title(004)
        logger.info("生成截图中...")
        insert_img(self.driver,title)
        logger.info(u"测试判断:%s 是否等于:%s" %(self.get_login_page().get_invalid_usr_hint(), expected_value))
        self.assertEqual(self.get_login_page().get_invalid_usr_hint(), expected_value)

    def test_005_login(self):
        """ 用例编号005：mp登录-用户名或密码错误 """
        logger.info(u"开始执行测试用例：用例编号005：mp登录-用户名或密码错误 ")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_normal_login(005))
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value(005)

        logger.info("正在获得截图标题...")
        title = get_image_title(005)
        logger.info("生成截图中...")
        insert_img(self.driver,title)
        logger.info(u"测试判断:%s 是否等于:%s" %(self.get_login_page().get_pwd_error_hint(), expected_value))
        self.assertEqual(self.get_login_page().get_pwd_error_hint(), expected_value)

    def test_006_login(self):
        """ 用例编号006：mp登录-用户名密码正确，且绑定了公众号 """
        logger.info(u"开始执行测试用例：用例编号006：mp登录-用户名密码正确，且绑定了公众号 ")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_normal_login(006))
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value(006)

        logger.info("正在获得截图标题...")
        title = get_image_title(006)
        logger.info("生成截图中...")
        insert_img(self.driver,title)
        logger.info(u"测试判断:%s 是否等于:%s" %(self.get_login_page().get_login_success_hint(), expected_value))
        self.assertEqual(self.get_login_page().get_login_success_hint(), expected_value)


'''
@author Mavis

'''
