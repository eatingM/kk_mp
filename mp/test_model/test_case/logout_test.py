#!usr/bin/python
# coding:utf-8

from mp.test_model.models.my_unittest import *
from mp.test_model.page_obj.main_page import *
from mp.test_model.page_obj.page_function import *


class LoginOutTest(MyTest):
    """mp 登录成功后退出测试"""

    def login_out(self, casenumber):
        flag = True
        try:
            self.user_normal_login(casenumber)
            MainPage(self.driver).mp_login_out()
            return flag
        except Exception as e:
            logger.error("操作异常！")
            logger.error("系统抛出异常 %s" % str(e))
            flag = False
            return flag

    def test_007_login_out(self):
        """ 用例编号007：mp登录-用户名密码正确，且绑定了公众号,然后退出 """
        logger.info(u"开始执行测试用例：用例编号007：mp登录-用户名密码正确，且绑定了公众号,然后退出")
        logger.info(u"开始登出操作...")
        self.assertTrue(self.login_out("007"))
        expected_value = get_expected_value("007")
        self.assertEqual(LoginPage(self.driver).get_login_button().text, expected_value)
        logger.info(u"测试判断:%s 是否等于:%s" %(LoginPage(self.driver).get_login_button().text, expected_value))
        title = get_image_title(007)
        insert_img(self.driver,title)

if __name__ =="__main__":

    LoginOutTest().login_out()
'''
@author Mavis

'''