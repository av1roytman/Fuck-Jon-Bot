import os
import json
import requests

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

messageUrl = 'https://api.groupme.com/v3/bots/post'

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    # We don't want to reply to ourselves!
    if data['name'] != 'apnorton-test-bot':
        msg = '{}, you sent "{}".'.format(data['name'], data['text'])
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
