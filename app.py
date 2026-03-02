from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

AFFILIATE_LINK = "https://broker-qx.pro/sign-up/?lid=1667491"

# Temporary memory store
users = {}

def send_message(chat_id, text):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

@app.route("/")
def home():
    return "Bot is running ✅"

# Telegram webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = str(data["message"]["chat"]["id"])
        text = data["message"].get("text", "")

        if text == "/start":
            custom_link = f"{AFFILIATE_LINK}&sub_id={chat_id}"
            users[chat_id] = {"deposit": 0}

            send_message(chat_id,
                "Welcome to RichardTrader Compounding Bug Session\n\n"
                "👇 Pehle is link se account create karein:\n"
                f"{https://market-qx.trade/sign-up/?lid=536015}\n\n"
                "Account create karne ke baad minimum $10 deposit karein."
            )

    return {"status": "ok"}

# Quotex Postback
@app.route("/postback", methods=["GET"])
def postback():
    sub_id = request.args.get("sub_id")
    amount = request.args.get("amount")
    status = request.args.get("status")

    if sub_id and amount:
        amount = float(amount)

        if amount >= 10:
            send_message(sub_id,
                "🎉 Congratulations!\n\n"
                "You are now officially in RICHARDTRADER bug session 🤍 👑\n\n"
                "📩 Ab is Telegram ID @richardteam0 par message bhejein aur apna session time confirm karein ⏱️\n\n"
                "💎 Get ready for your Private Compounding Session 🚀"
            )
        else:
            send_message(sub_id,
                "❌ Aapka current balance abhi minimum requirement se kam hai.\n\n"
                f"💰 Current Balance: ${amount}\n\n"
                "⚠️ Minimum required: $10\n\n"
                "👉 Please thoda sa top-up karein aur phir se try karein."
            )

    return "OK"
