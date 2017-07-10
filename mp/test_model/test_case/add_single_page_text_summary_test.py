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
        actual_value = SourceManagePage(self.driver).get_single_shown_summary_text()
        logger.info("测试判断:%s 是否等于:%s" % (actual_value, expected_value))
        self.assertEqual(actual_value, expected_value)
'''
@author Mavis

'''