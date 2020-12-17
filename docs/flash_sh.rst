My Board Flashing Script
==========================

This is the script I used to flash the board. It was run from ports/stm32 in the Micropython source tree `(GitHub Link) <https://github.com/mich181189/christmascard2020_micropython>`_

It makes use of an initial filesystem I created by copying the files to a board, then dumping the relevant section of flash. I then used the *fatlabel* utility to relabel it as CCARD2020

I used an STLink V2 for the flashing.

.. literalinclude:: examples/flash.sh