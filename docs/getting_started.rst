Getting Started
===============

.. contents::
    :depth: 3

An introduction to the Hardware
-------------------------------

The christmas card is a `Micropython <http://micropython.org/>`_ board, with 28 WS2812 LEDs (sometimes called NeoPixels). It has a USB connector, providing it with 5V power. As supplied, it pulls about 20mA so it can run from a decent power bank for quite a while. This depends very much on the script that's running though.

It can be simply used as a christmas decoration, though it can also be a lot more fun than that!

When plugged into a computer, it appears as both a mass storage device, and a serial port. Together, these allow the pattern to be customised.

There is also a temperature sensor on the board. Because why not?!

For more details of the hardware specs, see :doc:`hardware/index`

Connecting to the Board
-----------------------

Plug one end of a USB cable into the board. Plug the other end into your computer. Yep, thats all there is to it. Now read the next sections for details of what you can do with this!

Storage
^^^^^^^^

When connected to a computer, it will show up as a storage device. On this storage device you will find a few files:

* **boot.py** - this is run at startup, to configure the hardware. It doesn't contain much, and you can probably ignore it.
* **main.py** - This contains the script that is run when the board is powered up. It is run after boot.py - this is where the patterns are! As supplied, it contains :doc:`default`
* **pybcdc.inf** This file helps Windows to figure out what to do with the board. You can ignore this.

.. note::
    This is a very small filesystem, containing only about 64Kb of storage. It should only be used to hold Python scripts you want to run on the board. Try not to write to it more often than you need to since the flash memory on the microcontroller may eventually wear out.

Serial
^^^^^^^

The board shows up as a USB serial device. this runs at a baud rate of **115200**

When you first connect to it, you won't see much since it's running the pattern. You can press **Ctrl+C** to interrupt the running script, and get a Micropython prompt. If you want to restart the board from this prompt, you can use press **Ctrl+D**




The LEDs
--------

There are 28 WS2812 LEDs on the board. They are digitally controllable, with each taking three values in the range 0-255 - one for each of red, green and blue.

.. note::
    Values above about 30 are *very* bright, and if enough LEDs are lit at high levels, the board can get very hot quite quickly!

There is a single data connector to each LED, and they are daisy chained together. In effect, they form a shift register. The actual wire protocol has quite exacting timing, since the same line is used for both data and clock. This complexity is taken care of for you by the firmware on the board!

In order to communicate with the LEDs, we firstly need to tell the firmware how many are connected. Since there are 28 on the board, this is the number we will use:

>>> import ws2812
>>> ws2812.init(28)

Now we can set the colours of the LEDs:

>>> ws2812.set_led(4, 15, 20,25) # Set LED 4 to R,G,B values 15,20,25

Taking the Temperature
----------------------

As previously mentioned, there is a temperature sensor on the board. Reading the temperature using it is quite easy:

>>> from lm75 import LM75
>>> from machine import I2C
>>> i2c = I2C(1) # 1 is the hardware ID for the I2C channel the sensor is attached to
>>> lm75 = LM75(i2c)
>>> lm75.get_temperature()
24.75

Firstly, we import the :py:mod:`lm75` module. This is built into the firmware of the board. (If you're really curious, the source for it can be `found on GitHub <https://github.com/mich181189/christmascard2020_micropython/blob/master/drivers/lm75/lm75.py>`_ )
We then import the I2C module (docs for which can be found on the `Micropython I2C docs page <http://docs.micropython.org/en/latest/library/machine.I2C.html>`_) and set up I2C channel 1 (which is the only one broken out on this board) with a speed of 400kHz.
We then create an LM75 object, using the i2c object we just created. Then we can query the temperature.

One thing to keep in mind is that the LM75 sensor is constantly reading the temperature. This actually means it can heat itself up! To avoid this, you can put it into a shutdown mode when you're not using it, then wake it up when you want to start measuring again. Once you have woken it up, you probably want to give it a few hundred milliseconds to read the temperature again, otherwise you will get the old value from before it was shutdown until it re-measures.

>>> lm75.shutdown()
>>> lm75.is_shutdown()
True
>>> lm75.wakeup()
>>> lm75.is_shutdown()
False
>>> # you can now make your measurement after a short delay
>>> lm75.get_temperature()
25.25
