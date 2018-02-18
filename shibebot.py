import asyncio
import discord
from features import commands, functions
from settings import config

client = functions.client


@client.event
# Prints Info to Console when Bot has Successfully Connected
async def on_ready():
    print('Bot Connected.')
    print('Username: ' + functions.get_bot_name())
    print('Client ID: ' + functions.get_bot_id())
    print('Connected Servers: ' + str(functions.get_server_count()))
    print('Invite URL: ' + functions.get_bot_invite())
    await client.change_presence(game=discord.Game(name=config.game_status))


@client.event
# Reads Messages and Checks for Commands
async def on_message(message):
    # Checks if Message begins with Prefix, and not sent by a Bot
    if message.content.lower().startswith(config.prefix.lower()) and not message.author.bot:
        # Prevents Users from Executing Commands in Private Messages
        if message.channel.is_private:
            await client.send_message(message.channel, "Sorry, I can't Execute Commands in Private Messages!")
            return
        # Allows only Bot Developer to Execute Commands if in Maintenance Mode
        if config.maintenance and message.author.id != config.dev_id:
            await client.send_message(message.channel, config.maintenance_msg)
            return
        # Removes Prefix and White Space from Command at Start and End
        message.content = message.content[len(config.prefix):].strip()
        message_lower = message.content.lower()
        # Checks if Command Exists in Commands List
        for command in commands.cmds:
            # Checks all Aliases Defined for Each Command
            if message_lower.startswith(command.aliases):
                # Runs only if Command is Enabled
                if command.enabled:
                    # Removes Alias from Command Content
                    message.content = functions.strip_command_alias(message.content, command.aliases)
                    # TODO: Remove This Section, Make all Commands Run with await command.run()
                    if command.sendsFile:
                        await client.send_file(message.channel, command.run())
                    else:
                        await client.send_message(message.channel, command.run(message))
                # If Command not Enabled, inform the User
                else:
                    await client.send_message(message.channel, command.name + ' Command has been Disabled')
                return
        # If Command not Found, Notify the User if Enabled in Config
        if config.notify_invalid_command:
            await client.send_message(message.channel, commands.invalid_command())


#@client.event
# Records Log of Deleted Messages
#async def on_message_delete(message):
#    # Logs only if Message Author was not a Bot
#    if not message.author.bot:
#        await client.send_message(message.channel, message.author.name + '#' + message.author.discriminator + ' Message has been Deleted: "' + message.content + '"')


client.run(config.token)
