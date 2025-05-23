import time
import requests
import validators
import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread
load_dotenv()

website = os.getenv("WEB_URL")
print(website)

app = Flask("/")

@app.route("/")
def home():
    return "Hello World!"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


def ping(host):
    if validators.url(host) is True:
        r = requests.get(host)
        return r.status_code
    else:
        exit(
            f"Invalid URL '{host}': No scheme supplied. Perhaps you meant http://{host}?"
        )


if __name__ == "__main__":
    while True:
        print(ping(website))
        time.sleep(600)