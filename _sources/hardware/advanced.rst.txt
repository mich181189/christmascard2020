More Advanced Ideas
====================
This page contains some hints/tips/suggestions for things you might want to try if you get bored of the board as is.

Connecting More LEDs
---------------------
There are two test points on the board, TP1 and TP4 that are in the LED chain. *TP1* is the output of *PB0* on the microcontroller. This is probbaly of limited use for extension since while you could tap into it, the LEDs would be in parallel with those on the board, which doesn't sound incredibly useful. *TP4* however, may be more useful. It is the *DOUT* pin of the last LED in the chain. This could be connected to a string of WS2812 LEDs. Then, when you init the module, you could specify the extra count

>>> ws2812.init(28+60)

I really have no idea how many LEDs could be added this way, however the code for driving them uses quite a memory-efficient way of sending the data, so I suspect the number is actually quite high. Memory usage is 3 bytes per LED, plus 48 bytes of scratch space for the actual sending functions.

Connecting I2C Peripherals
--------------------------
There is a pin header on the bottom edge of the board. As well as power and data, this connects to the I2C bus (shared with the LM75 temperature sensor)

+-----------------+
| Pin  | Function |
+======+==========+
| 1    | +5V      |
+------+----------+
| 2    | +3.3V    |
+------+----------+
| 3    | SCL      |
+------+----------+
| 4    | SDA      |
+------+----------+
| 5    | GND      |
+------+----------+


.. warning::
	The SCL and SDA data lines run at 3.3V. 5V devices can be connected, as long as they do not try to pull these lines to the +5V rail - Since I2C devices should only be pulling the line low, this should not be a problem, except that some (many?) breakout boards contain their own pullup resistors to their power rail.

These devices can then be addressed much like any other device. For example, if you were trying to communicate with the LM75B sensor on the board using raw I2C commands:

>>> import machine
>>> i2c = machine.I2C(1, freq=400000) # 400KHz I2C bus on channel 1 (the one broken out on the connector)
>>> result = i2c.readfrom_mem(72, 0x00, 2) # read 2 bytes from register 0 on device with address 72 aka 0x48
>>> result
b'\x17\xa0'

