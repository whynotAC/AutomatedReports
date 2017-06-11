#!/usr/bin/env python
#-*-coding:utf-8-*-

import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import Scrapylog

class DealTime:
	def starttime(self):
		t_startTime = '2017-03-20 00:00:00'
		return datetime.datetime.strptime(t_startTime,'%Y-%m-%d %H:%M:%S')

	def getstarttime(self):
		return datetime.datetime.now() + datetime.timedelta(days=-5)

	def nowTime(self):
		return datetime.datetime.now()

	def disTime(self):
		return datetime.timedelta(days=1)

	def getdisTime(self,maxdata,mindata):
		return (maxdata-mindata).days

	def getTimestr(self,date):
		return date.strftime('%Y-%m-%d')

	def getYear(self,date):
		return date.year

	def getFilestr(self,date):
		return date.strftime('%Y_%m_%d')

	def getEndTime(self):
		t_EndTime = '2017-03-21 00:00:00'
		return datetime.datetime.strptime(t_EndTime,'%Y-%m-%d %H:%M:%S')

class getToutiaoUrl:
	m_baseurl ='https://toutiao.io/prev/'
	def getUrl(self,datestr):
		return self.m_baseurl+datestr

if __name__ == '__main__':
	t = DealTime()
	url = getToutiaoUrl()
	startTime = t.starttime()
	while t.getdisTime(t.nowTime(),startTime) > 0:
		print url.getUrl(t.getTimestr(startTime))
		startTime = startTime + t.disTime()
	log = Scrapylog.scrapylong()
	print(startTime.year)
	print t.getdisTime(t.nowTime(),t.starttime())