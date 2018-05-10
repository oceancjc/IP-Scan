# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 09:58:53 2016

@author: junchao chen

Last edit:   20180509    ignore_warning max_cnt for screen capture
"""
import sys,socket,threading
import requests


def get_pub_ip():
    url = r'http://www.trackip.net'
    try:
        r = requests.get(url)
        txt = r.text
        ip = txt[txt.find('title')+6:txt.find('/title')-1]
    except:
        ip = 'Fail to retrive Public IP'
    return ip


not_s = []
def run_thread(prefix,start,stop):
    global not_s
    for i in xrange(start,stop):
        try:
            r = socket.gethostbyaddr(prefix+'.{}'.format(i))
            if '2.7.' in sys.version:    print r[0],r[-1]
            else:                        print(r[0],r[-1])
            not_s.append(i)
        except:
            continue
    


t_s=[]
if '2.7.' in sys.version: 
    print 'Public IP: {}'.format(get_pub_ip())
    baseaddr = raw_input('Input gateway addr\n')
else:
    print( 'Public IP: {}'.format(get_pub_ip()) )                     
    baseaddr = input('Input gateway addr\n')
prefix = '.'.join( baseaddr.split('.')[:-1])

for i in range(10):
    t_s.append( threading.Thread(target=run_thread, args=(prefix,25*i+2,25*i+25+2)) )
    t_s[-1].start()

for i in t_s:    i.join()
    
    
all_ip_s = range(2,252)
for i in not_s:
    if i in all_ip_s:    all_ip_s.remove(i)

if '2.7.' in sys.version:    print 'Available IP:'
else:                        print('Available IP:')
for i in all_ip_s:
    if '2.7.' in sys.version:    print i
    else:                        print(i)