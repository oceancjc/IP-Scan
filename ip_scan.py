# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 09:58:53 2016

@author: junchao chen

Last edit:   20180509    ignore_warning max_cnt for screen capture
"""
import sys,socket,threading



def run_thread(prefix,start,stop):
	for i in xrange(start,stop):
		try:
			r = socket.gethostbyaddr(prefix+'.{}'.format(i))
			if '2.7.' in sys.version:    print r[0],r[-1]
			else:                        print(r[0],r[-1])
		except:
			continue
	
t_s=[]

if '2.7.' in sys.version:    baseaddr = raw_input('Input gateway addr\n')
else:                        baseaddr = input('Input gateway addr\n')
prefix = '.'.join( baseaddr.split('.')[:-1])

for i in range(10):
	t_s.append( threading.Thread(target=run_thread, args=(prefix,25*i+2,25*i+25+2)) )
	t_s[-1].start()
