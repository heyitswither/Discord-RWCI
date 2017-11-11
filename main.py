import rwci
import discord
import yaml

config = yaml.safe_load(open('config.yml'))

discord_client = discord.Client()
rwci_client = rwci.Client(gateway_url=config.get('rwci').get('gateway'))

@discord_client.event
async def on_ready():
    channel = discord_client.get_channel(str(config.get('discord').get('channel_id')))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nDiscord client ready!")
    print(f"{discord_client.user.name}#{discord_client.user.discriminator} {discord_client.user.id}")
    print(f"Watching #{channel.name} in {channel.server.name}")

@rwci_client.event
async def on_ready():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nRWCI client ready!")
    print(f"{rwci_client.username}")
    print(f"Watching #{config.get('rwci').get('channel')} on {rwci_client.gateway_url}")

@discord_client.event
async def on_message(message):
    if message.author == discord_client.user: return
    if not message.channel.id == str(config.get('discord').get('channel_id')): return
    await rwci_client.send(f"{message.author.name}: {message.clean_content}", config.get('rwci').get('channel'))

@rwci_client.event
async def on_message(message):
    if message.author == rwci_client.username: return
    message.content = message.content.replace('@', '@' + u'\u200b')
    if config.get('rwci').get('channel'):
      if not config.get('rwci').get('channel') == message.channel: return
      await discord_client.send_message(discord_client.get_channel(str(config.get('discord').get('channel_id'))), f"<{message.author}> {message.content}")
    else:
      await discord_client.send_message(discord_client.get_channel(str(config.get('discord').get('channel_id'))), f"#{message.channel} <{message.author}> {message.content}")

@rwci_client.event
async def on_join(member):
    await discord_client.send_message(discord_client.get_channel(str(config.get('discord').get('channel_id'))), f"*{member} has connected*")

@rwci_client.event
async def on_quit(member):
    await discord_client.send_message(discord_client.get_channel(str(config.get('discord').get('channel_id'))), f"*{member} has disconnected*")

@rwci_client.event
async def on_direct_message(message):
    await discord_client.send_message(discord_client.get_channel(str(config.get('discord').get('channel_id'))), f"|{message.author} > {rwci_client.username}| {message.content}")

async def start():
    await discord_client.wait_until_ready()
    await rwci_client.login(config.get('rwci').get('username'), config.get('rwci').get('password'))

discord_client.loop.create_task(start())
discord_client.run(config.get('discord').get('token'))

