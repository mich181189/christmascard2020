import ws2812
import utime
from lm75 import LM75
from machine import I2C
import random

i2c = I2C(1, freq=400000)
lm75 = LM75(i2c)

# take a reading, then shutdown the LM75 so it doesn't heat itself up
lm75.wakeup()
utime.sleep_ms(300)
start_temperature = lm75.get_temperature()
lm75.shutdown()

# Start the WS2812 handling stuff
ws2812.init(28)

def pattern_twinkle(starting):
	# The base LED patterns
	leds = starting

	# create the state object
	class State:
		twinkle_state = 0
		twinkle_led = 0
	state = State()

	# set the LEDs to their starting pattern
	for i in range(0,len(leds)):
		(r,g,b) = leds[i]
		ws2812.set_led(i, r,g,b)

	def twinkle_next(state):
		if state.twinkle_state == 0:
			(r,g,b) = leds[state.twinkle_led]
			ws2812.set_led(state.twinkle_led, r,g,b)
			state.twinkle_led = random.randint(0, len(leds)-1)
			(r,g,b) = leds[state.twinkle_led]
			if r > 0:
				r = r + 10
			if g > 0:
				g = g + 10
			if b > 0:
				b = b + 10
			ws2812.set_led(state.twinkle_led, r,g,b)
			state.twinkle_state = state.twinkle_state + 1
		elif state.twinkle_state == 1:
			(r,g,b) = leds[state.twinkle_led]
			if r > 0:
				r = r + 15
			if g > 0:
				g = g + 15
			if b > 0:
				b = b + 15
			ws2812.set_led(state.twinkle_led, r,g,b)
			state.twinkle_state = state.twinkle_state + 1
		elif state.twinkle_state == 2:
			(r,g,b) = leds[state.twinkle_led]
			if r > 0:
				r = r + 10
			if g > 0:
				g = g + 10
			if b > 0:
				b = b + 10
			ws2812.set_led(state.twinkle_led, r,g,b)
			state.twinkle_state = 0
		
		
	while True:
		utime.sleep_ms(100)
		twinkle_next(state)

def pattern_fade(starting_leds):
	class LEDState:
		STATE_WAIT = 0
		STATE_RAMP_UP = 1
		STATE_RAMP_DOWN = 2

		def __init__(self, i, r, g, b):
			self.i = i
			self.wait_count = random.randint(0, 35)
			self.base_r = r
			self.base_g = g
			self.base_b = b
			self.current_state = 0
			self.step = 0

		def run(self):
			if self.current_state == self.STATE_RAMP_UP:
				self.step += 1
				if self.step >= 7:
					self.current_state = self.STATE_RAMP_DOWN
			elif self.current_state == self.STATE_RAMP_DOWN:
				self.step -= 1
				if self.step <= 0:
					self.current_state = self.STATE_WAIT
					self.wait_count = 0
			else:
				# the aim of thisis to make something that looks sort of chaotic
				if self.wait_count < (75 - 2*(self.i % 3) + (self.i % 2) - (self.i % 4)) - self.i:
					self.wait_count += 1
					#ws2812.set_led(self.i, 0,0,0)
				else:
					self.current_state = self.STATE_RAMP_UP
			r = 0
			g = 0
			b = 0
			if self.base_r > 0:
				r = self.base_r	 + self.step*2 - 5
			if self.base_g > 0:
				g = self.base_g + self.step*2 - 5
			if self.base_b > 0:
				b = self.base_b + self.step*2 - 5
			ws2812.set_led(self.i, int(r), int(g), int(b))

	leds = []
	i = 0
	for l in starting_leds:
		r,g,b = l
		leds.append(LEDState(i, r, g, b))
		i += 1

	while True:
		for l in leds:
			l.run()
		utime.sleep_ms(50)


def pattern1():
	leds = [
		(10,10,0),
		(0,10,0),(0,10,0),
		(0,10,0),(0,10,0),(0,10,0),
		(10,0,0),(0,10,0),(0,10,0),(10,0,0),
		(0,10,0),(0,10,0),(0,10,0),
		(10,0,0),(0,10,0),(0,10,0),(10,0,0),
		(0,10,0),(0,10,0),(0,10,0),(0,10,0),(0,10,0),
		(10,0,0),(0,10,0),(0,10,0),(0,10,0),(0,10,0),(10,0,0),
		]
	if int(start_temperature * 100) % 2 == 0:
		pattern_twinkle(leds)
	else:
		pattern_fade(leds)

def pattern2():
	leds = [
		(10,10,0),
		(0,0,10),(0,0,10),
		(0,0,10),(0,0,10),(0,0,10),
		(10,0,10),(0,0,10),(0,0,10),(10,0,10),
		(0,0,10),(0,0,10),(0,0,10),
		(10,0,10),(0,0,10),(0,0,10),(10,0,10),
		(0,0,10),(0,0,10),(0,0,10),(0,0,10),(0,0,10),
		(10,0,10),(0,0,10),(0,0,10),(0,0,10),(0,0,10),(10,0,10),
		]
	if int(start_temperature * 100) % 2 == 0:
		pattern_twinkle(leds)
	else:
		pattern_fade(leds)

def pattern3():
	leds = [
		(10,10,0),
		(10,0,0),(10,0,0),
		(10,0,0),(10,0,0),(10,0,0),
		(0,10,5),(10,0,0),(10,0,0),(0,10,5),
		(10,0,0),(10,0,0),(10,0,0),
		(0,10,5),(10,0,0),(10,0,0),(0,10,5),
		(10,0,0),(10,0,0),(10,0,0),(10,0,0),(10,0,0),
		(0,10,5),(10,0,0),(10,0,0),(10,0,0),(10,0,0),(0,10,5),
		]
	if int(start_temperature * 100) % 2 == 0:
		pattern_twinkle(leds)
	else:
		pattern_fade(leds)

def pattern4():
	while True:
		for i in range(28):
			ws2812.set_led(i, random.randint(0,15),random.randint(0,15),random.randint(0,15))
		utime.sleep_ms(300)

random.seed()

print("Starting temperature is %f" % (start_temperature,))

if start_temperature < 20:
	pattern2()
elif start_temperature < 25:
	pattern1()
elif start_temperature < 26:
	pattern4()
else:
	pattern3()
