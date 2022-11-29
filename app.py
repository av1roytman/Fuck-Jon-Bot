import json
import os
import time
import re
import random

import requests

from flask import Flask, request

messageUrl = 'https://api.groupme.com/v3/bots/post'
baseUrl = 'https://api.groupme.com/v3'
tokenEnding = '?token=' + os.getenv('ACCESS_TOKEN')
toryId = '95539658'
isaacId = '104833868'

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "hey", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)

    if data['sender_id'] == toryId:
        randNum = random.randint(0, 2)
        match randNum:
            case 0:
                msg = 'Bro, you jerk off in 3rd Head even though you got your own rack... That\'s Sad.'
            case 1:
                msg = 'You\'re really awesome Tory!'
            case _:
                msg = 'Sober Up Bud'
        sendMessage(os.getenv('GROUPME_BOT_ID'), msg)
    elif data['sender_id'] == isaacId:
        randNum = random.randint(0, 12)
        match randNum:
            case 0:
                msg = 'I clearly took it too easy on you Isaac...'
            case 1:
                msg = 'Man I really miss that Broomstick'
            case 2:
                msg = 'Aren\'t you adopted?'
            case 3:
                msg = 'The Police are looking for you Isaac'
            case 4:
                msg = 'Hawkins called. They found your weed'
            case 5:
                msg = 'Uncle Sherwin misses you Isaac'
            case 6:
                msg = 'Didn\'t you impregnate that Blind Pig Bartender?'
            case _:
                msg = 'Phi Delta Uh...'

        sendMessage(os.getenv('GROUPME_BOT_ID'), msg)

    if re.match(r'zirkle', data['text'].lower()):
        msg = 'Please do not talk negatively of the Mesiah Zirkle Himself'
        sendMessage(os.getenv('GROUPME_BOT_ID'), msg)

    if re.match(r'@mod', data['text'].lower()):
        msg = 'Don\'t @ the Mod Bitch'
        sendMessage(os.getenv('GROUPME_BOT_ID'), msg)
        time.sleep(2)
        removeUser(group_id=data['group_id'], user_id=data['sender_id'])

    return "ok", 200


def sendMessage(bot_id, text):
    messageData = {
        "bot_id": bot_id,
        "text": text
    }

    response = requests.post(messageUrl, json=messageData)


# /groups/:group_id/members/:membership_id/remove
def removeUser(group_id, user_id):
    member_id = getMemberId(group_id, user_id)
    removeUrl = baseUrl + '/groups/' + group_id + '/members/' + member_id + '/remove' + tokenEnding
    print(removeUrl)
    response = requests.post(removeUrl)
    print(response.json())


def getMemberId(group_id, user_id):
    response = requests.get(baseUrl + '/groups/' + group_id + tokenEnding)
    response = response.json()
    print(response)
    for member in response['response']['members']:
        if member['user_id'] == user_id:
            return member['id']
    return None


if __name__ == '__main__':
    print('yes')
