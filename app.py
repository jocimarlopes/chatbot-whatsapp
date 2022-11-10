from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import bot
from neural_links import learning

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    user_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    jarvis = bot.init(user_msg)
    print(user_msg, ' - ', jarvis)
    learning.listening_all_time(user_msg, jarvis)
    msg.body(jarvis)
    return str(resp)

if __name__ == '__main__':
   app.run()
