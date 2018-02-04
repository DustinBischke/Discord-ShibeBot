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
        elif config.maintenance and message.author.id != config.dev_id:
            await client.send_message(message.channel, config.maintenance_msg)
            return
        else:
            # Removes Prefix and White Space from Command at Start and End
            message.content = message.content[len(config.prefix):].lower().strip()
            # Checks if Command Exists in Commands List
            for command in commands.cmds:
                # Checks all Aliases Defined for Each Command
                if message.content.startswith(command.alias):
                    # Runs only if Command is Enabled
                    if command.enabled:
                        # Removes Alias from Command Content
                        message.content = functions.prune_alias(message.content, command.alias)
                        # TODO: Remove This Section, make everything run from await command.run()
                        #       Allowing removal of sendsFile check from Commands
                        if command.sendsFile:
                            await client.send_file(message.channel, command.run())
                        else:
                            await client.send_message(message.channel, command.run(message))
                    # If Command not Enabled, inform the User
                    else:
                        await client.send_message(message.channel, command.name + ' Command has been Disabled')
                    return
            # If Command not found, run InvalidCommand
            await client.send_message(message.channel, commands.invalid_command())


#@client.event
# Records Log of Deleted Messages
#async def on_message_delete(message):
#    # Logs only if Message Author was not a Bot
#    if not message.author.bot:
#        await client.send_message(message.channel, message.author.name + '#' + message.author.discriminator + ' Message has been Deleted: "' + message.content + '"')


client.run(config.token)
