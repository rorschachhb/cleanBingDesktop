#!/usr/bin/python

import commands
import os
import socket
import sys
import urllib2
import xml.etree.ElementTree as ET

def download_picture():
	basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'wallpapers')
	if not os.path.exists(basedir):
		os.mkdir(basedir)
	validpath = ''
	for i in range(8, -1, -1):
		xmlurl = 'http://az517271.vo.msecnd.net/TodayImageService.svc/HPImageArchive?mkt=zh-cn&idx=%d' % (i)
		#this url supports ipv6, but cn.bing.com doesn't
		try:
			xmlhandle = urllib2.urlopen(xmlurl, timeout = 2)
			xmlresponse = xmlhandle.read()
			root = ET.fromstring(xmlresponse)
		except socket.timeout:
			print 'timeout downloading image information.'
			continue

		datestr = root[0].text
		imgpath = os.path.join(basedir, '%s.jpg' % (datestr))
		if not os.path.exists(imgpath):
			imgurl = root[6].text
			try:
				imgdata = urllib2.urlopen(imgurl, timeout = 2).read()
				if len(imgdata) < 100 * 1024:#if tunet not authorized
					pass
				else:
					imgfile = file(imgpath, 'wb')
					imgfile.write(imgdata)
					imgfile.close()
					validpath = imgpath
			except socket.timeout:
				print 'timeout downloading wallpapers.'
				continue
		else:
			validpath = imgpath
	return validpath

def set_wallpaper(picpath):
	if sys.platform == 'win32':
		import win32api, win32con, win32gui
		k = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, 'Control Panel\Desktop', 0, win32con.KEY_ALL_ACCESS)
		curpath = win32api.RegQueryValueEx(k, 'Wallpaper')[0]
		if curpath == picpath:
			pass
		else:
			# win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")#2 for tile,0 for center
			# win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
			win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, picpath, 1+2)
		win32api.RegCloseKey(k)
	elif sys.platform == 'darwin':
		from appscript import app, mactypes, its
		se = app('System Events')
		desktops = se.desktops.display_name.get()
		# change wallpaper on all monitors
		for d in desktops:
			desk = se.desktops[its.display_name == d]
			desk.picture.set(mactypes.File(picpath))
	else:
		curpath = commands.getstatusoutput('gsettings get org.gnome.desktop.background picture-uri')[1][1:-1]
		if curpath == picpath:
			pass
		else:
			commands.getstatusoutput('DISPLAY=:0 gsettings set org.gnome.desktop.background picture-uri "%s"' % (picpath))


picpath = download_picture()
if picpath != '':
	set_wallpaper(picpath)
