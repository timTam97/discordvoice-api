import datetime
import json

import discord

import auth

client = discord.Client()
attached_guild: discord.Guild = None


@client.event
async def on_voice_state_update(member=None, before=None, after=None):
    assert attached_guild is not None
    voice_data = {}
    for channel in attached_guild.voice_channels:
        channel_member_lst = []
        for member in channel.members:
            channel_member_lst.append(
                {"name": member.name, "streaming": member.voice.self_stream}
            )
        voice_data[str(channel)] = channel_member_lst
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
