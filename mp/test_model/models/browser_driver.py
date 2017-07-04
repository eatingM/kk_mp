#!usr/bin/python
# coding:utf-8

from time import sleep
from selenium.webdriver import Remote
from my_logger import *


logger = logging.getLogger("main.browser_driver")


def set_param(browser):
    """
    set_pararm方法：指定配置浏览器和代理节点
    :param browser:
    :return:
    """
    # original host host = 'http://127.0.0.1:5555/wd/hub'
    try:
        host = 'http://192.168.2.110:5555/wd/hub'
        driver = Remote(command_executor=host,
                     desired_capabilities={'platform':'ANY',
                                           'browserName':browser,
                                           'version':'',
                                           'javascriptEnabled':True}, browser_profile=None, proxy=None,
                     keep_alive=False, file_detector=None)
        logger.debug(u"配置的主机为：%s " % host)
        return driver
    except Exception as e:
        logger.error(u"主机配置失败！Selenium Server未启动！")
        logger.error(u"系统抛出异常:%s" % str(e))


def chrome_browser():
    """
    指定浏览器为chrome
    :return:
    """
    try:
        dr = set_param("chrome")
        logger.info("指定浏览器为chrome")
        return dr
    except Exception as e:
        logger.error("指定浏览器失败！")
        logger.error(u"系统抛出异常:%s" % str(e))



def firefox_browser():
    """
    指定浏览器为firefox
    :return:
    """
    try:
        dr = set_param("firefox")
        logger.info("指定浏览器为firefox")
        return dr
    except Exception as e:
        logger.error("指定浏览器失败！")
        logger.error(u"系统抛出异常:%s" % str(e))

def ie_browser():
    """
    指定浏览器为ie
    :return:
    """
    try:
        dr = set_param("ie")
        logger.info("指定浏览器为ie")
        return dr
    except Exception as e:
        logger.error("指定浏览器失败！")
        logger.error(u"系统抛出异常:%s" % str(e))


if __name__ == "__main__":

    dr = chrome_browser()
    url = "http://www.baidu.com"
    dr.get(url)
    sleep(1)
    dr.quit()

'''
@author Mavis

'''