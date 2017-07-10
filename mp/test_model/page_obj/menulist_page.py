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

    # Action

    def get_mp_basic_manage_btn(self):

        return self.find_element(self.get_element_loc("mp_basic_manage_loc"))

    def click_mp_basic_manage_btn(self):

        self.get_mp_basic_manage_btn().click()

    def get_mp_source_manage_btn(self):

        return self.find_element(self.get_element_loc("mp_source_manage_loc"))

    def click_mp_source_manage_btn(self):

        flag = True
        try:
            MenulistPage(self.driver).click_mp_basic_manage_btn()
            self.get_mp_source_manage_btn().click()
            return flag
        except Exception as e:
            logger.error("点击素材管理按钮发生异常！")
            logger.error(str(e))
            flag = False
            return flag



'''
@author Mavis

'''