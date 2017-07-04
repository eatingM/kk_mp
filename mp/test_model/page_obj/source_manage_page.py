#!usr/bin/python
# coding:utf-8


from mp.test_model.page_obj.base_page import *
from page_function import *
from mp.test_model.models.my_logger import *


class SourceManagePage(Page):

    """
    mp左侧管理菜单:基础管理-素材管理界面
    """
    logger = logging.getLogger("main.SourceManagePage")

    # Element loc
    mp_source_manage_title_loc = get_page_element(xml_list[1], "mp_source_manage_title_loc")

    # Action

    def get_mp_source_manage_title(self):

        return self.find_element(self.mp_source_manage_title_loc).text

'''
@author Mavis

'''