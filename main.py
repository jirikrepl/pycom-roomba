from machine import UART
import time
import struct

START = 128
FULL = 132
STOP = 173
CLEAN = 135
DRIVE_PWM = 146
MOTORS_PWM = 144
LEDS = 139
DIGIT_LEDS_ASCII = 164

# this uses the UART_1 default pins for TXD and RXD (``P3`` and ``P4``)
uart = UART(1, 115200)

uart.write(struct.pack("B", START))
uart.write(struct.pack("B", FULL))
time.sleep(0.1)

# uart.write(struct.pack("B", CLEAN))
# time.sleep(.5)
# uart.write(struct.pack("B", CLEAN))

uart.write(struct.pack(">Bbbb", LEDS, 8, 255, 128))

uart.write(struct.pack(">Bbbbb", DIGIT_LEDS_ASCII, 79, 83, 69, 76))

uart.write(struct.pack(">Bbbb", MOTORS_PWM, 0, -64, 0))
# uart.write(struct.pack(">Bbbb", MOTORS_PWM, 0, 0, 127))

speed = 64

uart.write(struct.pack(">Bhh", DRIVE_PWM, speed, -speed))
time.sleep(1)

uart.write(struct.pack(">Bhh", DRIVE_PWM, -speed, speed))
time.sleep(1)

uart.write(struct.pack(">Bbbbb", DIGIT_LEDS_ASCII, 83, 84, 79, 80))
uart.write(struct.pack("B", STOP))
