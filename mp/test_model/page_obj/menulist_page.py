#!usr/bin/python
# coding:utf-8

from mp.test_model.page_obj.base_page import *
from page_function import *
from mp.test_model.models.my_logger import *


class MenulistPage(Page):
    """
    mp左侧管理菜单界面
    """
    logger = logging.getLogger("main.menulist_page")

    # Element loc
    mp_basic_manage_loc = get_page_element(xml_list[1], "mp_basic_manage_loc")
    mp_source_manage_loc = get_page_element(xml_list[1], "mp_source_manage_loc")

    # Action

    def get_mp_basic_manage_btn(self):

        return self.find_element(self.mp_basic_manage_loc)

    def click_mp_basic_manage_btn(self):

        self.get_mp_basic_manage_btn().click()

    def get_mp_source_manage_btn(self):

        return self.find_element(self.mp_source_manage_loc)

    def click_mp_source_manage_btn(self):

        self.get_mp_source_manage_btn().click()



'''
@author Mavis

'''