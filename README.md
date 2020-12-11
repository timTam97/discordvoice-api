# discordvoice-api
Simple Flask API, used in [alexa-discordvoice](https://github.com/timTam97/alexa-discordvoice). Returns information on members in voice chat on a Discord server.

Consists of a Discord bot (`voice.py`) that must be joined to the server you want to monitor, and a Flask app (`api.py`) that serves up the information in JSON form.

### Sample Output
```json
{
  "member_count": 3,
  "occupied_channels": 2,
  "live_count": 1,
  "channels": {
    "Channel 1": [],
    "Channel 2": [],
    "Channel 3": [
      {
        "name": "memberOne",
        "self_deaf": false,
        "self_mute": false,
        "server_deaf": false,
        "server_mute": false,
        "streaming": true
      },
      {
        "name": "memberTwo",
        "self_deaf": false,
        "self_mute": false,
        "server_deaf": false,
        "server_mute": false,
        "streaming": false
      },
    ],
    "Channel 4": [
      {
        "name": "anotherMember",
        "self_deaf": true,
        "self_mute": true,
        "server_deaf": false,
        "server_mute": false,
        "streaming": false
      }
    ],
    "Channel 5": [],
    "Channel 6": [],
    "Channel 7": [],
    "Channel 8": []
  }
}
```
