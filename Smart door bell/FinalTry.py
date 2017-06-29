import json 
import requests
import urllib
import os
import Adafruit_BBIO.GPIO as GPIO
import time
from time import sleep
from time import localtime

TOKEN = "421045260:AAFNd4xiQF7XeTCOqg_Ireh41O_EuFyoS1s"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
chat = 445739809
text = "Wrong Command"

ring = "P9_28"
button = "P9_12"
servo = "P9_16"
enable = "P9_29"
rs = "P9_15"
data = ["P9_31","P9_26","P9_30","P9_42"]

GPIO.setup(ring, GPIO.IN)
GPIO.setup(button, GPIO.IN)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(rs, GPIO.OUT)
for i in data:
    GPIO.setup(i, GPIO.OUT)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

def get_last_update(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    return last_update

def get_last_chat_id_and_text(updates):
    last_update = get_last_update(updates)
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def get_last_chat_id_and_file_id(updates):
    last_update = get_last_update(updates)
    file_id = updates["result"][last_update]["message"]["voice"]["file_id"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (file_id, chat_id)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    result = get_url(url)
    return

def check_text(updates, no):
    try:
        text = updates["result"][no]["message"]["text"]
        return 1
    except:
        return 0

def check_voice(updates, no):
    try:
        voice = updates["result"][no]["message"]["voice"]
        return 1
    except:
        return 0

def check_file_type(updates, no):
    n = check_text(updates,no)
    if n == 1:
        return 0
    if n == 0:
        n = check_voice(updates, no)
        if n == 1:
            return 1
        else:
            return 2
    
def get_voice_path(updates):
    (file_id, chat_id) = get_last_chat_id_and_file_id(updates)
    url = URL + "getFile?file_id={}".format(file_id)
    jsfinal = get_json_from_url(url)
    file_path = jsfinal["result"]["file_path"] 
    #print(file_path)
    return (file_id, file_path)
    
def voice_download(updates):
    (voice_id, voice_path) = get_voice_path(updates)
    update = URL + "getUpdates"
    urllib.urlopen(update)
    ids = URL + "getFile?file_id={}".format(voice_id)
    urllib.urlopen(ids)
    path = URL + "{}".format(voice_path)
    urllib.urlretrieve(path, "file.wav")
    return

def voice_play():
    os.system("sudo su")
    os.system("aplay -D plughw:1 file.wav")

def alert_message():
    #take image
    a = localtime()
    send_message("There's someone at your door", chat)
    time = "At " + str(a[3]) + ":" + str(a[4]) + ":" + str(a[5]) + " on " + str(a[2]) + ":" + str(a[1]) + ":" + str(a[0])
    send_message(time, chat)
    send_message("Heres the pic of the person", chat)
    os.system("telegram-send --file down.jpg")
    send_message("Do you know this person? Reply with Yes or No.", chat)
    return

update = get_updates()
last_message = get_last_update(update)
a=localtime()
check = a[4] + 10
if check > 60:
    check - 60
while 1:
    #button_value = GPIO.input(button)
    button_value = 1
    ring_value = GPIO.input(ring)
    if button_value == 1:
        count = 0
        while button_value == 1:
            alert_message()
            print(0)
            reply = 1
            while reply == 1:
                print(1)
                update = get_updates()
                no = get_last_update(update)
                if no == last_message:
                    print(2)
                    continue
                elif no > last_message:
                    print(3)
                    nos = no
                    file = check_file_type(update, no)
                    if file == 0:
                        print(4)
                        (message, chat_id) = get_last_chat_id_and_text(update)
                        if message == "Yes":
                            send_message("Do yo want to send any voice greeting?  Reply with Yes or No.", chat)
                            replied = 1
                            while replied == 1:
                                update = get_updates()
                                no = get_last_update(update)
                                if no == nos:
                                    continue
                                elif no > nos:
                                    file = check_file_type(update, no)
                                    if file == 0:
                                        (messages, chat_id) = get_last_chat_id_and_text(update)
                                        if messages == "Yes":
                                            number = no
                                            update = get_updates()
                                            no = get_last_update(update)
                                            if no == number:
                                                continue
                                            elif no > number:
                                                file = check_file_type(update, no)
                                                if file == 1:
                                                    voice_download(update)
                                                    send_message("Opening the gate", chat)
                                                    #display("WELCOME")
                                                    voice_play()
                                                    gate_open()
                                                else:
                                                    send_message(text, chat)
                                                    send_message("Simply opening the gate", chat)
                                                    #display("WELCOME")
                                                    gate_open()
                                                replied = 0
                                            else:
                                                number = no
                                        elif messages == "No":
                                            send_message("Opening the gate", chat)
                                            gate_open()
                                            replied = 0
                                        else:
                                            send_message(text, chat)
                                            send_message("Simply opening the gate", chat)
                                            #display("WELCOME")
                                            gate_open()
                                            replied = 0
                                            reply = 0
                                    else:
                                        send_message(text, chat)
                                        send_message("Simply opening the gate", chat)
                                        #display("WELCOME")
                                        gate_open()
                                        replied = 0
                                        reply = 0
                                else:
                                    nos = no
                        elif message == "No":
                            send_message("Opening the gate", chat)
                            gate_open()
                            reply = 0
                        else:
                            send_message(text, chat)
                    else:
                        send_message(text, chat)
                else:
                    last_message = no
                last_message = no
    elif ring_value == 1:
        print(1)
        #display("The other button first")
    else:
        a=localtime()
        if check < a[4]:
            update = get_updates()
            no = get_last_update(update)
            if no == last_message:
                continue
            else:
                last_message = no
            check = a[4] + 10
            if check > 60:
                check - 60
