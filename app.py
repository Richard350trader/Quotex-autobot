from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = "APNA_BOT_TOKEN_YAHAN_DALO"

@app.route('/')
def home():
    return "Bot is running"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text")

        if text == "/start":
            send_message(chat_id, "Bot is active ✅")

    return "ok"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
