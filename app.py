from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8338747717:AAGPn04Hr0ltPff3i_u-eZobcpnz37C2Xik"
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/')
def home():
    return "Bot is running"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            reply = "Welcome! Bot is working ✅"
        else:
            reply = "Message received 👍"

        requests.post(
            f"{TELEGRAM_API}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": reply
            }
        )

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    @app.route("/postback")
def postback():
    user_id = request.args.get("sub_id")
    status = request.args.get("status")

    if user_id and status == "true":
        send_message(
            int(user_id),
            "🎉 Congratulations!\n\n"
            "Ready for richardtrader VIP bug compounding session 👑\n\n"
            "📩 Ab is Telegram ID @rajpottrader par message bhejein aur apna session time confirm karein ⏱️\n\n"
            "💎 Get ready for your Private Compounding Session 🚀"
        )

    return "OK"
