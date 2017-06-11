#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import json
import Scrapylog

FILESUM = 0
ITEMSUM = 0

def dealalldir(dirpath):
	global FILESUM, ITEMSUM
	log = Scrapylog.scrapylong()
	level1alldir = os.listdir(dirpath)
	for level1dir in level1alldir:
		level1child = os.path.join('%s/%s' % (dirpath,level1dir))
		level2alldir = os.listdir(level1child)
		for level2dir in level2alldir:
			level2child = os.path.join('%s/%s' % (level1child,level2dir))
			dealallfile(level2child,log)
	log.printlog(1,str(FILESUM))
	log.printlog(1,str(ITEMSUM))

def dealallfile(filepath,log):
	global FILESUM, ITEMSUM
	fileallname = os.listdir(filepath)
	for filename in fileallname:
		filepathandname = os.path.join('%s/%s' % (filepath,filename))
		FILESUM = FILESUM + 1
		log.printlog(1,filepathandname)
		with open(filepathandname,'r') as f:
			fileinfo = json.load(f)
		ITEMSUM = ITEMSUM + len(fileinfo["docs"])
		print(fileinfo)


if __name__ == '__main__':
	basedir = 'datadir'
	dealalldir(basedir)