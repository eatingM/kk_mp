#!usr/bin/python
# coding:utf-8

from mp.test_model.page_obj.base_page import *


class UnrecognizedFeedbackMenu(Page):

    """无法识别回复界面"""

    # Action

    def get_mp_unrecognized_manage_text(self):
        """
        获得无法识别管理的文字内容
        :return:
        """
        return self.find_element(self.get_element_loc("mp_unrecognized_manage_loc")).text

'''
@author Mavis

'''