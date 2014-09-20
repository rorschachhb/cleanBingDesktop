#!/usr/bin/python

import urllib2
import xml.etree.ElementTree as ET
import os
import os.path as op
import socket
import sys
import win32api, win32con, win32gui

if sys.platform == 'win32': #if running on windows
	basedir = 'E:\photos\wallpapers'
else: #if running on Linux
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
		if sys.platform == 'win32':
			k = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, 'Control Panel\Desktop', 0, win32con.KEY_ALL_ACCESS)
			currentwallpaper = win32api.RegQueryValueEx(k, 'Wallpaper')[0]
			if currentwallpaper == validpath:
				pass
			else:
				# win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")#2 for tile,0 for center
				# win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
				win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, validpath, 1+2)
			win32api.RegCloseKey(k)
		else:
			os.system('DISPLAY=:0 gsettings set org.gnome.desktop.background picture-uri "%s"' % (validpath))

download_picture()