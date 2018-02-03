import asyncio
import discord
from features import *
from settings import *

client = functions.client


@client.event
# Prints Bot Info to Console when Bot has Successfully Connected
async def on_ready():
    print('Bot Connected.')
    print('Username: ' + functions.get_bot_name())
    print('Client ID: ' + functions.get_bot_id())
    print('Connected Servers (' + str(functions.get_server_count()) + '): ' + functions.get_server_list())
    print('Invite URL: https://discordapp.com/oauth2/authorize?&client_id=' + functions.get_bot_id() + '&scope=bot&permissions=' + config.permissions)
    await client.change_presence(game=discord.Game(name=config.game))


@client.event
# Reads Messages and Checks for Bot Commands
async def on_message(message):
    # Checks if Message begins with Prefix as defined in config.py, and not sent by a Bot
    if message.content.lower().startswith(config.prefix) and not message.author.bot:
        # Prevents Users from Executing Commands in Private Messages
        if message.channel.is_private:
            await client.send_message(message.channel, "Sorry, I can't Execute Commands in Private Messages!")
            return
        # If Maintenance Mode is Enabled, only Bot Author can Execute Commands
        if config.maintenance and message.author.id != config.dev_id:
            await client.send_message(message.channel, config.maintenance_msg)
            return
        # Removes Prefix and White Space from Command at Start and End
        msg = message.content[len(config.prefix):].lower().strip()
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
        # If Command not found, run InvalidCommand
        await client.send_message(message.channel, commands.invalid())


#@client.event
# Records Log of Deleted Messages
#async def on_message_delete(message):
#    # Logs only if Message Author was not a Bot
#    if not message.author.bot:
#        await client.send_message(message.channel, message.author.name + '#' + message.author.discriminator + ' Message has been Deleted: "' + message.content + '"')


client.run(config.token)
