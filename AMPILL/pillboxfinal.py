import Adafruit_BBIO.GPIO as GPIO
import json
import requests
import urllib
import time
from time import sleep
morning=[]
afternoon=[]
night=[]
morningcount=[]
afternooncount=[]
nightcount=[]
newmorning=[]
med1=0
med2=0
med3=0
for j in range(0,2):
        morning.append(0)
def priscription():
        x=requests.get("https://api.thingspeak.com/channels/293432/feeds.json?results=2")
        content=x.content.decode("utf-8")
        s=json.loads(content)
        f=len(s["feeds"])
        newmorning=[]
        for i in range(0,f):
                newmorning.append(s["feeds"][i]["field1"])
        if(morning[1]!=newmorning[1]):
                morning =[]
                for i in range(0,f):
                        morning.append(s["feeds"][i]["field1"])
                        afternoon.append(s["feeds"][i]["field2"])
                        night.append(s["feeds"][i]["field3"])
                        morningcount.append(s["feeds"][i]["field4"])
                        afternooncount.append(s["feeds"][i]["field5"])
                        nightcount.append(s["feeds"][i]["field6"])
                telegram("YOUR PRISCRIPTION IS UPDATED")
                counttime=0
                med1=0
                med2=0
                med3=0
                return 1
        return 0        
def currenttime():
        x=requests.get("http://time.jsontest.com")
        content=x.content.decode("utf-8")
        s=json.loads(content)
        t=s["time"]
        time = [int(t[0]),int(t[1]),int(t[3]),int(t[4])]
        if t[9] == "P":
                a = time[0] * 10 + time[1] + 18
        else:
                a = time[0] * 10 + time[1] + 6
        if a > 23:
                a = a - 24
        time[0] = int(a/10)
        time[1] = a%10
        return time 


def telegram(text):
	url = "https://api.telegram.org/bot431672019:AAGT3dLEIzNoVLfcycEPrEZVKYFDcQCea8E/sendMessage?text={}&chat_id=401317072".format(text)
	x=urllib.urlopen(url)
	return
 
GPIO.setup("P8_17",GPIO.IN)
GPIO.setup("P8_16",GPIO.IN)
GPIO.setup("P9_12",GPIO.OUT)
GPIO.setup("P8_11",GPIO.OUT)
GPIO.setup("P8_15",GPIO.OUT)
mtime=[2,2,1,5]
aftime=[2,2,1,7]
ntime=[2,1,1,9]
reed=1
reed1=0
counttime=0
a=1
time1=[]
time2=[]
for i in range(0,4):
        time2.append(0)
	time1.append(0)

while True:
        time1=currenttime()
        s=priscription()
        if(s==1):
		if(counttime==0):
                	while reed1==0:
                        	reed1=GPIO.input("P8_16")
                	reed1=0

        elif(s==0):
                if(time1==mtime):
			if(counttime==0):
                        	telegram("YOUE MORNING MEDICINE IS SCHEDULED AT 9:00AM")
                        	telegram("MEDICINE NAME=")
                        	telegram(morning[med1])
                        	telegram("MEDICINE COUNT=")
                        	telegram(morningcount[med1])
                        	med1=med1+1
                                sleep(3)
                        	GPIO.output("P8_15",GPIO.HIGH)
                        	while(reed==1 & a==1):
                                	reed=GPIO.input("P8_17")
                                	time2=currenttime()
					print(time2)
                                	if (time2==[0,0,1,9]):
                                        	a=0
                                        	telegram("YOU MISSED YOUR MORNING MEDICINE")
				while(reed==0):
                                	reed=GPIO.input("P8_17")                
                        	a=1
                        	reed=1
                        	GPIO.output("P8_15",GPIO.LOW)
                        	counttime=counttime+1
                elif(time1==aftime):
			if( counttime==1):
                        	telegram("YOUE AFTERNOON MEDICINE IS SCHEDULED AT 3:00PM")
                        	telegram("MEDICINE NAME=")
                        	telegram(afternoon[med2])
                        	telegram("MEDICINE COUNT=")
                        	telegram(afternooncount[med1])
                        	med2=med2+1
                        	sleep(3)
                        	GPIO.output("P8_11".GPIO.HIGH)
                        	while(reed==1 & a==1):
                                	reed=GPIO.input("P8_17")
                                	time2=currenttime()
                                	if (time2==[2,2,1,8]):
                                        	a=0
                                        	telegram("YOU MISSED YOUR AFTERNOON MEDICINE")
                        	while(reed==0):
                                	reed=GPIO.input("P8_17")                
                        	a=1	
                        	reed=1
                        	GPIO.output("P8_11".GPIO.LOW)
                        	counttime=counttime+1        
                elif(time1==ntime):
			if(counttime==2):
                        	telegram("YOUE NIGHT MEDICINE IS SCHEDULED AT 10:00PM")
                        	telegram("MEDICINE NAME=")
                               	telegram(night[med3])
                               	telegram("MEDICINE COUNT=")
                        	telegram(nightcount[med1])
                        	med3=med3+1
                        	sleep(3)
                        	GPIO.output("P9_12".GPIO.HIGH)
                        	while(reed==1 & a==1):
                                	reed=GPIO.input("P8_17")
                                	time2=currenttime()
                                	if (time2==[2,2,2,0]):
                                        	a=0
                                        	telegram("YOU MISSED YOUR NIGHT MEDICINE")
                        	while(reed==0):
                                	reed=GPIO.input("P8_17")                
                        	a=1
                        	reed=1
                        	GPIO.output("P9_12".GPIO.LOW)
                        	counttime=counttime+1
                elif(counttime>=3):
                        b=priscription()
                        if(b==1):
                                loc=urllib.urlopen("https://dweet.io/dweet/for/0x55b57a7f50?status=yes")
                                telegram("CHECK YOUR AMPILL APP AND BUY YOUR MEDICINES")
                        elif(b==0):
                                if(v==0):
                                        telegram("YOUR PILLS ARE OVER")
                                        v=v+1
                        
                        while(reed==1):
                                reed=GPIO.input("P8_16")
                        counttime=0
                        v=0
                        loc=urllib.urlopen("https://dweet.io/dweet/for/0x55b57a7f50?status=no")
                        telegram("MEDICAL BOX IS UPDATED")
                        med=0
