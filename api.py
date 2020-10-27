import json

import flask

import auth

app = flask.Flask(__name__)


@app.route(auth.API_URL)
def default():
    if flask.request.headers.get("Authorization") == auth.HEADER_AUTH:
        members = []
        with open("voice_lst", "r") as f:
            for line in f:
                members.append(line.strip())
        return flask.Response(response=json.dumps(members), status=200)
    return flask.Response(response="no", status=403)
