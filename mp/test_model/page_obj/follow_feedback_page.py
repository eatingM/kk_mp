#!usr/bin/python
# coding:utf-8

from mp.test_model.page_obj.base_page import *


class FollowFeedbackMenu(Page):

    """关注时回复界面"""
    # Element loc

    mp_feedback_manage_loc = get_page_element(xml_list[1], "mp_feedback_manage_loc")

    # Action

    def get_mp_feedback_manage_loc_text(self):
        """
        获得关注时回复管理的文字内容
        :return:
        """

        return self.find_element(self.mp_feedback_manage_loc).text


'''
@author Mavis

'''