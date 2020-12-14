Christmas Card Hardware
========================

.. rubric:: The hardware consists of:

* STM32F401RET6 Microcontroller
* 28 WS2812B LEDs
* LM75B i2c Temperature Sensor
* A USB Connector

The microcontroller was chosen as the cheapest one available on `JLCPCB's SMT assembly service <https://jlcpcb.com/smt-assembly>`_ with decent Micropython support. This entire project was desgned in a bit of a rush 😅 

.. image:: /images/christmas-card-render.png
	:align: center
	:alt: Render of PCB

.. rubric:: Some Links

* The Schematic `is available as a PDF </_static/schematic_1_0.pdf>`_ 
* The hardware design is available on `Github <https://github.com/mich181189/christmascard2020>`_
  * If you want to play with  the hardware design, it was designed in `KiCad <https://kicad.org/>`_
* The board runs `Micropython <http://micropython.org/>`_
