from machine import UART
# import time
import struct

# this uses the UART_1 default pins for TXD and RXD (``P3`` and ``P4``)
uart = UART(1, 115200)

uart.write(struct.pack("b", 128))

uart.write(struct.pack("b", 135))

print('done')
