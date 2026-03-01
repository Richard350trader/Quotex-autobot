from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("No BOT_TOKEN set in environment variables")

TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"


@app.route("/")
def home():
    return "Bot is running ✅"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received update:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # START command
        if text.lower() == "/start":
            send_message(chat_id, "Welcome 🔥\n\nSend your deposit amount.")

        # Deposit detection (number only)
        elif text.isdigit():
            amount = text
            send_message(chat_id, f"Deposit of {amount} received ✅\nProcessing...")

        else:
            send_message(chat_id, "Please send a valid deposit amount (numbers only).")

    return {"status": "ok"}


def send_message(chat_id, text):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
