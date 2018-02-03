import asyncio
import discord
import os
import random
from settings import *

client = discord.Client()


# Returns the Bot Developer Name - Function must be Awaited when running
async def get_bot_dev():
    dev_user = await client.get_user_info(config.dev_id)
    dev = dev_user.name + '#' + dev_user.discriminator
    return dev


# Returns the Bot Name
def get_bot_name():
    return client.user.name


# Returns the Bot ID
def get_bot_id():
    return client.user.id


# Returns Directory of Random Picture from Specified Directory Within /resources/
def get_random_picture(directory):
    directory = 'resources/' + directory + '/'
    image = directory + random.choice(os.listdir(directory))
    return image


# Returns Number of Servers Connected
def get_server_count():
    return len(client.servers)


# Loads the Connected Server List from File as a String
def get_server_list():
    serverStr = ''
    if get_server_count() > 0:
        connectedServers = list(client.servers)
        for server in connectedServers:
            serverStr += server.name
            # serverStr += ' (' + server.id + ')'
            if (server != connectedServers[-1]):
                serverStr += ', '
    return serverStr


# Returns Total Amount of Users in All Servers Connected To
def get_user_count():
    count = 0
    for server in list(client.servers):
        count += len(server.members)
    return count


# Strips the Alias and WhiteSpace, and Returns True if new Length > 0
def check_message_not_empty(message, aliases):
    for alias in aliases:
        if message.startswith(alias):
            if len(message[len(alias):].strip()) > 0:
                return True
            else:
                return False


def prune_alias(message, aliases):
    for alias in aliases:
        if message.startswith(alias):
            message = message[len(alias):].strip()
    return message