#!usr/bin/python
# coding:utf-8

from mp.test_model.models.my_unittest import *
from mp.test_model.page_obj.main_page import *
from mp.test_model.page_obj.custom_menu_page import *
from mp.test_model.page_obj.follow_feedback_page import *
from mp.test_model.page_obj.keyword_feedback_page import *
from mp.test_model.page_obj.unrecognized_feedback_page import *
from mp.test_model.page_obj.menulist_page import *


class SourceManageTest(MyTest):
    """mp 登录首页素材管理测试"""

    def test_017_page_text(self):
        """用例编号017：mp登录后，创建单图文素材"""
        logger.info(u"开始执行测试用例：mp登录后，创建单图文素材")
        logger.info(u"开始登录操作...")
        self.user_login_success()
        expected_value = get_expected_value("017")
        MenulistPage(self.driver).click_mp_source_manage_btn()
        title = get_image_title("017")

'''
@author Mavis

'''