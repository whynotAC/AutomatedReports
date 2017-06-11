#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
	with open('Error.log','w') as w:
		with open('Scrapylog.log','r') as f:
			for line in f.readlines():
				if line.find('INFO Other') != -1:
					w.write(line)