#cleanBingDesktop

This project downloads 9 latest wallpapers fron Microsoft's Bing Desktop server and set the latest one as your desktop background.

##Run-time system

* Ubuntu-based Linux distribution

##Requirements

* python 2.7

##How to run

If you only want to do it once, simply run the script

	./change_wallpaper.py

If you want the script to automatically, use the cron daemon

	crontab -e

add the following lines to crontab

	#m	h		dom 	mon 	dow		command
	0	*/2 	*		*		* 		python /<some absolute path>/change_wallpaper.py

restart cron daemon

	sudo restart cron

and the cript will check for latest wallpapers every two hours.