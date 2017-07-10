#!usr/bin/python
# coding:utf-8

from mp.test_model.page_obj.base_page import *


class KeywordFeedbackMenu(Page):

    """关键字回复界面"""
    # Action

    def get_mp_keyword_manage_text(self):
        """
        获得关键字回复按钮文字内容
        :return:
        """
        return self.find_element(self.get_element_loc("mp_keyword_manage_loc")).text


'''
@author Mavis

'''