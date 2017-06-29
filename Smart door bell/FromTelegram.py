import json 
import requests
import urllib

TOKEN = "421045260:AAFNd4xiQF7XeTCOqg_Ireh41O_EuFyoS1s"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
chat = 445739809
text = "Hello from Beagle Bone"

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:
            print(e)
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

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def get_last_chat_id_and_file_id(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    file_id = updates["result"][last_update]["message"]["voice"]["file_id"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (file_id, chat_id)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    result = get_url(url)
    return

def check_file_type():
    js = get_updates()
    last_update = len(js["result"]) - 1
    return

def get_voice_path():
    js = get_updates()
    (file_id, chat_id) = get_last_chat_id_and_file_id(js)
    url = URL + "getFile?file_id={}".format(file_id)
    jsfinal = get_json_from_url(url)
    file_path = jsfinal["result"]["file_path"] 
    print(file_path)
    return (file_id, file_path)
    
def voice_download():
    (voice_id, voice_path) = get_voice_path()
    update = URL + "getUpdates"
    urllib.urlopen(update)
    id = URL + "getFile?file_id={}".format(voice_id)
    urllib.urlopen(id)
    path = URL + "{}".format(voice_path)
    urllib.urlretrieve(path, "file.wav")
    return

#text, chat = get_last_chat_id_and_text(get_updates())
#send_message(text, chat)
voice_download()
#check_file_type()
