from flask import Flask, request, abort
import requests
import json
from AIchat import callAI

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        reply_token = payload['events'][0]['replyToken']
        print(reply_token)

        # Check if 'message' key exists in the payload
        if 'message' in payload['events'][0]:
            message = payload['events'][0]['message']['text']
            print(message)

            reply_message_text = callAI(message)    
            reply_message(reply_token, reply_message_text, 'kXG3Al9bf81+wGV7cR86cl9xq/XAcTbbKG8qzRoW/RkXEYsXOzgBZnCS9wot/2n7M2s3D0LfBeE/NDA3H95zlvqKnhuDrgr9HFJBpGdehHhsojYqhMchCCNo+HiB/YbnWD2/rUfZ24QOUJqEUXSbXQdB04t89/1O/w1cDnyilFU=')  # ใส่ Channel access token
            return request.json, 200
        else:
            # Handle the case where 'message' key is missing
            abort(400)

def reply_message(reply_token, text_message, line_access_token):
    line_api = 'https://api.line.me/v2/bot/message/reply'
    authorization = 'Bearer {}'.format(line_access_token)
    print(authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }
    data = {
        "replyToken": reply_token,
        "messages": [{
            "type": "text",
            "text": text_message
        }]
    }
    data = json.dumps(data)
    r = requests.post(line_api, headers=headers, data=data)
    return r.status_code

if __name__ == '__main__':
    app.run(debug=True)
