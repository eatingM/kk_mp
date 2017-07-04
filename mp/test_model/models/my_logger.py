#!usr/bin/python
# coding:utf-8

import logging
import os

logger_file_name = os.path.dirname(os.path.abspath("logger.py")).split("\\test_model")[0] + "\\report\\mp_test_log.txt"
test = "main"
logger = logging.getLogger(test)
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    fmt = logging.Formatter("%(asctime)s -%(name)s- [file:%(filename)s]-[func:%(funcName)s]"
                                     "[line:%(lineno)d] - %(levelname)s: %(message)s")
    # 设置控制台日志
    sh = logging.StreamHandler()
    sh.setFormatter(fmt)
    sh.setLevel(logging.DEBUG)

    # 设置文件日志
    fh = logging.FileHandler(logger_file_name)
    fh.setFormatter(fmt)
    fh.setLevel(logging.DEBUG)

    logger.addHandler(sh)
    logger.addHandler(fh)

def debug( message):
    """
    输出debug信息
    :param message:
    :return:
    """
    logger.debug(message)

def info(message):
    """

    :param message:
    :return:
    """
    logger.info(message)


def warn( message):
    """

    :param message:
     :return:
    """
    logger.warning(message)


def error( message):
    """

    :param message:
    :return:
    """
    logger.error(message)


def critical(self, message):
    """

    :param message:
    :return:
    """
    logger.critical(message)

if __name__ == "__main__":

    logtest = logging.getLogger("main.test1")
    logtest.info("This is a test message!")
'''
@author Mavis

'''