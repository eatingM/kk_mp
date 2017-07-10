#!usr/bin/python
# coding:utf-8

from mp.test_model.page_obj.base_page import *


class CustomMenu(Page):

    """
    自定义菜单界面

    """

    # Action

    def get_mp_custom_menu_manage_text(self):
        """
        返回自定义菜单按钮的文字内容
        :return:
        """
        return self.find_element(self.get_element_loc("mp_custom_menu_manage_loc")).text

'''
@author Mavis

'''