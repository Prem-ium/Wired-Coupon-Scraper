# Full Instructions:

# Enable Keep Alive by using the KEEP_ALIVE variable in .env
# After running, you can copy the URL from the console and paste it into an UptimeRobot monitor to keep the bot alive 24/7
# Personally, I use Replit to host my flask always-on projects (https://replit.com/).

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Program is online/active, all thanks to UpTimeRobot!"

def run():
    app.run(host = '0.0.0.0', port = 8080)

def keep_alive():
    t = Thread(target = run)
    t.start()