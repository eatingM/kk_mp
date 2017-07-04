#!usr/bin/python
# coding:utf-8


from page_function import *
from mp.test_model.models.my_logger import *


class Page(object):
    mp_url = "http://192.168.2.88:8050/WxMgr/webconsole"

    logger = logging.getLogger("main.base_page")

    def __init__(self, selenium_driver, base_url=mp_url, parent=None):
        """
        1、指定url打开后缀
        2、指定启动的driver（指定浏览器）
        3、指定超时时间
        4、
        :param selenium_driver:
        :param base_url:
        :param parent:
        :return:
        """
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        """
        定义页面跳转方法，私有方法
        :param url:
        :return:
        """
        self.url = self.base_url + url
        self.driver.get(self.url)

        # assert self.on_page(self.url), "Fail to get onto the page!"

    def find_element(self, loc):
        """
        定义查找元素方法，传入的loc是一个list，包括查找方式和查找值
        :param loc:
        :return:
        """
        by = loc[0]
        value = loc[1]
        return getElement(by, self.driver, value)

    def find_elements(self, loc):
        """
        定义批量查找方式
        :param loc:
        :return:
        """
        return self.driver.find_elemnets(loc)

    def open(self, url):
        """
        公有的页面打开方法
        :param url:
        :return:
        """
        self._open(url)

    def on_page(self, url):
        """

        :param url:
        :return:
        """
        return self.driver.current_url == url

    def script(self, src):
        """
        javascript执行方法
        :param src:
        :return:
        """

        return self.driver.execute_script(src)


if __name__ == "__main__":
    url = "/login.jsp"

    dr = chrome_browser()
    a = Page(dr)
    a.open(url)

'''
@author Mavis

'''
