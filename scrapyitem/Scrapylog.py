#!/usr/bin/env python
#-*-coding:utf-8-*-

import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class scrapylong:
	def __init__(self):
		logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
			datefmt='%a, %d %b %Y %H:%M:%S',
			filename='Itemlog.log',
			filemode='a')

	def __info(self,msg):
		logging.info(msg)

	def __debug(self,msg):
		logging.debug(msg)

	def __warning(self,msg):
		logging.warning(msg)

	def printlog(self,flag,msg):
		if flag == 1:   #Info
			self.__info(msg)
		elif flag == 2:	#Debug
			self.__debug(msg)
		elif flag == 3:	#Warning
			self.__warning(msg)
		else:
			self.__info('Other Msg:' + msg)

if __name__ == '__main__':
	log = scrapylong()
	log.Info('hello')
	log.Debug('debug')
	log.Warning('warning')