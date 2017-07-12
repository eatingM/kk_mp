#!usr/bin/python
# coding:utf-8

from mp.test_model.models.my_unittest import *
from mp.test_model.page_obj.menulist_page import *
from mp.test_model.page_obj.source_manage_page import *
import sys
from selenium.webdriver.common.keys import Keys
reload(sys)
sys.setdefaultencoding('utf8')


class AddSinglePageTextTextTest(MyTest):

    """mp 素材管理之单图文中正文编辑测试"""

    def add_single_page_text_text(self, case_number):

        logger.info("开始执行测试用例：用例编号%s：mp登录后，进入素材管理的图文界面，进行单图文添加" % case_number)
        logger.info("开始登录操作...")
        self.assertTrue(self.user_login_success())
        self.assertTrue(SourceManagePage(self.driver).get_new_single_page_text_page())
        self.assertTrue(SourceManagePage(self.driver).get_text_input(case_number))
        (flag, exist_value) = SourceManagePage(self.driver).get_exist_text_input()
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value(case_number)
        logger.info("获得的实际正文值为: %s"% exist_value)
        self.assertTrue(flag)
        logger.info("测试判断:%s 是否等于:%s" % (exist_value, expected_value))
        self.assertEqual(exist_value, expected_value)
        logger.info("正在获得截图标题...")
        title = get_image_title(case_number)
        logger.info("生成截图中...")
        insert_img(self.driver, title)

    def test_070_edit_single_text(self):
        """用例编号070：mp登录后，进入素材管理的图文界面，添加单图文的正文(短文字)"""
        self.add_single_page_text_text("070")

    def test_071_edit_single_text(self):
        """用例编号071：mp登录后，进入素材管理的图文界面，添加单图文的正文(长文字)"""
        self.add_single_page_text_text("071")

    def test_072_edit_single_text(self):
        """用例编号072：mp登录后，进入素材管理的图文界面，添加单图文的正文(短英文)"""
        self.add_single_page_text_text("072")

    def test_073_edit_single_text(self):
        """用例编号073：mp登录后，进入素材管理的图文界面，添加单图文的正文(长英文)"""
        self.add_single_page_text_text("073")

    def test_074_edit_single_text(self):
        """用例编号074：mp登录后，进入素材管理的图文界面，添加单图文的正文(英文短特殊字符)"""
        self.add_single_page_text_text("074")

    def test_075_edit_single_text(self):
        """用例编号075：mp登录后，进入素材管理的图文界面，添加单图文的正文(英文短特殊字符)"""
        self.add_single_page_text_text("075")

    def test_076_edit_single_text(self):
        """用例编号076：mp登录后，进入素材管理的图文界面，添加单图文的正文(英文120特殊字符)"""
        self.add_single_page_text_text("076")

    def test_077_edit_single_text(self):
        """用例编号077：mp登录后，进入素材管理的图文界面，添加单图文的正文(中文120特殊字符)"""
        self.add_single_page_text_text("077")

    def test_078_edit_single_text(self):
        """用例编号078：mp登录后，进入素材管理的图文界面，添加单图文的正文(短数字)"""
        self.add_single_page_text_text("078")

    def test_079_edit_single_text(self):
        """用例编号079：mp登录后，进入素材管理的图文界面，添加单图文的正文(120长数字)"""
        self.add_single_page_text_text("079")

    def test_080_edit_single_text(self):
        """用例编号080：mp登录后，进入素材管理的图文界面，添加单图文的正文(短组合)"""
        self.add_single_page_text_text("080")

    def test_081_edit_single_text(self):
        """用例编号081：mp登录后，进入素材管理的图文界面，添加单图文的正文(120组合)"""
        self.add_single_page_text_text("081")

    def test_082_edit_single_text(self):
        """用例编号082：mp登录后，进入素材管理的图文界面，添加单图文的正文(删除内容输入)"""
        self.add_single_page_text_text("082")
        "to be continued..."


'''
@author Mavis

'''