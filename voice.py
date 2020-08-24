import auth
import discord

client = discord.Client()


@client.event
async def on_voice_state_update(member=0, before=0, after=0):
    pingu = 0
    for guild in client.guilds:
        if guild.name == auth.SERVER_NAME:
            pingu = guild
    members = []
    for channel in pingu.voice_channels:
        members.append(channel.members)
    members = [item for sublist in members for item in sublist]
    members = list(map(lambda x: x.name, members))
    with open("voice_lst", "w") as f:
        for member in members:
            f.write(str(member) + "\n")
    print("updated.")


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    await on_voice_state_update()


def main():
    client.run(auth.DISCORD_TOKEN)


if __name__ == "__main__":
    main()
