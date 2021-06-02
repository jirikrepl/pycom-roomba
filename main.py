from machine import UART
import time
import struct
import binascii

START = 128
FULL = 132
STOP = 173
CLEAN = 135
DRIVE_PWM = 146

# this uses the UART_1 default pins for TXD and RXD (``P3`` and ``P4``)
uart = UART(1, 115200)

uart.write(struct.pack("B", START))
uart.write(struct.pack("B", FULL))
time.sleep(0.1)

# uart.write(struct.pack("B", CLEAN))
# time.sleep(.5)
# uart.write(struct.pack("B", CLEAN))

speed = 64

uart.write(struct.pack(">Bhh", DRIVE_PWM, speed, -speed))
time.sleep(1)

uart.write(struct.pack(">Bhh", DRIVE_PWM, -speed, speed))
time.sleep(1)

uart.write(struct.pack("B", STOP))

print('done')
