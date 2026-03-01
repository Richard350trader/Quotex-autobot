from flask import Flask, request
import requests

app = Flask(__name__)

# ====== BOT TOKEN ======
TOKEN = "8338747717:AAGPn04Hr0ltPff3i_u-eZobcpnz37C2Xik"
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

# ====== AFFILIATE BASE LINK ======
AFFILIATE_BASE = "https://broker-qx.pro/sign-up/fast/"

# ====== HOME ROUTE ======
@app.route("/")
def home():
    return "Bot is running"

# ====== TELEGRAM WEBHOOK ======
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text")

        if text == "/start":
            # Dynamic affiliate link with Telegram ID
            affiliate_link = f"{AFFILIATE_BASE}?sub_id={chat_id}"

            keyboard = {
                "inline_keyboard": [
                    [
                        {
                            "text": "🚀 Register on Quotex",
                            "url": affiliate_link
                        }
                    ]
                ]
            }

            requests.post(
                f"{TELEGRAM_API}/sendMessage",
                json={
                    "chat_id": chat_id,
                    "text": "🔥 Welcome!\n\nRegister using the button below and deposit $10 to unlock VIP session 💎",
                    "reply_markup": keyboard
                }
            )

        else:
            requests.post(
                f"{TELEGRAM_API}/sendMessage",
                json={
                    "chat_id": chat_id,
                    "text": "Message received 👍"
                }
            )

    return {"status": "ok"}

# ====== QUOTEX POSTBACK ROUTE ======
@app.route("/postback")
def postback():
    user_id = request.args.get("sub_id")
    status = request.args.get("status")

    if user_id and status == "true":
        requests.post(
            f"{TELEGRAM_API}/sendMessage",
            json={
                "chat_id": int(user_id),
                "text": "🎉 Congratulations!\n\n"
                        "Ready for richardtrader VIP bug compounding session 👑\n\n"
                        "📩 Ab is Telegram ID @rajpottrader par message bhejein aur apna session time confirm karein ⏱️\n\n"
                        "💎 Get ready for your Private Compounding Session 🚀"
            }
        )

    return "OK"
