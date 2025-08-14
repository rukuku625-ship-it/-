from flask import Flask from threading import Thread
app = Flask name
@app. route (' / def home ():
return "Both is running!"
def run():
app. run (host ="0.0.0.0*
port =8080)
def keep alivel):
t = Thread (target=run)
t.start ()
