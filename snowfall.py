#!/usr/bin/python

# Original logic from https://github.com/moorescloud/twintrest/blob/master/twinkle.py

__author__ = 'Mark Pesce' # Original
__version__ = '1.01.dev'
__license__ = 'MIT'

import sys, os, time, threading, logging, random
from secretapi.holidaysecretapi import HolidaySecretAPI

class Twinkler(threading.Thread):
	"""If you want to run the Twitter twinkler on its own thread, use this"""

	def start(self, holiday):
		self.matches = []
		self.hol = holiday
		self.r = 0
		self.g = 0
		self.b = 0

		# Initialize the twinkles
		self.twinklevals = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
		0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
		0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
		0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
		0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]

		super(Twinkler, self).start()

	def insert_match(self, msg):
		th = [0, msg] # Array containing position and message
		self.matches.append(th)
		printme('depth %d' % len(self.matches))

	def run(self):
		while True:

			# Do some twinkling. Just a touch.
			j = 0
			while j < self.hol.NUM_GLOBES:
				e = random.uniform(-0.075, 0.075) # Generate a random twinkle value
				m = self.twinklevals[j] + e
				if (m < -0.5):
					m = -0.5
				else:
					if (m > 0.5):
						m = 0.5

				(ar, ag, ab) = self.hol.getglobe(j) # Get the current globe value

				rv = ar * (m + 0.5) # Adjust for range and multiply
				gv = ag * (m + 0.5)
				bv = ab * (m + 0.5)
				self.hol.setglobe(j, int(rv), int(gv), int(bv))
				self.twinklevals[j] = m
				j = j+1

			# Now go through and animate the matches
			for thingy in self.matches:
				pos = thingy[0]
				if pos >= self.hol.NUM_GLOBES:
					self.matches.remove(thingy)
				else:
					(ar, ag, ab) = self.hol.getglobe(pos) # Get the current globe value
					ar = 0x2f
					ag = 0x2f
					ab = 0x2f # Make it all whiterer, but not too bright
					self.hol.setglobe(pos, ar, ag, ab)
					thingy[0] = thingy[0] + 1 # And move the position along
			try:
				self.hol.render()
			except:
				printme('Something failed on the send, not to worry...')
			time.sleep(0.05) # 20hz twinkles

def printme(str):
	"""A print function that can switch quickly to logging"""
	# print(str)
	logging.debug(str)

if __name__ == '__main__':
	logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
	printme('Logging initialized')

	if len(sys.argv) > 1:
		holiday_address = sys.argv[1]		# Pass IP address of Holiday on command line
	elif 'HOLIDAY_ADDRESS' in os.environ:
		holiday_address = os.environ.get('HOLIDAY_ADDRESS')
	else:
		print('Holiday address required')
		sys.exit(1)

	# Startup the twinkler process
	hol = HolidaySecretAPI(addr=holiday_address)
	app = Twinkler()
	app.start(hol)

	while True:
		try:
			time.sleep(random.uniform(0.1, 4))
			app.insert_match('anything')
		except KeyboardInterrupt:
			app.terminate = True
			sys.exit(0)