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
    if data['name'] != 'Fuck Jon':
        msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        print(os.getenv('GROUPME_BOT_ID'))
        sendMessage(os.getenv('GROUPME_BOT_ID').replace('\n', ''), msg)
    print(data)

    return "ok", 200


def sendMessage(bot_id, text):
    print('this got here')
    messageData = {
        "bot_id": bot_id,
        "text": text
    }
    response = requests.post(messageUrl, data=messageData)
    print(response.json())
    print('this got her 2')


if __name__ == '__main__':
    print('yes')
