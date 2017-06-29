import Adafruit_BBIO.GPIO as GPIO
import time

data = ["P9_16","P9_24","P9_13","P9_11","P9_12","P9_14","P9_15","P9_17"]
sel = ["P9_18","P9_23","P9_26","P9_21"]

for i in data:
	GPIO.setup(i, GPIO.OUT)

for i in sel:
	GPIO.setup(i, GPIO.OUT)

nos = [[1,1,1,1,1,1,0,0],[0,1,1,0,0,0,0,0],[1,1,0,1,1,0,1,0],[1,1,1,1,0,0,1,0],[0,1,1,0,0,1,1,0],
       [1,0,1,1,0,1,1,0],[1,0,1,1,1,1,1,0],[1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,0],[1,1,1,1,0,1,1,0]]

def select(value):
    for i in range(0,4):
        if i == value:
            GPIO.output(sel[i],1)
        else:
            GPIO.output(sel[i],0)
    return

def segment(value):
    for i in range(0,8):
        GPIO.output(data[i],nos[value][i])
    return

def clear():
    for i in range(0,8):
        GPIO.output(data[i],0)
    return

while True:
    for i in range(0,4):
        select(i)
        for j in range(0,10):
            segment(j)
            time.sleep(1)
