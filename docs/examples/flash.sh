#!/bin/bash

make BOARD=CHRISTMAS_CARD2020 deploy-openocd
openocd -f interface/stlink-v2.cfg -f target/stm32f4x_stlink.cfg -c "init" -c "reset halt"  -c "flash write_image erase init_fs.bin 0x8004000" -c "reset" -c "shutdown"