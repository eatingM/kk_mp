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

    """mp 素材管理之单图文中编辑标题测试"""

    def add_single_page_text_title(self, casenumber):
        logger.info("开始执行测试用例：用例编号%s：mp登录后，进入素材管理的图文界面，进行单图文添加" % casenumber)
        logger.info("开始登录操作...")
        self.assertTrue(self.user_login_success())
        self.assertTrue(SourceManagePage(self.driver).get_new_single_page_text_page())
        self.assertTrue(SourceManagePage(self.driver).get_single_page_text_title_input(casenumber))
        logger.info(" 正在获得用例期望值...")
        expected_value = get_expected_value(casenumber)
        logger.info("正在获得截图标题...")
        title = get_image_title(casenumber)
        logger.info("生成截图中...")
        insert_img(self.driver, title)
        return expected_value

    def test_023_edit_single_title(self):
        """用例编号023：mp登录后，进入素材管理的图文界面，添加单图文的标题(短中文输入)"""
        expected_value = self.add_single_page_text_title("023")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_024_edit_single_title(self):
        """用例编号024：mp登录后，进入素材管理的图文界面，添加单图文的标题(64个字长中文输入)"""
        expected_value = self.add_single_page_text_title("024")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_025_edit_single_title(self):
        """用例编号025：mp登录后，进入素材管理的图文界面，添加单图文的标题(66个字长中文输入)"""
        expected_value = self.add_single_page_text_title("025")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_026_edit_single_title(self):
        """用例编号026：mp登录后，进入素材管理的图文界面，添加单图文的标题(短英文输入)"""
        expected_value = self.add_single_page_text_title("026")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_027_edit_single_title(self):
        """用例编号027：mp登录后，进入素材管理的图文界面，添加单图文的标题(64个长英文输入)"""
        expected_value = self.add_single_page_text_title("027")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_028_edit_single_title(self):
        """用例编号028：mp登录后，进入素材管理的图文界面，添加单图文的标题(66个长英文输入)"""
        expected_value = self.add_single_page_text_title("028")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_029_edit_single_title(self):
        """用例编号029：mp登录后，进入素材管理的图文界面，添加单图文的标题(短特殊字符输入)"""
        expected_value = self.add_single_page_text_title("029")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_030_edit_single_title(self):
        """用例编号030：mp登录后，进入素材管理的图文界面，添加单图文的标题(64长特殊字符输入)"""
        expected_value = self.add_single_page_text_title("030")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_031_edit_single_title(self):
        """用例编号031：mp登录后，进入素材管理的图文界面，添加单图文的标题(66长特殊字符输入)"""
        expected_value = self.add_single_page_text_title("031")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_032_edit_single_title(self):
        """用例编号032：mp登录后，进入素材管理的图文界面，添加单图文的标题(短数字输入)"""
        expected_value = self.add_single_page_text_title("032")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_033_edit_single_title(self):
        """用例编号033：mp登录后，进入素材管理的图文界面，添加单图文的标题(64长数字输入)"""
        expected_value = self.add_single_page_text_title("033")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_034_edit_single_title(self):
        """用例编号034：mp登录后，进入素材管理的图文界面，添加单图文的标题(68长数字输入)"""
        expected_value = self.add_single_page_text_title("034")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_035_edit_single_title(self):
        """用例编号035：mp登录后，进入素材管理的图文界面，添加单图文的标题(短组合输入)"""
        expected_value = self.add_single_page_text_title("035")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_036_edit_single_title(self):
        """用例编号036：mp登录后，进入素材管理的图文界面，添加单图文的标题(64组合输入)"""
        expected_value = self.add_single_page_text_title("036")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_037_edit_single_title(self):
        """用例编号037：mp登录后，进入素材管理的图文界面，添加单图文的标题(68组合输入)"""
        expected_value = self.add_single_page_text_title("037")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_038_edit_single_title(self):
        """用例编号038：mp登录后，进入素材管理的图文界面，添加单图文的标题(空内容输入)"""
        expected_value = self.add_single_page_text_title("038")
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_039_edit_single_title(self):
        """用例编号039：mp登录后，进入素材管理的图文界面，添加单图文的标题(删除标题内容)"""
        expected_value = self.add_single_page_text_title("039")
        SourceManagePage(self.driver).get_mp_single_title_input().send_keys(Keys.BACKSPACE)
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_040_edit_single_title(self):
        """用例编号040：mp登录后，进入素材管理的图文界面，添加单图文的标题(删空标题内容)"""
        expected_value = self.add_single_page_text_title("040")
        SourceManagePage(self.driver).get_mp_single_title_input().send_keys(Keys.BACKSPACE)
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)

    def test_041_edit_single_title(self):
        """用例编号041：mp登录后，进入素材管理的图文界面，添加单图文的标题(更新标题内容)"""
        expected_value = self.add_single_page_text_title("041")
        SourceManagePage(self.driver).get_mp_single_title_input().send_keys(Keys.BACKSPACE)
        input_value = get_input_value("041")
        SourceManagePage(self.driver).get_mp_single_title_input().send_keys(input_value)
        logger.info("测试判断:%s 是否等于:%s" % (SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value))
        self.assertEqual(SourceManagePage(self.driver).get_mp_single_shown_title_text(), expected_value)




'''
@author Mavis

'''