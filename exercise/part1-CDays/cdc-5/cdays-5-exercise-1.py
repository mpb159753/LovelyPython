#!/bin/python
#coding:utf-8
'''cdays-5-exercise-1.py this year is a leap year or not
    @author: U{shengyan<mailto:shengyan1985@gmail.com>}
    @version:$Id$
'''

import time														#导入time模块

thisyear = time.localtime()[0]										#获取当前年份

if thisyear % 400 == 0 or thisyear % 4 ==0 and thisyear % 100 <> 0:		#判断闰年条件，满足模400为0，或者模4为0但模100不为0
	print 'this year %s is a leap year' % thisyear
else:
	print 'this year %s is not a leap year' % thisyear