from flask import Flask, request, jsonify
import os
import threading
import requests

app = Flask(__name__)

# URL Webhook Discord (Ganti dengan URL webhook yang kamu buat)
WEBHOOK_URL = "https://discord.com/api/webhooks/1349682417455071293/ZTbAFIcA5xgC1DxQ-T3i5vYWUQq1BVjlXuNbbvRQs60SFdcuwIX_D3pVZ495_qiRb-j4"

def send_webhook_message(message):
    payload = {
        "content": message
    }
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code != 204:
        print(f"Error sending webhook: {response.status_code}")
    else:
        print("Message sent to Discord webhook!")

def run_bot(token):
    os.system(f"python bot.py {token}")
    send_webhook_message(f"✅ Bot is running with token: {token}")

@app.route("/run-bot", methods=["POST"])
def start_bot():
    data = request.json
    token = data.get("token", "ADMIN123")

    # Jalankan bot di thread terpisah
    thread = threading.Thread(target=run_bot, args=(token,))
    thread.start()

    # Kirim pesan bahwa bot sedang dijalankan ke Discord webhook
    send_webhook_message(f"✅ Bot has been started with token: {token}")

    return "✅ Bot sedang berjalan!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
