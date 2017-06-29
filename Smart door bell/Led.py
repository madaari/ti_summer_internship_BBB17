#!/usr/bin/python
import Adafruit_BBIO.GPIO as GPIO
import time
from time import sleep

GPIO.setup("P9_42",GPIO.OUT)

while True:
	GPIO.output("P9_42",1)
	sleep(0.5)
	GPIO.output("P9_42",0)
        sleep(0.5)

