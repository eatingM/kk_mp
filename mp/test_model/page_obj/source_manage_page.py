#!usr/bin/python
# coding:utf-8


from mp.test_model.page_obj.base_page import *
from page_function import *
from mp.test_model.models.my_logger import *
from mp.test_model.page_obj.menulist_page import *


class SourceManagePage(Page):

    """
    mp左侧管理菜单:基础管理-素材管理界面
    """
    logger = logging.getLogger("main.SourceManagePage")

    # Action

    """
    获得元素的方法

    """

    def get_single_shown_summary_text(self):

        return self.find_element(self.get_element_loc("mp_single_shown_summary_loc")).text

    def get_mp_single_summary_input(self):

        return self.find_element(self.get_element_loc("mp_single_summary_loc"))

    def get_mp_single_image_size_error_hint(self):

        return self.find_element(self.get_element_loc("mp_single_image_size_error_loc")).text

    def get_mp_single_image_error_hint(self):

        return self.find_element(self.get_element_loc("mp_single_image_error_loc")).text

    def get_mp_single_shown_image_src(self):

        return self.find_element(self.get_element_loc("mp_single_shown_image_loc")).get_attribute("src")

    def get_mp_single_image_input(self):

        return self.find_element(self.get_element_loc("mp_single_image_loc"))

    def get_mp_single_shown_title_text(self):

        return self.find_element(self.get_element_loc("mp_single_shown_title_loc")).text

    def get_mp_single_title_input(self):

        return self.find_element(self.get_element_loc( "mp_single_title_loc"))

    def get_mp_video_add_btn(self):

        return self.find_element(self.get_element_loc("mp_video_add_btn_loc"))

    def get_mp_video_add_btn_text(self):

        return self.get_mp_video_add_btn().text

    def get_mp_video_manage_btn(self):

        return self.find_element(self.get_element_loc("mp_video_manage_loc"))

    def get_mp_audio_add_btn(self):

        return self.find_element(self.get_element_loc("mp_audio_add_btn_loc"))

    def get_mp_audio_add_btn_text(self):

        return self.get_mp_audio_add_btn().text

    def get_mp_audio_manage_btn(self):

        return self.find_element(self.get_element_loc("mp_audio_manage_loc"))

    def get_mp_image_size_note_text(self):

        return self.find_element(self.get_element_loc("mp_image_size_note_loc")).text

    def get_mp_image_manage_btn(self):

        return self.find_element(self.get_element_loc("mp_image_manage_loc"))

    def get_mp_source_manage_title(self):

        return self.find_element(self.get_element_loc("mp_source_manage_title_loc")).text

    def get_add_new_single_page_text(self):

        return self.find_element(self.get_element_loc("mp_add_new_single_page_text_loc")).text

    def get_mp_add_single_page_text_btn(self):

        return self.find_element(self.get_element_loc("mp_add_single_page_text_loc"))

    def get_mp_add_multi_page_text_btn(self):

        return self.find_element(self.get_element_loc("mp_add_multi_page_text_loc"))

    def get_mp_text_btn(self):

        return self.find_element(self.get_element_loc("mp_text_btn_loc"))

    def get_mp_edit_text_btn(self):

        return self.find_element(self.get_element_loc("mp_edit_text_btn_loc"))

    def get_mp_edit_text_textarea(self):

        return self.find_element(self.get_element_loc("mp_edit_text_textarea_loc"))

    def get_mp_save_text_btn(self):

        return self.find_element(self.get_element_loc("mp_save_text_btn_loc"))

    def get_new_single_page_text_page(self):
        """
        跳转到添加单图文界面
        作为测试用例执行的关键步骤
        :return:
        """

        flag = True
        try:
            MenulistPage(self.driver).click_mp_source_manage_btn()
            self.get_mp_add_single_page_text_btn().click()
            return flag
        except Exception as e:
            logger.error("点击新增单图文按钮操作异常！")
            logger.error(str(e))
            flag = False
            return flag

    def get_new_multi_page_text_page(self):
        """
        跳转到添加多图文界面
        作为测试用例执行的关键步骤
        :return:
        """

        flag = True
        try:
            MenulistPage(self.driver).click_mp_source_manage_btn()
            self.get_mp_add_multi_page_text_btn().click()
            return flag
        except Exception as e:
            logger.error("点击新增多图文按钮操作异常！")
            logger.error(str(e))
            flag = False
            return flag

    def get_image_manage_page(self):
        """
        跳转到添加图片界面
        作为测试用例执行的关键步骤
        :return:
        """
        flag = True
        try:
            MenulistPage(self.driver).click_mp_source_manage_btn()
            self.get_mp_image_manage_btn().click()
            return flag
        except Exception as e:
            logger.error("点击图片按钮操作异常！")
            logger.error(str(e))
            flag = False
            return flag

    def get_audio_manage_page(self):
        """
        跳转到添加音频界面
        作为测试用例执行的关键步骤
        :return:
        """
        flag = True
        try:
            MenulistPage(self.driver).click_mp_source_manage_btn()
            self.get_mp_audio_manage_btn().click()
            return flag
        except Exception as e:
            logger.error("点击语音按钮操作异常！")
            logger.error(str(e))
            flag = False
            return flag

    def get_video_manage_page(self):
        """
        跳转到添加视频界面
        作为测试用例执行的关键步骤
        :return:
        """
        flag = True
        try:
            MenulistPage(self.driver).click_mp_source_manage_btn()
            self.get_mp_video_manage_btn().click()
            return flag
        except Exception as e:
            logger.error("点击视频按钮操作异常！")
            logger.error(str(e))
            flag = False
            return flag

    def get_single_page_text_title_input(self, casenumber):
        """
        预置条件：已经到了单图文的编辑界面
        进行单图文的标题输入
        作为测试用例执行的关键步骤
        :return:
        """
        flag = True
        try:
            input_value = get_input_value(casenumber)
            self.get_mp_single_title_input().send_keys(input_value)
            return flag
        except Exception as e:
            logger.error("向单图文标题栏输入操作异常！")
            logger.error("系统抛出异常！%s" % str(e))
            flag = False
            return flag

    def get_single_page_text_image_input(self, casenumber):
        """
        预置条件：已经到了单图文的编辑界面
        进行单图文的标题输入
        作为测试用例执行的关键步骤
        :return:
        """
        flag = True
        try:
            input_value = get_input_value(casenumber)
            self.get_mp_single_image_input().send_keys(input_value)
            return flag
        except Exception as e:
            logger.error("单图文编辑时选择图书时操作异常！")
            logger.error("系统抛出异常！%s" % str(e))
            flag = False
            return flag

    def get_summary_input(self, casenumber):
        """
        预置条件：已经到了单图文的编辑界面
        进行单图文的摘要输入
        :param casenumber:
        :return:
        """
        flag = True
        try:
            input_value = get_input_value(casenumber)
            self.get_mp_single_summary_input().send_keys(input_value)
            return flag
        except Exception as e:
            logger.error("向单图文摘要栏输入操作异常！")
            logger.error("系统抛出异常！%s" % str(e))
            flag = False
            return flag

    def get_text_input(self, case_number):
        """

        :param case_number:
        :return:
        """
        flag = True
        try:
            input_value = get_input_value(case_number)
            logger.info("点击正文按钮...")
            self.get_mp_text_btn().click()
            logger.info("点击编辑正文按钮...")
            self.get_mp_edit_text_btn().click()
            logger.info("向正文编辑框输入内容: %s" % input_value)
            self.get_mp_edit_text_textarea().send_keys(input_value)
            logger.info("点击保存正文...")
            self.get_mp_save_text_btn().click()
            return flag
        except Exception as e:
            logger.error("向单图文正文输入框输入操作异常！")
            logger.error("系统抛出异常！%s" % str(e))
            flag = False
            return flag

    def get_exist_text_input(self):

        """

        :return:
        """
        flag = True
        try:
            logger.info("点击正文按钮...")
            self.get_mp_text_btn().click()
            logger.info("点击编辑已有正文按钮...")
            self.get_mp_edit_text_btn().click()

            exist_value = self.get_mp_edit_text_textarea().text
            logger.info("获取已有正文的内容: %s" % exist_value)
            return flag, exist_value

        except Exception as e:
            logger.error("向单图文正文输入框输入操作异常！")
            logger.error("系统抛出异常！%s" % str(e))
            flag = False
            return flag, exist_value
'''
@author Mavis

'''