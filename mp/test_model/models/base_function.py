#!usr/bin/python
# coding:utf-8

from browser_driver import *
from xml.dom import minidom
import re
from my_logger import *


logger = logging.getLogger("main.base_function")


def insert_img(driver, file_name):

    """
    insert_ima方法：生成测试图片文件
    base_dir = os.path.dirname(os.path.abspath(__file__))
    获得当前文件的所在目录
    base_dir = str(base_dir)
    base_dir = base_dir.split("\\test_model")[0]
    做路劲分割，为路劲拼接做准备
    file_path = base_dir + "\\report\\image\\" + file_name
    windows下使用\\

    :param driver, file_name
    :return
    """
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = str(base_dir)
        base_dir = base_dir.split("\\test_model")[0]
        file_path = base_dir + "\\report\\image\\" + file_name
        driver.get_screenshot_as_file(file_path)
        logger.info(u"生成截图文件:%s" % file_path)
    except Exception as e:
        logger.error(u"生成截图文件失败！")
        logger.error(str(e))


def read_xml(xml_file):
    """
    read_xml方法：读取xml文件，返回所有根节点
    :param xml_file
    :return root

    """
    try:
        dom = minidom.parse(xml_file)
        root = dom.documentElement
        logger.info(u"打开%s文件读取..."%xml_file)
        return root
    except Exception as e:
        logger.error(u"%s文件读取失败!"%xml_file)
        logger.error(str(e))


def get_test_number(test_number):

    """
    get_test_number方法：处理传入的测试用例编号
    :param test_number:
    :return:
    """
    try:
        test_number = str(test_number)
        result = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", test_number)
        return int(result)
    except Exception as e:
        logger.error("输入的测试用例编号%s 异常，请检查后再次输入！" % test_number)


if __name__ == '__main__':

    dr = chrome_browser()
    url = "http://www.baidu.com"
    dr.get(url)
    insert_img(dr, "test_0615.jpg")
    dr.quit()





'''
@author Mavis

'''