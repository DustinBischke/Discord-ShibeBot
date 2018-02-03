import asyncio
import discord
from features import *
from settings import *

client = functions.client


@client.event
# Prints Bot Info to Console when Bot has Successfully Connected
async def on_ready():
    print('Bot Connected.')
    print('Username: ' + functions.getBotName())
    print('Client ID: ' + functions.getBotID())
    print('Connected Servers (' + str(functions.getServerCount()) + '): ' + functions.getServerList())
    print('Invite URL: https://discordapp.com/oauth2/authorize?&client_id=' + functions.getBotID() + '&scope=bot&permissions=' + config.permissions)
    await client.change_presence(game=discord.Game(name=config.game))


@client.event
# Reads Messages and Checks for Bot Commands
async def on_message(message):
    # Checks if Message begins with Prefix as defined in config.py, and not sent by a Bot
    if message.content.lower().startswith(config.prefix) and message.author.bot == False:
        # Removes Prefix and White Space from Command at Start and End
        msg = message.content[len(config.prefix):].lower().strip()

        # If Maintenance Mode is Enabled, only Bot Author can Execute Commands
        if config.maintenance and message.author.id != config.devid:
            await client.send_message(message.channel, 'Maintenance Mode Enabled. Sorry for the Inconvenience!')
        else:
            for command in commands.cmds:
                if command.enabled and msg.startswith(command.alias):
                    if command.sendsFile:
                        await client.send_file(message.channel, command.run())
                    else:
                        if command.acceptsInput:
                            await client.send_message(message.channel, command.run(msg))
                        else:
                            await client.send_message(message.channel, command.run())
                    return

            # If Command not found in list, run InvalidCommand
            await client.send_message(message.channel, commands.invalid())


client.run(config.token)
