import urllib
import json
import requests
import time

TOKEN = "421045260:AAFNd4xiQF7XeTCOqg_Ireh41O_EuFyoS1s"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
chat = 445739809
text = "Last message"

def main():
    	last_textchat = (None, None)
	last_update_id = None
	while True:
        	updates = get_updates(last_update_id)
        	if len(updates["result"]) > 0:
        	    	last_update_id = get_last_update_id(updates) + 1
            		echo_all(updates)
        	time.sleep(0.5)
	return

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:
            print(e)

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

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


#x = urllib.urlopen(URL + 'sendMessage?text={}&chat_id={}'.format(text, chat))
#y = urllib.urlopen(URL + '/getupdates&chat_id={}'.format(chat))
#print(json.loads(y))
#print(y.read)

if __name__ == '__main__':
    main()
