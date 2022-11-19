import os
import requests

from flask import Flask, request

messageUrl = 'https://api.groupme.com/v3/bots/post'
baseUrl = 'https://api.groupme.com/v3'

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "hey", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    # We don't want to reply to ourselves!
    if data['sender_id'] == os.getenv('SENDER_ID'):
        msg = 'Didn\'t you Graduate?'
        sendMessage(os.getenv('GROUPME_BOT_ID'), msg)
    if data['text'] == 'Remove Omar':
        removeUser(group_id=data['group_id'], membership_id='829987163')

    return "ok", 200


def sendMessage(bot_id, text):
    messageData = {
        "bot_id": bot_id,
        "text": text
    }

    response = requests.post(messageUrl, json=messageData)


# /groups/:group_id/members/:membership_id/remove
def removeUser(group_id, membership_id):
    removeUrl = baseUrl + '/groups/' + group_id + '/members/' + membership_id + '/remove' + '?token=' + os.getenv('ACCESS_TOKEN')
    print(removeUrl)
    response = requests.post(removeUrl)
    print(response.json())


if __name__ == '__main__':
    print('yes')
