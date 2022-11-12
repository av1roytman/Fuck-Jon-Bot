import os
import requests

from flask import Flask, request

messageUrl = 'https://api.groupme.com/v3/bots/post'

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

    return "ok", 200


def sendMessage(bot_id, text):
    messageData = {
        "bot_id": bot_id,
        "text": text
    }

    response = requests.post(messageUrl, json=messageData)


if __name__ == '__main__':
    print('yes')
