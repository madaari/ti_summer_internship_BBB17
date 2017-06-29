import argparse
import json
import os
from subprocess import call

import requests

#from secret import key

parser = argparse.ArgumentParser(description="Send the daily Astronomy Picture of the Day.")
parser.add_argument("--config", help="/home/debian/Desktop/Abhishek/telegram-send/setup.cfg", type=str)
args = parser.parse_args()
conf_command = ["--config", args.config] if args.config else []
print(conf_command)
#call(["telegram-send", "--configure"])
call(["telegram-send", "--image", "down.jpg"] + conf_command)
