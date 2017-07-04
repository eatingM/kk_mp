#!usr/bin/python
# coding:utf-8

import logging,os


class Logger(object):

    def __init__(self, clevel=logging.DEBUG, flevel=logging.DEBUG):
        """

        :param path:
        :param clevel:
        :param flevel:
        :return:
        """
        self.logger_file_name = os.path.dirname(os.path.abspath("logger.py")).split("\\test_model")[0] + "\\report\\mp_test_log.txt"
        self.test = "mod"
        self.logger = logging.getLogger(self.test)
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            self.fmt = logging.Formatter("%(asctime)s - [file:%(filename)s]-[func:%(funcName)s]"
                                         "[line:%(lineno)d] - %(levelname)s: %(message)s")
            # 设置控制台日志
            sh = logging.StreamHandler()
            sh.setFormatter(self.fmt)
            sh.setLevel(clevel)

            # 设置文件日志
            fh = logging.FileHandler(self.logger_file_name)
            fh.setFormatter(self.fmt)
            fh.setLevel(flevel)

            self.logger.addHandler(sh)
            self.logger.addHandler(fh)

    def debug(self, message):
        """
        输出debug信息
        :param message:
        :return:
        """
        self.logger.debug(message)

    def info(self, message):
        """

        :param message:
        :return:
        """
        self.logger.info(message)

    def warn(self, message):
        """

        :param message:
        :return:
        """
        self.logger.warning(message)

    def error(self, message):
        """

        :param message:
        :return:
        """
        self.logger.error(message)

    def critical(self, message):
        """

        :param message:
        :return:
        """
        self.logger.critical(message)

if __name__ == "__main__":

    logtest = logging.getLogger("mod.test1")
    logtest.info("This is a test message!")

'''
@author Mavis

'''