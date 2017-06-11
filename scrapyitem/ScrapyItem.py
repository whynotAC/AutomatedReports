#!/usr/bin/env python
#-*-coding:utf-8-*-

import re
import json
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import ScrapyRequests
import Scrapylog

class getItem:
	def __init__(self):
		self.weekday = '//h3[@class="date"]/span[1]/text()'
		self.datetime = '//h3[@class="date"]/small[1]/text()'
		self.url = '//h3[@class="date"]/a/@href'
		self.recommendinfo = '//div[@class="posts"]/div[@class="post"]'
		self.thumbsup = '//div/div[1]/a[1]/span[1]/text()'
		self.collection = '//div/div[1]/a[2]/span[1]/text()'
		self.doctitle = '//div/div[@class="content"]//a[1]/@title'
		self.docurl = '//div/div[@class="content"]//a[1]/@href'
		self.docsource = '//div/div[@class="content"]/div[1]/text()'
		self.doccomment = '//div/div[@class="content"]/div/span/text()'
		self.docauthorname = '//div/div[@class="user-info"]//h4/text()'
		self.docsubjectname = '//div/div[@class="subject-name"]/a/text()'
		self.log = Scrapylog.scrapylong()

	def __getweekday(self,html):
		pageinfo = etree.HTML(html)
		weekdayinfo = str(pageinfo.xpath(self.weekday))
		return self.__strip(weekdayinfo)

	def __getdatetime(self,html):
		pageinfo = etree.HTML(html)
		datetimeinfo = str(pageinfo.xpath(self.datetime));
		return self.__strip(datetimeinfo)

	def __getpageurl(self,html):
		pageinfo = etree.HTML(html)
		urlinfo = str(pageinfo.xpath(self.url))
		return self.__strip(urlinfo)

	def __getrecommendinfo(self,html):
		pageinfo = etree.HTML(html)
		return pageinfo.xpath(self.recommendinfo)

	def __getdocthmbsup(self,html):
		pageinfo = etree.HTML(html)
		thumbsupinfo = str(pageinfo.xpath(self.thumbsup))
		return self.__replacechar(thumbsupinfo,'\D')

	def __getdoccollection(self,html):
		pageinfo = etree.HTML(html)
		collectioninfo = str(pageinfo.xpath(self.collection))
		return self.__replacechar(collectioninfo,'\D')

	def __getdoctitle(self,html):
		pageinfo = etree.HTML(html)
		doctitleinfo = str(pageinfo.xpath(self.doctitle))
		return self.__strip(doctitleinfo)

	def __getdocurl(self,html):
		pageinfo = etree.HTML(html)
		docurl = str(pageinfo.xpath(self.docurl))
		return self.__strip(docurl)

	def __getdocsource(self,html):
		pageinfo = etree.HTML(html)
		docsourceinfo = str((pageinfo.xpath(self.docsource)))
		docsourceinfo = docsourceinfo.replace(' ','')
		docsourceinfo = docsourceinfo.replace('\\n','')
		docsourceinfo = docsourceinfo.replace('\\xa0','')
		docsourceinfo = docsourceinfo.replace('[','')
		docsourceinfo = docsourceinfo.replace(']','')
		return self.__replacechar(docsourceinfo,'[u\'|\'|,]+')

	def __getdoccomment(self,html):
		pageinfo = etree.HTML(html)
		doccommentinfo = str(pageinfo.xpath(self.doccomment))
		return self.__replacechar(doccommentinfo,'\D')

	def __getdocauthor(self,html):
		pageinfo = etree.HTML(html)
		docauthorinfo = str(pageinfo.xpath(self.docauthorname))
		return self.__strip(docauthorinfo)

	def __getdocsubjectname(self,html):
		pageinfo = etree.HTML(html)
		docsubjectnameinfo = str(pageinfo.xpath(self.docsubjectname))
		return self.__strip(docsubjectnameinfo)

	def __replacechar(self,inputstr,pattern=''):
		outputstr = re.sub(pattern,'',inputstr)
		return outputstr

	def __strip(self,inputstr):
		if inputstr.find('[u\'') != -1:
			outputstr = inputstr.replace('[u\'','').replace('\']','')
		else:
			outputstr = inputstr.replace('[\'','').replace('\']','')
		return outputstr

	def combinationjson(self,html,filename):
		try:
			returnjson = {}
			returnjson['weekday'] = self.__getweekday(html)
			returnjson['datetime'] = self.__getdatetime(html)
			returnjson['url'] = self.__getpageurl(html)
			datalist = []
			commendinfos = self.__getrecommendinfo(html)
			for i in range(0,len(commendinfos)):
				dochtml =  etree.tostring(commendinfos[i])
				datadict = {}
				datadict['docthmbsup'] = self.__getdocthmbsup(dochtml)
				datadict['doccollection'] = self.__getdoccollection(dochtml)
				datadict['doctitle'] = self.__getdoctitle(dochtml)
				datadict['docurl'] = self.__getdocurl(dochtml)
				datadict['docsource'] = self.__getdocsource(dochtml)
				datadict['doccomment'] = self.__getdoccomment(dochtml)
				datadict['docauthor'] = self.__getdocauthor(dochtml)
				datadict['docsubjectname'] = self.__getdocsubjectname(dochtml)
				datalist.append(datadict)
			returnjson['docs'] = datalist
			with open(filename,'wb') as docjson:
				json.dump(returnjson,docjson)
			msg = filename + ' combinationjson ok'
			self.log.printlog(1,msg)
			return True
		except:
			msg = filename + ' combinationjson failed'
			self.log.printlog(3,msg)
			return False


if __name__ == '__main__':
	test = getItem()
	with open('test.html') as html:
		context = html.read()
	test.combinationjson(context,'div.json')
	
