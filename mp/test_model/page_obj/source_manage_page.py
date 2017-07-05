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
    try:
        mp_source_manage_title_loc = get_page_element(xml_list[1], "mp_source_manage_title_loc")
        mp_add_single_page_text_loc = get_page_element(xml_list[1], "mp_add_single_page_text_loc")
        mp_add_new_single_page_text_loc = get_page_element(xml_list[1], "mp_add_new_single_page_text_loc")
    except Exception as e:
        logger.error(u"页面元素加载异常！！")
        logger.error(u"系统抛出异常:%s" % str(e))

    # Action

    def get_mp_source_manage_title(self):

        return self.find_element(self.mp_source_manage_title_loc).text

    def get_add_new_single_page_text(self):

        return self.find_element(self.mp_add_new_single_page_text_loc).text

    def get_new_page_text_page(self):
        MenulistPage(self.driver).click_mp_source_manage_btn()
        self.find_element(self.mp_add_single_page_text_loc).click
'''
@author Mavis

'''