import asyncio
import cleverwrap
import discord
import giphy_client
import os
import random
import re
import urllib.parse
import urllib.request
from settings import config

client = discord.Client()
cleverbot = cleverwrap.CleverWrap(config.cleverbot_api)


# Returns the Bot Developer Name and Discriminator
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


# Returns the Bot Invite URL
def get_bot_invite():
    return 'https://discordapp.com/oauth2/authorize?client_id=' + get_bot_id() + '&scope=bot&permissions=' + config.permissions


# Returns Number of Servers the Bot is Connected to
def get_server_count():
    return len(client.servers)


# Returns the Connected Server List as a String
def get_server_list():
    if get_server_count() > 0:
        servers = ''
        server_list = sorted(list(client.servers), key=lambda server: server.member_count, reverse=True)
        for server in server_list:
            servers += server.name + ' (' + str(server.member_count) + ')'
            if server != server_list[-1]:
                servers += ', '
        return servers
    return 'None'


# Returns Number of Users in Specific Server
def get_user_count(server):
    return server.member_count


# Returns Total Users in All Servers the Bot is Connected to
def get_total_user_count():
    count = 0
    for server in list(client.servers):
        count += server.member_count
    return count


# Strips Command Alias and WhiteSpace from Front and Back of Message
def strip_command_alias(message, aliases):
    message_lower = message.lower()
    for alias in aliases:
        if message_lower.startswith(alias):
            message = message[len(alias):].strip()
            break
    return message


# Returns Cleverbot Response to Input Message
def get_cleverbot_response(message):
    if config.cleverbot_api != '':
        response = cleverbot.say(message)
        return response
    else:
        return 'Missing Cleverbot API in Config'


# Returns File Name of Random Picture from Specified Directory Within /resources/
def get_random_image(directory):
    directory = 'resources/' + directory + '/'
    image = directory + random.choice(os.listdir(directory))
    return image


# Returns Giphy URL of Random GIF Result from Search Query
def get_random_giphy(search):
    api_instance = giphy_client.DefaultApi()
    api_response = api_instance.gifs_random_get(config.giphy_api, tag=search, rating=config.giphy_rating)
    return api_response.data.url


# Returns Youtube URL of Top Result from Search Query
def get_youtube_search_result(search):
    query_string = urllib.parse.urlencode({'search_query' : search})
    html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return 'http://www.youtube.com/watch?v=' + search_results[0]
