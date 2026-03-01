from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received data:", data)

    user_id = data.get("user_id")
    deposit = data.get("deposit")

    if deposit:
        return {"status": "Deposit received", "user_id": user_id}
    else:
        return {"status": "No deposit"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
