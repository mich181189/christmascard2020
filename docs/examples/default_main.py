import ws2812
import utime
import random
from lm75 import LM75
from machine import I2C

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
	pattern_twinkle(leds)

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
	pattern_twinkle(leds)

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
	pattern_twinkle(leds)

def pattern4():
	import urandom
	while True:
		for i in range(28):
			ws2812.set_led(i, urandom.randint(0,15),urandom.randint(0,15),urandom.randint(0,15))
		utime.sleep_ms(200)


print("Starting temperature was " + str(start_temperature))
pattern4()