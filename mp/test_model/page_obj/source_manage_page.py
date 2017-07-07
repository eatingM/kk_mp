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

    # Element loc

    mp_source_manage_title_loc = get_page_element(xml_list[1], "mp_source_manage_title_loc")
    mp_add_single_page_text_loc = get_page_element(xml_list[1], "mp_add_single_page_text_loc")
    mp_add_new_single_page_text_loc = get_page_element(xml_list[1], "mp_add_new_single_page_text_loc")
    mp_add_multi_page_text_loc = get_page_element(xml_list[1], "mp_add_multi_page_text_loc")
    mp_image_manage_loc = get_page_element(xml_list[1], "mp_image_manage_loc")
    mp_image_size_note_loc = get_page_element(xml_list[1], "mp_image_size_note_loc")
    mp_audio_manage_loc = get_page_element(xml_list[1], "mp_audio_manage_loc")
    mp_audio_add_btn_loc = get_page_element(xml_list[1], "mp_audio_add_btn_loc")
    mp_video_manage_loc = get_page_element(xml_list[1], "mp_video_manage_loc")
    mp_video_add_btn_loc = get_page_element(xml_list[1], "mp_video_add_btn_loc")
    mp_single_title_loc = get_page_element(xml_list[1], "mp_single_title_loc")
    mp_single_shown_title_loc = get_page_element(xml_list[1], "mp_single_shown_title_loc")
    mp_single_image_loc = get_page_element(xml_list[1], "mp_single_image_loc")
    mp_single_shown_image_loc = get_page_element(xml_list[1], "mp_single_shown_image_loc")

    # Action

    def get_mp_single_shown_image_src(self):

        return self.find_element(self.mp_single_shown_image_loc).get_attribute("src")

    def get_mp_single_image_input(self):

        return self.find_element(self.mp_single_image_loc)

    def get_mp_single_shown_title_text(self):

        return self.find_element(self.mp_single_shown_title_loc).text

    def get_mp_single_title_input(self):

        return self.find_element(self.mp_single_title_loc)

    def get_mp_video_add_btn(self):

        return self.find_element(self.mp_video_add_btn_loc)

    def get_mp_video_add_btn_text(self):

        return self.get_mp_video_add_btn().text

    def get_mp_video_manage_btn(self):

        return self.find_element(self.mp_video_manage_loc)

    def get_mp_audio_add_btn(self):

        return self.find_element(self.mp_audio_add_btn_loc)

    def get_mp_audio_add_btn_text(self):

        return self.get_mp_audio_add_btn().text

    def get_mp_audio_manage_btn(self):

        return self.find_element(self.mp_audio_manage_loc)

    def get_mp_image_size_note_text(self):

        return self.find_element(self.mp_image_size_note_loc).text

    def get_mp_image_manage_btn(self):

        return self.find_element(self.mp_image_manage_loc)

    def get_mp_source_manage_title(self):

        return self.find_element(self.mp_source_manage_title_loc).text

    def get_add_new_single_page_text(self):

        return self.find_element(self.mp_add_new_single_page_text_loc).text

    def get_mp_add_single_page_text_btn(self):

        return self.find_element(self.mp_add_single_page_text_loc)

    def get_mp_add_multi_page_text_btn(self):

        return self.find_element(self.mp_add_multi_page_text_loc)

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
            logger.error("向单图文标题栏输入操作异常！")
            logger.error("系统抛出异常！%s" % str(e))
            flag = False
            return flag

'''
@author Mavis

'''