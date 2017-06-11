#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import Scrapylog

class getToutiaoInfo:
	def __init__(self):
		self.header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0","Host":"www.toutiao.io" }
		self.log = Scrapylog.scrapylong()


	def getUrlInfo(self,url):
		try:
			pagecontent = requests.get(url,headers=self.header)
			if pagecontent.status_code == requests.codes.ok:
				pagecontent.close()
				logmsg = 'url:' + url + ' Download!!'
				self.log.printlog(1,logmsg)
				return pagecontent.text
			else:
				logmsg = 'url:' + url + ' status:' + pagecontent.status_code + ' don\'t Download!!'
				self.log.printlog(3,logmsg)
				return None
		except:
			logmsg = 'url:' + url + 'Except'
			self.log.printlog(4,logmsg)
			return None


if __name__ == '__main__':
	test = getToutiaoInfo()
	info = test.getUrlInfo('https://toutiao.io/prev/2017-03-07')
	with open('test.html','wb') as writefile:
		writefile.write(info)