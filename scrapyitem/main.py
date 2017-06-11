#!/usr/bin/env python
#-*-coding:utf-8-*-

import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import ScrapyDate
import Scrapylog
import ScrapyRequests
import ScrapyItem
import os

if __name__ == '__main__':
	log = Scrapylog.scrapylong()
	log.printlog(1,'start scrapy')
	scrapytime = ScrapyDate.DealTime()
	url = ScrapyDate.getToutiaoUrl()
	request = ScrapyRequests.getToutiaoInfo()
	item = ScrapyItem.getItem()

	basedir = 'datadir'
	if os.path.exists(basedir) != True:
		os.mkdir(basedir)
	startTime = scrapytime.getstarttime()
	while scrapytime.getdisTime(scrapytime.nowTime(),startTime) > 0:
		nowdir = basedir + '\\' + str(startTime.year) + '\\' + str(startTime.month)
		if os.path.exists(nowdir) != True: 
			os.mkdir(nowdir)
		
		filename = nowdir + '\\' + scrapytime.getFilestr(startTime) + '.json'	#文件名
		requesturl = url.getUrl(scrapytime.getTimestr(startTime))				#url
		if os.path.exists(filename) == False:
			pageinfo = request.getUrlInfo(requesturl)
			if pageinfo != None:
				item.combinationjson(pageinfo,filename)

		startTime = startTime + scrapytime.disTime()

	log.printlog(1,'end scrapy')
