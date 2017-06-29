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

def test(js, n):
	try:
		x = js["result"][n]
		return 1
	except:
		return 0

def get_last_id(js):
	n = 0
	x = test(js, n)
	while(x):
		n+=1
		x = test(js, n)
	n-=1
	return n

def get_File_Id():
	js = get_updates()
	file_id = js["result"][get_last_id(js)]["message"]["voice"]["file_id"]
	print(file_id)


get_File_Id()
