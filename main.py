from machine import UART
import time
import struct

START = 128
FULL = 132
STOP = 173
CLEAN = 135

# this uses the UART_1 default pins for TXD and RXD (``P3`` and ``P4``)
uart = UART(1, 115200)

uart.write(struct.pack("b", START))

uart.write(struct.pack("b", FULL))

uart.write(struct.pack("b", CLEAN))

time.sleep(.5)

uart.write(struct.pack("b", CLEAN))

uart.write(struct.pack("b", STOP))

print('done')
