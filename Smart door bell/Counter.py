import Adafruit_BBIO.GPIO as GPIO
import time
from time import sleep

data = ["P9_16","P9_24","P9_13","P9_11","P9_12","P9_14","P9_15","P9_17"]
sel = ["P9_18","P9_23","P9_26","P9_21"]
value = 0

GPIO.setup("P9_27",GPIO.IN)

for i in data:
        GPIO.setup(i,GPIO.OUT)

for i in sel:
        GPIO.setup(i,GPIO.OUT)

nos = [[1,1,1,1,1,1,0,0],[0,1,1,0,0,0,0,0],[1,1,0,1,1,0,1,0],[1,1,1,1,0,0,1,0],[0,1,1,0,0,1,1,0],
       [1,0,1,1,0,1,1,0],[1,0,1,1,1,1,1,0],[1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,0],[1,1,1,1,0,1,1,0],
       [1,1,1,0,1,1,1,0],[0,0,1,1,1,1,1,0],[1,0,0,1,1,1,0,0],[0,1,1,1,1,0,1,0],[1,0,0,1,1,1,1,0],[1,0,0,0,1,1,1,0]]

def select(value):
	for i in range(0,4):
        	if i == value:
        		GPIO.output(sel[i],1)
        	else:
        		GPIO.output(sel[i],0)
	return

def segment(value):
	val = [0,0,0,0]
	k=3
	while value>=1:
		val[k] = value%16;
		k-=1
		value = int(value/16);
	print(val)
        for i in range(0,4):
                print(nos[val[i]])
                clear()
                for j in range(0,8):
                        GPIO.output(data[j],nos[val[i]][j])
                select(i)
	return

def clear():
        for i in range(0,4):
        	GPIO.output(sel[i],1)
	return

while True:
        a = GPIO.input("P9_27")
        if a==0:
                value+=1
                segment(value)
                while a==0:
                        a = GPIO.input("P9_27")
                        segment(value)
                        sleep(0.009)
        if a==1:
                segment(value)
                sleep(0.009)
                continue
