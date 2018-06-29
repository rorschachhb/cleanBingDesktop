# cleanBingDesktop

This project downloads wallpapers fron Microsoft's Bing Desktop server and set the latest one as your desktop background. I started this to get rid of some stupid bugs of the official BingDesktop.

## Run-time system

* Ubuntu-based Linux distributions. (I guess other Linux distributions will do)
* Windows 64bit. (I guess 32bit Windows will do)

## Requirements

* python 2.7
* pywin32(for Windows)
* appscript(for Mac)

## How to run

If you only want to do it once, simply run the script.
On Linux:

	./change_wallpaper.py

On Windows:

	python change_wallpaper.py

If you want the script to run automatically on Linux, use the cron daemon.

	crontab -e

then add the following lines to crontab.

	#m	h		dom 	mon 	dow		command
	0	*/2 	*		*		* 		python /<some absolute path>/change_wallpaper.py

restart cron daemon.

	sudo restart cron

and the cript will check for latest wallpapers every two hours.

If you want the script to run automatically on Windows, add the following command into Windows Task Scheduler.

	<some absolute path>\run.bat

and the script will run at the time you set.
