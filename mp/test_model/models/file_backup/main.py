#!usr/bin/python
# coding:utf-8

import logging
import logging.config

logging.config.fileConfig('D:/PycharmProjects/kk_mp/mp/test_model/models/logging.conf')
root_logger = logging.getLogger('root')

"""
#root_logger.debug('test root logger...')

logger = logging.getLogger('main')
#logger.info('test main logger')
#logger.info('start import module \'mod\'...')

import browser_driver


#logger.debug('let\'s test browser_driver.testLogger()')

browser_driver.set_param("chrome")


#root_logger.info('finish test...')

"""
'''
@author Mavis

'''