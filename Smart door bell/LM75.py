#!/usr/bin/python
from Adafruit_I2C imprt Adafruit_I2C
from time import sleep

i2c = Adafruit_I2C(0x48,2)

while True:
	a= i2c.readU16(0)
	a = i2c.reverseByteOrder(a)
	a = a>>7
	a = a*0.5
	print a
	sleep(1)
