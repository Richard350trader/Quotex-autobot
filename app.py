from flask import Flask, request
import requests
import os

app = Flask(__name__)

# ====== CONFIG ======
TOKEN = os.environ.get("BOT_TOKEN")  # Render me environment variable set karna
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

AFFILIATE_LINK = "https://broker-qx.pro/sign-up/?lid=1667491"

# ====== FUNCTION TO SEND MESSAGE ======
def send_message(chat_id, text):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

# ====== HOME ROUTE ======
@app.route("/")
def home():
    return "Bot is running ✅"

# ====== TELEGRAM WEBHOOK ======
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if not data:
        return {"status": "no data"}

    if "message" in data:
        chat_id = str(data["message"]["chat"]["id"])
        text = data["message"].get("text", "")

        if text == "/start":
            custom_link = f"{AFFILIATE_LINK}&sub_id={chat_id}"

            send_message(chat_id,
                "🔥 Welcome to RichardTrader Compounding Session 🔥\n\n"
                "👇 Pehle is link se account create karein:\n\n"
                f"{custom_link}\n\n"
                "💰 Account create karne ke baad minimum $10 deposit karein."
            )

    return {"status": "ok"}

# ====== QUOTEX POSTBACK ======
@app.route("/postback", methods=["GET"])
def postback():
    sub_id = request.args.get("sub_id")
    amount = request.args.get("amount")

    if sub_id and amount:
        amount = float(amount)

        if amount >= 10:
            send_message(sub_id,
                "🎉 Congratulations!\n\n"
                "You are now officially in RICHARDTRADER session 👑\n\n"
                "📩 Ab @richardteam0 par message bhejein aur apna session time confirm karein."
            )
        else:
            send_message(sub_id,
                f"❌ Aapka balance ${amount} hai.\n"
                "⚠️ Minimum required: $10\n\n"
                "👉 Please top-up karein aur phir try karein."
            )

    return "OK"

# ====== RUN APP ======
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
