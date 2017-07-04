#!usr/bin/python
# coding:utf-8


from mp.test_model.models.base_function import *
from mp.test_model.models.my_logger import *


base_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = base_dir.split('\\test_model')[0]
xml_Page_data_dir = base_dir + '\\data\\Page_data.xml'
xml_Page_element_dir = base_dir + '\\data\\Page_element.xml'
xml_list = [xml_Page_data_dir, xml_Page_element_dir]


logger = logging.getLogger("main.page_function")


def getElement(by,driver,value):

        """
        元素定位方法
        :param by:     查找元素的方式
        :param value:  文本值
        :return:       查找到的元素
        """
        if by == "id":
            return driver.find_element_by_id(value)
        elif by == "class":
            return driver.find_element_by_class_name(value)
        elif by == "name":
            return driver.find_element_by_name(value)
        elif by == "css":
            return driver.find_element_by_css_selector(value)
        elif by == "linktext":
            return driver.find_element_by_link_text(value)
        elif by == "partcialtext":
            return driver.find_element_by_partial_link_text(value)
        elif by == "tag":
            return driver.find_element_by_tag_name(value)
        elif by == 'xpath':
            return driver.find_element_by_xpath(value)
        else:
            print u"请输入适合的查找元素方式。。。"


def get_test_data(xml_path, test_number, test_attribute):
    """
    测试数据获取封装
    xml_path=数据封装文件，test_number=测试用例编号，test_attribute= 测试用例需要获取的数据属性值
    :param xml_path:
    :param test_number:
    :param test_attribute:
    :return:
    """
    try:
        root = read_xml(xml_path)
        test_cases = root.getElementsByTagName("test_case")
        test_number = get_test_number(test_number)
        logger.info(u"读取测试数据中... 读取路径为:%s ,用例编号为%s"% (xml_list[0], test_number))
        logger.info(u"使用的测试数据属性为:%s, 读取到的测试数据值为:%s" % (test_attribute, test_cases[test_number-1].getAttribute(test_attribute)))
        return test_cases[test_number-1].getAttribute(test_attribute)
    except Exception as e:
        logger.error(u"读取测试数据失败！")
        logger.error(u"系统抛出异常:%s" % str(e))


def get_page_element(xml_path, element_name):
    """
    页面元素获取封装
    xml_path = 页面元素封装的文件，element_name=页面元素存储的数据标签名称
    loc_by 该元素的定位方式
    loc 该元素的定位信息
    :param xml_path:
    :param element_name:
    :return:
    """
    root = read_xml(xml_path)
    list =[]
    try:
        element = root.getElementsByTagName(element_name)[0]
        logger.info(u"定位元素中...")
        logger.info(u"定位元素名称为：%s" % element_name)
        list.append(element.getAttribute("loc_by"))
        logger.info(u"定位%s元素的方式为： %s" % (element_name,element.getAttribute("loc_by")))
        list.append(element.getAttribute("loc"))
        logger.info(u"定位%s元素的值为:%s" % (element_name,element.getAttribute("loc")))
        return list
    except Exception as e:
        logger.error(u"找不到元素： %s" % element_name)
        logger.error(u"系统抛出异常:%s" % str(e))


def get_login_username(case_number):
    """
    根据测试用例编号获得username的值
    :param case_number:
    :return:
    """
    try:
        username = get_test_data(xml_list[0], case_number, "username")
        return username
    except Exception as e:
        logger.error(u"系统抛出异常:%s" % str(e))


def get_login_password(case_number):
    """
    根据测试用例编号获得password的值
    :param case_number:
    :return:
    """
    try:
        password = get_test_data(xml_list[0], case_number, "password")
        return password
    except Exception as e:
        logger.error(u"系统抛出异常:%s" % str(e))


def get_expected_value(case_number):
    """
    根据测试用例编号获得断言的期望值
    :param case_number:
    :return:
    """
    try:
        expected_value = get_test_data(xml_list[0], case_number, "value")
        logger.info(u"读取测试数据中... 读取路径为:%s ,用例编号为%s,读取到的测试期望值为:%s" % (xml_list[0], case_number, expected_value ))
        return expected_value
    except Exception as e:
        logger.error(u"测试数据期望值读取失败！")
        logger.error(u"系统抛出异常:%s" % str(e))


def get_image_title(case_number):
    """
    根据测试用例编号获得截图生成的名称
    :param case_number:
    :return:
    """
    try:
        image_title = get_test_data(xml_list[0], case_number, "title")
        logger.info(u"读取测试数据中... 读取路径为:%s ,用例编号为%s,读取到的截图名称为: %s" % (xml_list[0], case_number,image_title))
        return image_title
    except Exception as e:
        logger.error(u"测试数据截图名称读取失败！")
        logger.error(u"系统抛出异常:%s" % str(e))


if __name__ == "__main__":

    print get_test_data(xml_list[0], 05, "username")
    '''
    get_login_case()
    get_login_title(001)
    '''
    '''
    print base_dir
    print get_test_data(xml_list[0], 001, "title")
    print base_dir,xml_Page_data_dir ,xml_Page_element_dir
    print xml_list[0],xml_list[1]
    '''

'''
@author Mavis

'''