import os
import time
from time import sleep

def sendMessage():
	os.system('telegram-send "Someones at your door"')
	return

def sendPicture():
	os.system('telegram-send --image down.jpg --caption "Heres the person\'s Image" ')
	return

def sendVoice():
	os.system('telegram-send --file Audio.mp3')
	return

sendMessage()
sleep(5)
sendPicture()
sleep(5)
sendVoice()
sleep(5)
