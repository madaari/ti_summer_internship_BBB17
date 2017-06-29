import urllib
import json
import requests

TOKEN = "421045260:AAFNd4xiQF7XeTCOqg_Ireh41O_EuFyoS1s"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
chat = 445739809
text = "Hello"

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

def get_File_Id():
	js = get_updates()
	file_id = js["result"][2]["message"]["voice"]["file_id"]
	print(file_id)


get_File_Id()
