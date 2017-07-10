#!usr/bin/python
# coding:utf-8

from mp.test_model.models.my_unittest import *
from mp.test_model.page_obj.menulist_page import *
from mp.test_model.page_obj.source_manage_page import *
import sys
from selenium.webdriver.common.keys import Keys
reload(sys)
sys.setdefaultencoding('utf8')


class AddSinglePageTextTitleTest(MyTest):

    """mp 素材管理之单图文中图片上传测试"""

    def add_single_page_text_image(self, casenumber):
        logger.info("开始执行测试用例：用例编号%s：mp登录后，进入素材管理的图文界面，进行单图文添加" % casenumber)
        logger.info("开始登录操作...")
        self.assertTrue(self.user_login_success())
        self.assertTrue(SourceManagePage(self.driver).get_new_single_page_text_page())
        self.assertTrue(SourceManagePage(self.driver).get_single_page_text_image_input(casenumber))
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value(casenumber)
        logger.info("正在获得截图标题...")
        title = get_image_title(casenumber)
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        return expected_value

    def test_042_edit_single_title(self):
        """用例编号042：mp登录后，进入素材管理的图文界面，添加单图文的图片(png)"""
        expected_value = self.add_single_page_text_image("042")
        logger.info("测试判断:%s 是否不等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_image_src(), expected_value))
        self.assertNotEqual(SourceManagePage(self.driver).get_mp_single_shown_image_src(), expected_value)

    def test_043_edit_single_title(self):
        """用例编号043：mp登录后，进入素材管理的图文界面，添加单图文的图片(jpeg)"""
        expected_value = self.add_single_page_text_image("043")
        logger.info("测试判断:%s 是否不等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_image_src(), expected_value))
        self.assertNotEqual(SourceManagePage(self.driver).get_mp_single_shown_image_src(), expected_value)

    def test_044_edit_single_title(self):
        """用例编号044：mp登录后，进入素材管理的图文界面，添加单图文的图片(jpeg)"""
        expected_value = self.add_single_page_text_image("044")
        logger.info("测试判断:%s 是否不等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_image_src(), expected_value))
        self.assertNotEqual(SourceManagePage(self.driver).get_mp_single_shown_image_src(), expected_value)

    def test_045_edit_single_title(self):
        """用例编号045：mp登录后，进入素材管理的图文界面，添加单图文的图片(jpg)"""
        expected_value = self.add_single_page_text_image("045")
        logger.info("测试判断:%s 是否不等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_image_src(), expected_value))
        self.assertNotEqual(SourceManagePage(self.driver).get_mp_single_shown_image_src(), expected_value)

    def test_046_edit_single_title(self):
        """用例编号046：mp登录后，进入素材管理的图文界面，添加单图文的图片(log)"""
        expected_value = self.add_single_page_text_image("046")
        error_hint = SourceManagePage(self.driver).get_mp_single_image_error_hint()
        logger.info("测试判断:%s 是否等于:%s" % (error_hint, expected_value))
        self.assertEqual(error_hint, expected_value)

    def test_047_edit_single_title(self):
        """用例编号047：mp登录后，进入素材管理的图文界面，添加单图文的图片(大图片文件)"""
        expected_value = self.add_single_page_text_image("047")
        error_hint = SourceManagePage(self.driver).get_mp_single_image_size_error_hint()
        logger.info("测试判断:%s 是否等于:%s" % (error_hint, expected_value))
        self.assertEqual(error_hint, expected_value)

    def test_048_edit_single_title(self):
        """用例编号048：mp登录后，进入素材管理的图文界面，添加单图文的图片(0kb jpg)"""
        expected_value = self.add_single_page_text_image("048")
        logger.info("测试判断:%s 是否不等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_image_src(), expected_value))
        self.assertNotEqual(SourceManagePage(self.driver).get_mp_single_shown_image_src(), expected_value)

'''
@author Mavis

'''