#!usr/bin/python
# coding:utf-8

from mp.test_model.models.my_unittest import *
from mp.test_model.page_obj.main_page import *
from mp.test_model.page_obj.custom_menu_page import *
from mp.test_model.page_obj.follow_feedback_page import *
from mp.test_model.page_obj.keyword_feedback_page import *
from mp.test_model.page_obj.unrecognized_feedback_page import *


class MainPageForwardTest(MyTest):
    """mp 登录首页按钮页面跳转检查"""

    def test_012_forward_send_all(self):
        """用例编号012：mp登录后，通过点击蓝凌软件群发功能全新上线跳转到群发消息界面"""
        logger.info(u"开始执行测试用例：用例编号012：mp登录后，通过点击蓝凌软件群发功能全新上线跳转到群发消息界面")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info("点击mp公告按钮...")
        MainPage(self.driver).get_mp_note_btn().click()
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("012")
        logger.info("正在获得截图标题...")
        title = get_image_title("012")
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        logger.info(u"测试判断:%s 是否等于:%s" %(MainPage(self.driver).get_mp_send_all_text(), expected_value))
        self.assertEqual(MainPage(self.driver).get_mp_send_all_text(), expected_value)

    def test_013_forward_customed_menu(self):
        """用例编号013：mp登录后，通过点击自定义菜单跳转到自定义菜单界面"""
        logger.info(u"开始执行测试用例：用例编号013：mp登录后，通过点击自定义菜单跳转到自定义菜单界面")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info("点击mp自定义菜单按钮...")
        MainPage(self.driver).get_custom_menu_btn().click()
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("013")
        logger.info("正在获得截图标题...")
        title = get_image_title("013")
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        logger.info(u"测试判断:%s 是否等于:%s" %(CustomMenu(self.driver).get_mp_custom_menu_manage_text(), expected_value))
        self.assertEqual(CustomMenu(self.driver).get_mp_custom_menu_manage_text(), expected_value)

    def test_014_forward_follow_feedback(self):
        """用例编号014：mp登录后，通过点击关注时回复跳转到关注回复设置界面"""
        logger.info(u"开始执行测试用例：用例编号014：mp登录后，通过点击关注时回复跳转到关注回复设置界面")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info("点击mp自动回复按钮...")
        MainPage(self.driver).get_mp_feedback_btn().click()
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("014")
        logger.info("正在获得截图标题...")
        title = get_image_title("014")
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        logger.info(u"测试判断:%s 是否等于:%s" %(KeywordFeedbackMenu(self.driver).get_mp_keyword_manage_text(), expected_value))
        self.assertEqual(KeywordFeedbackMenu(self.driver).get_mp_keyword_manage_text(), expected_value)

    def test_015_forward_keyword_feedback(self):
        """用例编号015：mp登录后，通过点击关键字回复跳转到关键字回复设置界面"""
        logger.info(u"开始执行测试用例：用例编号015：mp登录后，通过点击关键字回复跳转到关键字回复设置界面")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info("点击mp关键字回复按钮...")
        MainPage(self.driver).get_mp_keyword_feedback_btn().click()
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("015")
        logger.info("正在获得截图标题...")
        title = get_image_title("015")
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        logger.info(u"测试判断:%s 是否等于:%s" %(FollowFeedbackMenu(self.driver).get_mp_feedback_manage_loc_text(), expected_value))
        self.assertEqual(FollowFeedbackMenu(self.driver).get_mp_feedback_manage_loc_text(), expected_value)

    def test_016_forwad_unrecognized_feedback(self):
        """用例编号016：mp登录后，通过点击无法失败回复跳转到无法识别回复设置界面"""
        logger.info(u"用例编号016：mp登录后，通过点击无法失败回复跳转到无法识别回复设置界面")
        logger.info(u"开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info("点击mp无法识别按钮...")
        MainPage(self.driver).get_mp_unrecognized_btn().click()
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("016")
        logger.info("正在获得截图标题...")
        title = get_image_title("016")
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        logger.info(u"测试判断:%s 是否等于:%s" % (UnrecognizedFeedbackMenu(self.driver).get_mp_unrecognized_manage_text(), expected_value))
        self.assertEqual(UnrecognizedFeedbackMenu(self.driver).get_mp_unrecognized_manage_text(), expected_value)


'''
@author Mavis

'''