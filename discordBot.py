import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)
voiceChannel = None


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return

    if 'ayy' in message.content:
        await message.channel.send('lmaoo')

    if f"<@{352974450205130763}>" in message.content:
        await message.channel.send(f"<@{message.author.id}> fuck you. dont ping me, you bitch")


@client.command(pass_context=True)
async def ayy(ctx):
    await ctx.send("lmaoo")


@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        global voiceChannel
        if ctx.voice_client:
            await voiceChannel.move_to(channel)
        else:
            voiceChannel = await channel.connect()
    else:
        await ctx.send("You're not in a voice channel")


@client.command(pass_context=True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I leave voice channel")

    else:
        await ctx.send("I'm not in a voice channel at this moment")



client.run()
