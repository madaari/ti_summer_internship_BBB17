import json 
import requests
import urllib
import os
import Adafruit_CharLCD as LCD
import Adafruit_BBIO.GPIO as GPIO
import argparse
from time import sleep
from time import localtime
from subprocess import call


TOKEN = "320429258:AAE6F96ml5SAR7zOx1IeF1Nqf2lwv1hTm2E"
URL = "http://api.telegram.org/bot{}/".format(TOKEN)
down = "http://api.telegram.org/file/bot{}/".format(TOKEN)
chat = 426960508
text = "Wrong Command"

time = 10

lcd_rs        = "P8_15"
lcd_en        = "P8_30"
lcd_d4        = "P8_32"
lcd_d5        = "P8_25"
lcd_d6        = "P8_31"
lcd_d7        = "P8_41"
lcd_backlight = "P8_7"
lcd_columns = "16"
lcd_rows    = "2"

ring = "P9_29"
button = "P9_11"
servo = "P9_16"

GPIO.setup(ring, GPIO.IN)
GPIO.setup(button, GPIO.IN)
GPIO.setup(servo, GPIO.OUT)

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.clear()

def display(message):
    lcd.message(message)
    return
    
def configure():
    parser = argparse.ArgumentParser(description="Send the daily Astronomy Picture of the Day.")
    parser.add_argument("--config", help="configuration file for telegram-send", type=str)
    args = parser.parse_args()
    conf_command = ["--config", args.config] if args.config else []
    call(["telegram-send", "--configure"])
    call(["telegram-send", "--image", "down.jpg"] + conf_command)
    return

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
    path = down + "{}".format(voice_path)
    urllib.urlretrieve(path, "file.wav")
    return

def voice_play():
    os.system("mplayer file.wav")

def voice_send():
    count = 0
    while count < 20000:
        ring_value = GPIO.input(ring)
        if ring_value == 1:
            os.system("sudo arecord -D plughw:1 -c 1 -f cd -t wav request.wav")
            os.system("telegram-send --file request.wav")
            return
        else:
            count= count+1
    if count > 19999:
       # send_message("He has not recorded his voice", chat)
        return

def alert_message():
    os.system("fswebcam file.jpg")
    a = localtime()
    send_message("There's someone at your door", chat)
    time = "At " + str(a[3]) + ":" + str(a[4]) + ":" + str(a[5]) + " on " + str(a[2]) + ":" + str(a[1]) + ":" + str(a[0])
    send_message(time, chat)
    send_message("Heres the pic of the person", chat)
    os.system("telegram-send --image file.jpg")
#    display("Please record voice Max 10sec")
    voice_send()
    return

def opengate():
    
    return

update = get_updates()
last_message = get_last_update(update)
a=localtime()
check = a[4] + 10
if check > 60:
    check - 60
#configure()
while 1:
    button_value = GPIO.input(button)
    ring_value = GPIO.input(ring)
    print(button_value)
    if button_value == 1:
        alert_message()
        send_message("Do you know this person? Reply with Yes or No", chat)
        reply = 1
        count = 0
        while (reply == 1 and count < 100):
            update = get_updates()
            no = get_last_update(update)
            if no == last_message:
                continue
            elif no > last_message:
                file = check_file_type(update, no)
                if file == 0:
                    (message, chat_id) = get_last_chat_id_and_text(update)
                    if message == "Yes":
                        replied = 1
                        counter = 0
                        nos = no
                        send_message("Do you want to send any greeting or not? Reply with Yes or No", chat)
                        while (replied == 1 and counter < 100):
                            update = get_updates()
                            no = get_last_update(update)
                            if no == nos:
                                continue
                            elif no > nos:
                                file = check_file_type(update, no)
                                if file == 0:
                                    (message, chat_id) = get_last_chat_id_and_text(update)
                                    if message == "Yes":
                                        send_message("Send your voice message", chat)
                                        replies = 1
                                        n = no
                                        counts = 1
                                        while (replies == 1 and counts < 100):
                                            update = get_updates()
                                            no = get_last_update(update)
                                            if no == n:
                                                continue
                                            elif no > n:
                                                file = check_file_type(update, no)
                                                if file == 1:
                                                    voice_download(update)
                                                    voice_play()
                                                    display("Welcome")
                                                    send_message("Opening the gate", chat)
                                                    replies = 0
                                                else:
                                                    send_message("Wrong Command", chat)
                                                    display("Welcome")
                                                    send_message("Simply opening the gate", chat)
                                                    replies = 0
                                            else:
                                                n = no
                                            counts = counts + 1
                                        #open_gate()
                                    else:
                                        display("Welcome")
                                        send_message("Opening the gate", chat)
                                        #open_gate()
                                else:
                                    send_message(text, chat)
                                    send_message("Simply opening the gate", chat)
                                    display("Welcome")
                                    #open_gate()
                                replied = 0
                                reply = 0
                            else:
                                nos = no
                            counter = counter + 1
                        last_message = no
                        if counter > 99:
                            send_Message("Request Time-Out")
                            display("Welcome")
                            send_message("Simply opening the gate",chat)
                            #open_gate()
                            reply = 0
                    elif message == "No":
                        display("You are not allowed. Cont: 9717572746")
                        reply = 0
                    else:
                        send_message(text, chat)
                else:
                    send_message(text, chat)
            else:
                last_message = no
            count = count + 1
        last_message = no
        if count > 99:
            print(1)
            display("There is no reply.Cont: 9717572746")
        sleep(5)
    elif ring_value == 1:
        print(1)
        display("The other button first")
        sleep(5)
    else:
        a=localtime()
        if check < a[4]:
            update = get_updates()
            no = get_last_update(update)
            if no == last_message:
                continue
            else:
                last_message = no
            check = a[4] + time
            if check > 60:
                check - 60
    lcd.clear()
