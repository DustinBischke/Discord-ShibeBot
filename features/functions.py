import asyncio
import discord
import os
import random
import re
import urllib.parse
import urllib.request
from features import commands
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
            if server != connectedServers[-1]:
                serverStr += ', '
    return serverStr


# Returns Total Amount of Users in All Servers Connected To
def get_user_count():
    count = 0
    for server in list(client.servers):
        count += len(server.members)
    return count


# Strips the Alias and WhiteSpace
def prune_alias(message, aliases):
    for alias in aliases:
        if message.startswith(alias):
            message = message[len(alias):].strip()
            break
    return message


# Returns Youtube URL for Top Result from Search Query
def search_youtube(search):
    query_string = urllib.parse.urlencode({"search_query" : search})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return 'http://www.youtube.com/watch?v=' + search_results[0]
