import json

import flask

import auth

app = flask.Flask(__name__)


@app.route("/members")
def members():
    if flask.request.headers.get("Authorization") == auth.HEADER_AUTH:
        with open("voice_lst", "r") as f:
            data = json.load(f)
        return flask.jsonify(data), 200
    return "<h1>NO</h1>", 403
