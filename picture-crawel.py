# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:29:36 2017

@author: caibo
"""

#coding=utf-8
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    html=html.decode('utf-8')
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,r'D:\tmp\%s.jpg' % x)
        x+=1


html = getHtml("http://tieba.baidu.com/p/2460150866")

print (getImg(html))