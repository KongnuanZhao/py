'''
Created on 2014.7.21
@author: zhaokongnuan
coding:utf-8
'''
#coding=utf-8 
import urllib
link = '<a title="R����&nbsp;��R���Բ�ѯip��γ�ȼ�google��ͼ��ע" target="_blank" href="http://blog.sina.com.cn/s/blog_403aa80a0101ft7r.html">R����&nbsp;��R���Բ�ѯip��γ�ȼ���</a>'
title = link.find(r'<a title')
href =link.find(r'href')
html=link.find(r'html')
url=link[href+6:html+5]
print url
content=urllib.urlopen(url).read()
