import requests
import json

messageUrl = 'https://api.groupme.com/v3/bots/post'
botDataFile = 'botData.json'


def sendMessage(bot_id, text):
    messageData = {
        "bot_id": bot_id,
        "text": text
    }
    requests.post(messageUrl, json=messageData)


if __name__ == '__main__':
    bot_id = 'dc4082fa5dea7d3a200cc69f08'
    message = input('What Message would you like to send? ')
    sendMessage(bot_id, message)
