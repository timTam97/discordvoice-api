from flask import Flask

import auth

app = Flask(__name__)


@app.route(auth.API_URL)
def default():
    members = []
    with open("voice_lst", "r") as f:
        for line in f:
            members.append(line.strip())
    return str(members)
