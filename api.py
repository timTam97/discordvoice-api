import json

import flask

import auth

app = flask.Flask(__name__)


@app.route("/members")
def members():
    if flask.request.headers.get("Authorization") == auth.HEADER_AUTH:
        with open("voice_lst", "r") as f:
            data = json.load(f)
        if flask.request.headers.get("Response-Type") == "natural":
            num_channels = len({k: v for (k, v) in data.items() if len(v) > 0})
            num_members = sum(len(sub) for sub in data.values())
            # How far is too far?
            member_lst = list(
                map(
                    lambda x: x.get("name"),
                    [
                        item for sublist in [sub for sub in data.values()]
                        for item in sublist
                    ],
                ))

            return "{} people in {} channels: {}".format(
                num_members, num_channels, ", ".join(member_lst)), 200
        else:
            return flask.jsonify(data), 200
    return "<h1>NO</h1>", 403
