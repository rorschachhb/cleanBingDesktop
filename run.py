#!/usr/bin/python

import urllib2
import xml.etree.ElementTree as ET
import os.path as op

for i in range(8, -1, -1):
	xmlurl = 'http://az517271.vo.msecnd.net/TodayImageService.svc/HPImageArchive?mkt=zh-cn&idx=%d' % (i)
	xmlhandle = urllib2.urlopen(xmlurl)
	xmlresponse = xmlhandle.read()
	root = ET.fromstring(xmlresponse)

	datestr = root[0].text
	imgpath = '%s.jpg' % (datestr)
	if not op.exists(imgpath):
		imgurl = root[6].text
		imgdata = urllib2.urlopen(imgurl).read()
		imgfile = file(imgpath, 'wb')
		imgfile.write(imgdata)
		imgfile.close()