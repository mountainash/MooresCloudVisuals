#!/usr/bin/python

# Just a wrapper for blinky.py in the 'secretapi'

__author__ = 'mountainash'
__version__ = '1.0.0'
__license__ = 'unlicense'

import sys, os, time, subprocess
import settings

if __name__ == '__main__':

	if len(sys.argv) > 1:
		holiday_address = sys.argv[1]		# Pass IP address of Holiday on command line
	elif 'HOLIDAY_ADDRESS' in os.environ:
		holiday_address = os.environ.get('HOLIDAY_ADDRESS')
	else:
		print 'Holiday address required'
		sys.exit(1) # If not there, fail

	subprocess.Popen(['python', 'secretapi/blinky.py', holiday_address])

	while True:
		try:
			time.sleep(0.1)
		except KeyboardInterrupt:
			sys.exit(0)