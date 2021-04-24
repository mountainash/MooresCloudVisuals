#!/usr/bin/python

# The ants came marching 2 by 2

__author__ = 'mountainash'
__version__ = '1.01.dev'
__license__ = 'unlicense'

import sys, os, time, threading, logging, random
import settings
from secretapi.holidaysecretapi

class Spin(threading.Thread):
	"""Moves along the lights"""

	def start(self, holiday, passed1 = 255, passed2 = 255):
		self.hol = holiday
		self.color1 = passed1
		self.color2 = passed2
		self.r = 0
		self.g = 0
		self.b = 0

		# Define a light [red, green, blue, opacity]
		self.lights =

		# Initialize the light holder
		self.twinklevals = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
		0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
		0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
		0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
		0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]

		super(Spin, self).start()

	def run(self):
		while True:

			pos = 0
			while pos < self.hol.NUM_GLOBES:
				e = random.uniform(-0.075, 0.075) # generate a random twinkle value
				m = self.twinklevals[pos] + e
				if (m < -0.5):
					m = -0.5
				else:
					if (m > 0.5):
						m = 0.5

				(ar, ag, ab) = self.hol.getglobe(pos) # Get the current globe value
				print(ar, ag, ab)
				rv = ar + m
				gv = ag + m
				bv = ab + m
				self.hol.setglobe(pos, int(rv), int(gv), int(bv))
				self.twinklevals[pos] = m
				pos = pos + 1

			self.hol.render()
			time.sleep(0.05)  # 20hz twinkles
			time.sleep(1.05) # 20hz twinkles

			# # Now go through and animate the matches
			# for thingy in self.matches:
			# 	pos = thingy[0]
			# 	if pos >= self.hol.NUM_GLOBES:
			# 		self.matches.remove(thingy)
			# 	else:
			# 		(ar, ag, ab) = self.hol.getglobe(pos) # Get the current globe value
			# 		ar = 0x2f
			# 		ag = 0x2f
			# 		ab = 0x2f # Make it all whiterer, but not too bright
			# 		self.hol.setglobe(pos, ar, ag, ab)
			# 		thingy[0] = thingy[0] + 1 # And move the position along
			# try:
			# 	self.hol.render()
			# except:
			# 	print("Something failed on the send, not to worry...")
			# time.sleep(0.05) # 20hz twinkles

if __name__ == '__main__':

	if len(sys.argv) > 1:
		holiday_address = sys.argv[1] # pass address of Holiday on command line
	elif 'HOLIDAY_ADDRESS' in os.environ:
		holiday_address = os.environ.get('HOLIDAY_ADDRESS') # get the address from the .env file
	else:
		print 'Holiday address required'
		sys.exit(1) # fail

	hol = HolidaySecretAPI(addr=holiday_address)
	app = Spin()
	app.start(hol)

	while True:
		try:
			time.sleep(0.1)
		except KeyboardInterrupt:
			sys.exit(0)