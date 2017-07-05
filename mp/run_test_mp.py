#!usr/bin/python
# coding:utf-8
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import sys
from mp.test_model.models.my_logger import *
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger("main.run_test_mp")


def send_mail(file_new):
    """
    1、 定义发送邮件
    :param file_new:
    :return:
    """

    f = file(file_new, 'rb')
    mail_body = f.read()
    f.close()

    server = "smtp.163.com"
    sender = 'eating<diqiuqq@163.com>'
    reciever = 'maoyt@landray.com.cn'
    msg = MIMEText(mail_body,'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['from'] = 'eating<diqiuqq@163.com>'
    msg['to'] = 'maoyt@landray.com.cn'

    try:
        smtp = smtplib.SMTP()
        smtp.connect("smtp.163.com")
        smtp.login("diqiuqq@163.com" , '')
        smtp.sendmail("diqiuqq@163.com", "maoyt@landray.com.cn", msg.as_string())
        smtp.quit()
        logger.info(u"发送邮件中：由 %s 发往 %s "%(sender, reciever))
        logger.info(u"邮件发送成功！")
    except Exception as e:
        logger.error(u"邮件发送失败！")
        logger.error(u"系统抛出异常:%s" % str(e))


def new_report(testreport_path):

    """
    二、 查找测试报告目录，找到最新生成的测试报告文件
    1. 列出当前路径testreport_path下的全部文件
    2、然后获得所有文件的时间戳，然后排序
    3、然后获得最新的那个测试报告文件

    """
    lists = os.listdir(testreport_path)
    lists.sort(key=lambda fn:os.path.getmtime(testreport_path + '\\' +fn))
    file_new = os.path.join(testreport_path, lists[-1])
    return file_new

if __name__ == "__main__":

    logger.info(u"开始执行测试用例...")
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    try:
        report_path = os.path.dirname(__file__) + "/report/"
        filename = report_path + now + '_result.html'
        logger.info(u"正在生成测试报告：%s" % filename)
        fb = open(filename, 'wb')
    except Exception as e:
        logger.error(u"生成测试报告失败！")
        logger.error(str(e))

    runner = HTMLTestRunner(stream=fb,
                            title="mp<运营管理平台>自动化测试报告",
                            description='环境: windows7 浏览器: chrome')

    case_path = os.path.dirname(__file__) + "/test_model"
    logger.info(u"正在组织测试用例...,测试用例路径为:%s" % case_path)
    try:
        discover = unittest.defaultTestLoader.discover(case_path, pattern='*_test.py')
        runner.run(discover)
        logger.info(u"开始执行...")
    except Exception as e:
        logger.error(u"用例启动失败！")
        logger.error(str(e))

    fb.close()
    file_path = new_report(report_path)
    send_mail(file_path)



'''
@author Mavis

'''