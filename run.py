#!/usr/bin/python

import urllib2
import xml.etree.ElementTree as ET

xmlurl = 'http://az517271.vo.msecnd.net/TodayImageService.svc/HPImageArchive?mkt=zh-cn&idx=0'
xmlhandle = urllib2.urlopen(xmlurl)
xmlresponse = xmlhandle.read()
root = ET.fromstring(xmlresponse)
imgurl = root[6].text
imgdata = urllib2.urlopen(imgurl).read()
imgpath = 'desktop.jpg'
imgfile = file(imgpath, 'wb')
imgfile.write(imgdata)
imgfile.close()