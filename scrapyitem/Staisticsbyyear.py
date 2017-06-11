#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import json

def dealdatadir(dirpath):
	writejson = {}
	level1alldir = os.listdir(dirpath)
	#处理年份的数据
	for level1dir in level1alldir:
		#print(str(level1dir))
		yearnumber = 0;
		yearjson = {}
		monthjson = {}
		level1child = os.path.join('%s/%s' % (dirpath,level1dir))
		level2alldir = os.listdir(level1child)
		for level2dir in level2alldir:
			level2child = os.path.join('%s/%s' % (level1child,level2dir))
			monthnumber = dealallfile(level2child)
			monthjson[str(level2dir)] = monthnumber
			yearnumber = yearnumber + monthnumber
		yearjson['sum'] = yearnumber
		yearjson['month'] = monthjson
		writejson[str(level1dir)] = yearjson
	with open('Statistics.txt','wb') as docjson:
		json.dump(writejson,docjson)

def dealallfile(filepath):
	monthnumber = 0
	fileallname = os.listdir(filepath)
	for filename in fileallname:
		filepathandname = os.path.join('%s/%s' % (filepath,filename))
		with open(filepathandname,'r') as f:
			fileinfo = json.load(f)
		monthnumber = monthnumber + len(fileinfo["docs"])
	return monthnumber

if __name__ == '__main__':
	basicdir = 'datadir'
	dealdatadir(basicdir)