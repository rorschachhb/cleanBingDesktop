#!/usr/bin/python

import urllib2
import xml.etree.ElementTree as ET
import os
import os.path as op
import socket

basedir = '/tmp/'

def download_picture():
	validpath = ''
	for i in range(8, -1, -1):
		xmlurl = 'http://az517271.vo.msecnd.net/TodayImageService.svc/HPImageArchive?mkt=zh-cn&idx=%d' % (i)
		try:
			xmlhandle = urllib2.urlopen(xmlurl, timeout = 2)
			xmlresponse = xmlhandle.read()
			root = ET.fromstring(xmlresponse)
		except socket.timeout:
			print 'timeout'
			continue

		datestr = root[0].text
		imgpath = op.join(basedir, '%s.jpg' % (datestr))
		if not op.exists(imgpath):
			imgurl = root[6].text
			try:
				imgdata = urllib2.urlopen(imgurl, timeout = 2).read()
				imgfile = file(imgpath, 'wb')
				imgfile.write(imgdata)
				imgfile.close()
				validpath = imgpath
			except socket.timeout:
				print 'timeout'
				continue 
		else:
			validpath = imgpath
	
	if validpath != '':
		os.system('gsettings set org.gnome.desktop.background picture-uri "%s"' % (validpath))

download_picture()