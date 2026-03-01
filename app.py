from flask import Flask, request

app = Flask(__name__)

# Home Route (Check if server running)
@app.route("/")
def home():
    return "Bot is running"

# Postback Route (GET + POST dono allow)
@app.route("/postback", methods=["GET", "POST"])
def postback():
    try:
        # GET parameters (jab link browser se test karte ho)
        user_id = request.args.get("sub_id")
        status = request.args.get("status")

        # Agar POST aaye (future safety ke liye)
        if request.method == "POST":
            data = request.form
            user_id = data.get("sub_id")
            status = data.get("status")

        print("Received Postback:")
        print("User ID:", user_id)
        print("Status:", status)

        if user_id and status:
            return "OK", 200
        else:
            return "Missing parameters", 400

    except Exception as e:
        print("Error:", str(e))
        return "Server Error", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
