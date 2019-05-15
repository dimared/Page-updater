#*- coding: utf-8 -*-
import json
import requests
import time


def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(URL + 'sendMessage', data=params)
    return response


# Be careful with encoding
with open("initial.json", "r", encoding='utf-8') as initial:
    data = json.load(initial)

URL = "https://api.telegram.org/bot" + data["token"] + "/"
CHAT_ID = data["admin_id"]

LINK = data["link"]
TEXT = "Обновление на сайте: " + LINK
ANCHOR_LEFT = data["anchor_left"] 
ANCHOR_RIGHT = data["anchor_right"] 
target = "-"

while True:
    req = requests.get(LINK)
    html = req.text

    # positions
    pos_left = html.find(ANCHOR_LEFT)
    pos_right = pos_left + html[pos_left:].find(ANCHOR_RIGHT)

    old_target = target
    target = html[pos_left:pos_right]

    if target != old_target and old_target != None:
        send_mess(CHAT_ID, TEXT)

    time.sleep(data["period"])
