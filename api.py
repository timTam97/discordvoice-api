import json
from typing import Tuple

import flask

import auth

app = flask.Flask(__name__)


def create_grammar(
    num_members: int, num_channels: int, num_live: int, num_non_live: int
) -> Tuple[str, str, str, str, str]:
    member_addresser = "people"
    ch_addresser = "channels"
    live_addresser = "Live: "
    non_live_addresser = ""
    punctuation = ":"
    if num_channels == 1:
        ch_addresser = "channel"
    if num_members == 1:
        member_addresser = "person"
    if num_members == 0 and num_channels == 0:
        punctuation = "."
    if num_live == 0:
        live_addresser = ""
    if num_non_live == 0:
        non_live_addresser = ""
    elif (num_non_live == 0 and num_live != 0) or (num_live == 0 and num_non_live != 0):
        live_addresser = ""
        non_live_addresser = ""
    return (
        member_addresser,
        ch_addresser,
        punctuation,
        live_addresser,
        non_live_addresser,
    )


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
                    lambda x: [x.get("name"), x.get("streaming")],
                    [
                        item
                        for sublist in [sub for sub in data["channels"].values()]
                        for item in sublist
                    ],
                )
            )
            members_non_live = list(
                map(lambda x: x[0], filter(lambda x: not x[1], member_lst))
            )
            members_live = list(map(lambda x: x[0], filter(lambda x: x[1], member_lst)))
            (
                member_addresser,
                ch_addresser,
                punctuation,
                live_addresser,
                non_live_addresser,
            ) = create_grammar(
                num_members, num_channels, len(members_live), len(members_non_live)
            )
            num_line_breaks = 2 if len(members_live) > 0 else 1
            # ok definitely too far
            return (
                "{} {} in {} {}{}{}{}{}{}{}{}".format(
                    num_members,
                    member_addresser,
                    num_channels,
                    ch_addresser,
                    punctuation,
                    "<br/>" * num_line_breaks,
                    live_addresser,
                    ", ".join(members_live),
                    "<br/>" * num_line_breaks,
                    non_live_addresser,
                    ", ".join(members_non_live),
                ),
                200,
            )
        else:
            return flask.jsonify(data), 200
    return "<h1>NO</h1>", 403
