import json
import os
import time

import requests

from flask import Flask, request

messageUrl = 'https://api.groupme.com/v3/bots/post'
baseUrl = 'https://api.groupme.com/v3'
tokenEnding = '?token=' + os.getenv('ACCESS_TOKEN')

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "hey", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)

    # We don't want to reply to ourselves!
    # if data['sender_id'] == os.getenv('SENDER_ID'):
    #     msg = 'Didn\'t you Graduate?'
    #     sendMessage(os.getenv('GROUPME_BOT_ID'), msg)
    if data['text'] == 'Remove Myself':
        msg = 'Get Fucked Cuh'
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
