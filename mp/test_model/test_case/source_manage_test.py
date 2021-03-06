#!usr/bin/python
# coding:utf-8

from mp.test_model.models.my_unittest import *
from mp.test_model.page_obj.menulist_page import *
from mp.test_model.page_obj.source_manage_page import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class SourceManageTest(MyTest):
    """mp 登录首页素材管理测试"""

    def test_017_page_text(self):
        """用例编号017：mp登录后，进入素材管理界面"""
        logger.info("开始执行测试用例：mp登录后，进入素材管理界面")
        logger.info("开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("017")
        logger.info("正在点击素材管理按钮...")
        self.assertTrue(MenulistPage(self.driver).click_mp_source_manage_btn())
        logger.info("正在获得截图标题...")
        title = get_image_title("017")

        logger.info("生成截图中...")
        insert_img(self.driver, title)
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_source_manage_title(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_source_manage_title(), expected_value)

    def test_018_add_single_page_text(self):
        """用例编号018：mp登录后，进入素材管理界面,进入新增单图文界面"""
        logger.info("开始执行测试用例：用例编号018：mp登录后，进入素材管理界面,进入新增单图文界面")
        logger.info("开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("018")
        self.assertTrue(SourceManagePage(self.driver).get_new_single_page_text_page())
        logger.info("正在获得截图标题...")
        title = get_image_title("018")
        logger.info("生成截图中...")
        insert_img(self.driver, title)

        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_add_new_single_page_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_add_new_single_page_text(), expected_value)

    def test_019_add_single_page_text(self):
        """用例编号019：mp登录后，进入素材管理界面,进入新增多图文界面"""
        logger.info("开始执行测试用例：用例编号020：mp登录后，进入素材管理界面,进入新增多图文界面")
        logger.info("开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("019")
        self.assertTrue(SourceManagePage(self.driver).get_new_multi_page_text_page())
        logger.info("正在获得截图标题...")
        title = get_image_title("019")
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_add_new_single_page_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_add_new_single_page_text(), expected_value)

    def test_020_turn_to_image_manage_page(self):
        """用例编号020：mp登录后，进入素材管理界面,进入新增图片管理界面"""
        logger.info("开始执行测试用例：用例编号020：mp登录后，进入素材管理界面,进入图片管理界面")
        logger.info("开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("020")
        self.assertTrue(SourceManagePage(self.driver).get_image_manage_page())
        logger.info("正在获得截图标题...")
        title = get_image_title("020")
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_image_size_note_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_image_size_note_text(), expected_value)

    def test_021_turn_to_audio_manage_page(self):
        """用例编号021：mp登录后，进入素材管理界面,进入添加语音管理界面"""
        logger.info("开始执行测试用例：用例编号021：mp登录后，进入素材管理界面,进入图片管理界面")
        logger.info("开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("021")
        self.assertTrue(SourceManagePage(self.driver).get_audio_manage_page())
        logger.info("正在获得截图标题...")
        title = get_image_title("021")
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_audio_add_btn_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_audio_add_btn_text(), expected_value)

    def test_022_turn_to_video_manage_page(self):
        """用例编号022：mp登录后，进入素材管理界面,进入添加视频管理界面"""
        logger.info("开始执行测试用例：用例编号020：mp登录后，进入素材管理界面,进入语音管理界面")
        logger.info("开始登录操作...")
        self.assertTrue(self.user_login_success())
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value("022")
        self.assertTrue(SourceManagePage(self.driver).get_video_manage_page())
        logger.info("正在获得截图标题...")
        title = get_image_title("022")
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_video_add_btn_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_video_add_btn_text(), expected_value)

'''
@author Mavis

'''