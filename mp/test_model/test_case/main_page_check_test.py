#!usr/bin/python
# coding:utf-8

from mp.test_model.models.my_unittest import *
from mp.test_model.page_obj.main_page import *
from mp.test_model.page_obj.page_function import *


class MainPageCheckTest(MyTest):
    """mp 登录首页页面元素数据检查"""

    def test_008_loc(self):
        """用例编号008：mp登录-用户名密码正确，且绑定了公众号，登录后检查首页位置"""
        logger.info(u"开始执行测试用例：用例编号008：mp登录-用户名密码正确，且绑定了公众号，登录后检查首页位置")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("008")

        logger.info("正在获得截图标题...")
        title = get_image_title("008")
        logger.info("生成截图中...")
        insert_img(self.driver,title)
        logger.info(u"测试判断:%s 是否等于:%s" %(MainPage(self.driver).get_mp_main_page_loc_text(),expected_value))
        self.assertEqual(MainPage(self.driver).get_mp_main_page_loc_text(),expected_value)

    def test_009_service_name(self):
        """用例编号009：mp登录-用户名密码正确，且绑定了公众号，登录后检查公众号名称"""
        logger.info(u"开始执行测试用例：用例编号009：mp登录-用户名密码正确，且绑定了公众号，登录后检查公众号名称")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("009")

        logger.info("正在获得截图标题...")
        title = get_image_title("009")
        logger.info("生成截图中...")
        insert_img(self.driver,title)
        logger.info(u"测试判断:%s 是否等于:%s" %(MainPage(self.driver).get_mp_service_name_text(),expected_value))
        self.assertEqual(MainPage(self.driver).get_mp_service_name_text(),expected_value)

    def test_010_service_id(self):
        """用例编号010：mp登录-用户名密码正确，且绑定了公众号，登录后检查公众号id"""
        logger.info(u"开始执行测试用例：用例编号010：mp登录-用户名密码正确，且绑定了公众号，登录后检查公众号id")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("010")

        logger.info("正在获得截图标题...")
        title = get_image_title("010")
        logger.info("生成截图中...")
        insert_img(self.driver,title)
        logger.info(u"测试判断:%s 是否等于:%s" %(MainPage(self.driver).get_mp_service_id_text(),expected_value))
        self.assertEqual(MainPage(self.driver).get_mp_service_id_text(),expected_value)

    def test_011_note(self):
        """用例编号011：mp登录-用户名密码正确，且绑定了公众号，登录后检查公众号公告内容"""
        logger.info(u"开始执行测试用例：用例编号011：mp登录-用户名密码正确，且绑定了公众号，登录后检查公众号公告内容")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("011")

        logger.info("正在获得截图标题...")
        title = get_image_title("011")
        logger.info("生成截图中...")
        insert_img(self.driver,title)
        logger.info(u"测试判断:%s 是否等于:%s" % (MainPage(self.driver).get_mp_note_text(),expected_value))
        self.assertEqual(MainPage(self.driver).get_mp_note_text(),expected_value)





'''
@author Mavis

'''