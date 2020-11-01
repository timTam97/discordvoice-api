import json
from typing import Tuple

import flask

import auth

app = flask.Flask(__name__)


def create_grammar(num_members: int, num_channels: int) -> Tuple[str, str, str]:
    member_addresser = "people"
    ch_addresser = "channels"
    punctuation = ":"
    if num_channels == 1:
        ch_addresser = "channel"
    if num_members == 1:
        member_addresser = "person"
    if num_members == 0 and num_channels == 0:
        punctuation = "."
    return member_addresser, ch_addresser, punctuation


@app.route("/members")
def members():
    if flask.request.headers.get("Authorization") == auth.HEADER_AUTH:
        with open("voice_lst", "r") as f:
            data = json.load(f)
        if flask.request.headers.get("Response-Type") == "natural":
            num_channels = data["occupied_channels"]
            num_members = data["member_count"]
            # How far is too far?
            member_lst = list(
                map(
                    lambda x: x.get("name"),
                    [
                        item
                        for sublist in [sub for sub in data["channels"].values()]
                        for item in sublist
                    ],
                )
            )
            member_addresser, ch_addresser, punctuation = create_grammar(
                num_members, num_channels
            )
            return (
                "{} {} in {} {}{} {}".format(
                    num_members,
                    member_addresser,
                    num_channels,
                    ch_addresser,
                    punctuation,
                    ", ".join(member_lst),
                ),
                200,
            )
        else:
            return flask.jsonify(data), 200
    return "<h1>NO</h1>", 403
