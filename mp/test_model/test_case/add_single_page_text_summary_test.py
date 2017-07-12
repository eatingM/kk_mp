#!usr/bin/python
# coding:utf-8

from mp.test_model.models.my_unittest import *
from mp.test_model.page_obj.menulist_page import *
from mp.test_model.page_obj.source_manage_page import *
import sys
from selenium.webdriver.common.keys import Keys
reload(sys)
sys.setdefaultencoding('utf8')


class AddSinglePageTextSummaryTest(MyTest):

    """mp 素材管理之单图文中摘要测试"""

    def add_single_page_text_image(self, casenumber):
        logger.info("开始执行测试用例：用例编号%s：mp登录后，进入素材管理的图文界面，进行单图文添加" % casenumber)
        logger.info("开始登录操作...")
        self.assertTrue(self.user_login_success())
        self.assertTrue(SourceManagePage(self.driver).get_new_single_page_text_page())
        self.assertTrue(SourceManagePage(self.driver).get_summary_input(casenumber))
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value(casenumber)
        logger.info("正在获得截图标题...")
        title = get_image_title(casenumber)
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        return expected_value

    def test_049_edit_single_title(self):
        """用例编号049：mp登录后，进入素材管理的图文界面，添加单图文的摘要(短文字)"""
        expected_value = self.add_single_page_text_image("049")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_050_edit_single_title(self):
        """用例编号050：mp登录后，进入素材管理的图文界面，添加单图文的摘要(120个文字)"""
        expected_value = self.add_single_page_text_image("050")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_051_edit_single_title(self):
        """用例编号051：mp登录后，进入素材管理的图文界面，添加单图文的摘要(125个文字)"""
        expected_value = self.add_single_page_text_image("051")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_052_edit_single_title(self):
        """用例编号052：mp登录后，进入素材管理的图文界面，添加单图文的摘要(短英文)"""
        expected_value = self.add_single_page_text_image("052")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_053_edit_single_title(self):
        """用例编号053：mp登录后，进入素材管理的图文界面，添加单图文的摘要(120英文)"""
        expected_value = self.add_single_page_text_image("053")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_054_edit_single_title(self):
        """用例编号054：mp登录后，进入素材管理的图文界面，添加单图文的摘要(125英文)"""
        expected_value = self.add_single_page_text_image("054")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_055_edit_single_title(self):
        """用例编号055：mp登录后，进入素材管理的图文界面，添加单图文的摘要(英文短特殊字符)"""
        expected_value = self.add_single_page_text_image("055")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_056_edit_single_title(self):
        """用例编号056：mp登录后，进入素材管理的图文界面，添加单图文的摘要(中文短特殊字符)"""
        expected_value = self.add_single_page_text_image("056")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_057_edit_single_title(self):
        """用例编号057：mp登录后，进入素材管理的图文界面，添加单图文的摘要(英文120特殊字符)"""
        expected_value = self.add_single_page_text_image("057")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_059_edit_single_title(self):
        """用例编号059：mp登录后，进入素材管理的图文界面，添加单图文的摘要(中文120特殊字符)"""
        expected_value = self.add_single_page_text_image("059")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_060_edit_single_title(self):
        """用例编号060：mp登录后，进入素材管理的图文界面，添加单图文的摘要(短数字)"""
        expected_value = self.add_single_page_text_image("060")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_061_edit_single_title(self):
        """用例编号061：mp登录后，进入素材管理的图文界面，添加单图文的摘要(120长数字)"""
        expected_value = self.add_single_page_text_image("061")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_062_edit_single_title(self):
        """用例编号062：mp登录后，进入素材管理的图文界面，添加单图文的摘要(125长数字)"""
        expected_value = self.add_single_page_text_image("062")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_063_edit_single_title(self):
        """用例编号063：mp登录后，进入素材管理的图文界面，添加单图文的摘要(短组合输入)"""
        expected_value = self.add_single_page_text_image("063")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_064_edit_single_title(self):
        """用例编号064：mp登录后，进入素材管理的图文界面，添加单图文的摘要(120组合输入)"""
        expected_value = self.add_single_page_text_image("064")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_065_edit_single_title(self):
        """用例编号065：mp登录后，进入素材管理的图文界面，添加单图文的摘要(125组合输入)"""
        expected_value = self.add_single_page_text_image("065")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_066_edit_single_title(self):
        """用例编号066：mp登录后，进入素材管理的图文界面，添加单图文的摘要(摘要输入)"""
        expected_value = self.add_single_page_text_image("066")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_067_edit_single_title(self):
        """用例编号067：mp登录后，进入素材管理的图文界面，添加单图文的标题(删除摘要内容)"""
        expected_value = self.add_single_page_text_image("067")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        logger.info("输入后，回删输入的内容")
        SourceManagePage(self.driver).get_mp_single_summary_input().send_keys(Keys.BACKSPACE)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_068_edit_single_title(self):
        """用例编号068：mp登录后，进入素材管理的图文界面，添加单图文的标题(删空摘要内容)"""
        expected_value = self.add_single_page_text_image("068")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        logger.info("输入后，回删输入的内容")
        SourceManagePage(self.driver).get_mp_single_summary_input().send_keys(Keys.BACKSPACE)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

    def test_069_edit_single_title(self):
        """用例编号069：mp登录后，进入素材管理的图文界面，添加单图文的标题(更新摘要内容)"""
        expected_value = self.add_single_page_text_image("069")
        logger.info("获得的测试用例期望值为： %s" % expected_value)
        logger.info("输入后，回删输入的内容")
        SourceManagePage(self.driver).get_mp_single_summary_input().send_keys(Keys.BACKSPACE)
        input_value = get_input_value("069")
        SourceManagePage(self.driver).get_mp_single_summary_input().send_keys(input_value)
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info(("获得的测试用例实际值为： %s" % actual_value))
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)

'''
@author Mavis

'''