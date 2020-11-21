import datetime
import json

import discord

import auth

client = discord.Client()
attached_guild: discord.Guild = None


@client.event
async def on_voice_state_update(member=None, before=None, after=None):
    assert attached_guild is not None
    member_count = 0
    live_count = 0
    occupied_channel_count = 0
    voice_data = {"channels": {}}
    for channel in attached_guild.voice_channels:
        nonempty = False
        channel_member_lst = []
        for member in channel.members:
            nonempty = True
            member_count += 1
            live_count += 1 if member.voice.self_stream else 0
            channel_member_lst.append(
                {
                    "name": member.name,
                    "streaming": member.voice.self_stream,
                    "self_mute": member.voice.self_mute,
                    "self_deaf": member.voice.self_deaf,
                    "server_deaf": member.voice.deaf,
                    "server_mute": member.voice.mute,
                }
            )
        occupied_channel_count += 1 if nonempty else 0
        voice_data["channels"][str(channel)] = channel_member_lst
    voice_data["occupied_channels"] = occupied_channel_count
    voice_data["member_count"] = member_count
    voice_data["live_count"] = live_count
    with open("voice_lst", "w") as f:
        json.dump(voice_data, f)
    print("[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] updated")


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    global attached_guild
    for guild in client.guilds:
        if guild.name == auth.SERVER_NAME:
            attached_guild = guild
    await on_voice_state_update()


def main():
    client.run(auth.DISCORD_TOKEN)


if __name__ == "__main__":
    main()
