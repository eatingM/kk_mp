#!usr/bin/python
# coding:utf-8


import sys
sys.path.append("D:\\PycharmProjects\\kk_mp\\mp\\test_model\\page_obj")
sys.path.append("D:\\PycharmProjects\\kk_mp\\mp\\test_model\\models")
from mp.test_model.page_obj.loginPage import *
from mp.test_model.page_obj.base_page import *
from time import sleep


class MainPage(Page):

    """
    mp 主界面
    """
    # Element loc

    mp_quict_loc = get_page_element(xml_list[1], "mp_quict_loc")
    mp_custom_menu_loc = get_page_element(xml_list[1], "mp_custom_menu_loc")
    mp_feedback_loc = get_page_element(xml_list[1], "mp_feedback_loc")
    mp_keyword_loc = get_page_element(xml_list[1], "mp_keyword_loc")
    mp_unrecognized_loc = get_page_element(xml_list[1], "mp_unrecognized_loc")
    mp_timestamp_loc = get_page_element(xml_list[1], "mp_timestamp_loc")
    mp_main_page_loc = get_page_element(xml_list[1], "mp_main_page_loc")
    mp_service_name_loc = get_page_element(xml_list[1], "mp_service_name_loc")
    mp_service_id_loc = get_page_element(xml_list[1], "mp_service_id_loc")
    mp_note_loc = get_page_element(xml_list[1], "mp_note_loc")
    mp_send_all_loc = get_page_element(xml_list[1], "mp_send_all_loc")

    # Action

    def get_mp_send_all_text(self):
        return self.find_element(self.mp_send_all_loc).text

    def get_mp_note_text(self):
        return self.find_element(self.mp_note_loc).text

    def get_mp_service_id_text(self):
        return self.find_element(self.mp_service_id_loc).text

    def get_mp_service_name_text(self):
        return self.find_element(self.mp_service_name_loc).text

    def get_mp_main_page_loc_text(self):
        return self.find_element(self.mp_main_page_loc).text

    def get_mp_timestamp(self, LoginPage, username, password):
        LoginPage.mp_user_login(username, password)
        return self.find_element(self.mp_timestamp_loc).text

    def get_mp_unrecognized_btn(self):
        return self.find_element(self.mp_unrecognized_loc)

    def turn_to_unrecognized_feedback(self, LoginPage, username, password):
        LoginPage.mp_user_login(username, password)
        self.get_mp_unrecognized_btn().click()

    def get_mp_keyword_feedback_btn(self):
        return self.find_element(self.mp_keyword_loc)

    def turn_to_keyword_feedback(self, LoginPage, username, password):
        LoginPage.mp_user_login(username,password)
        self.get_mp_feedback_btn().click

    def get_mp_feedback_btn(self):
        return self.find_element(self.mp_feedback_loc)

    def turn_to_feedback(self, LoginPage, username, password):
        LoginPage.mp_user_login(username, password)
        self.get_mp_feedback_btn().click()

    def get_custom_menu_btn(self):
        return self.find_element(self.mp_custom_menu_loc)

    def turn_to_custom_menu(self, LoginPage, username, password):
        LoginPage.mp_user_login(username, password)
        self.get_custom_menu_btn().click()

    def get_mp_note_btn(self):
        return self.find_element(self.mp_note_loc)

    def turn_to_send_page(self):
        self.get_mp_note_btn().click()

    def get_mp_quit_btn(self):

        return self.find_element(self.mp_quict_loc)

    def mp_login_out(self):

        self.get_mp_quit_btn().click()
        logger.info(u"退出登录中...")


if __name__ =='__main__':

    dr = chrome_browser()
    print MainPage(dr).get_mp_timestamp(LoginPage(dr),"0099", "1")
    #MainPage(dr).turn_to_feedback(LoginPage(dr), "0099", '1')
    #MainPage(dr).turn_to_custom_menu(LoginPage(dr), "0099", '1')
    #MainPage(dr).mp_login_out(LoginPage(dr), '0099', '1')


    '''
    loginPage(dr).mp_user_login("0099",'1')
    dr.maximize_window()
    print main_page(dr).get_mp_quit_btn().text
    main_page(dr).get_mp_quit_btn().click()
    #main_page(dr).open('/logout.do')
    '''

    sleep(1)

'''
@author Mavis

'''