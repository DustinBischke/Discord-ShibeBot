import asyncio
import discord
import os
import random
from settings import *

client = discord.Client()


# Returns the Bot Developer Name
#async def getBotDeveloper():
#    devUser = await client.get_user_info(config.devid)
#    dev = devUser.name# + '#' + devUser.discriminator
#    return dev


# Returns the Bot Name
def getBotName():
    return client.user.name


# Returns the Bot ID
def getBotID():
    return client.user.id


# Strips the Alias and WhiteSpace, and Returns True if new Length > 0
def checkMessageNotEmpty(message, aliases):
    for alias in aliases:
        if message.startswith(alias):
            if len(message[len(alias):].strip()) > 0:
                return True
            else:
                return False


# Returns Random Integer Within Range
def getRandomNumber(min, max):
    return random.randint(min, max)


# Returns Directory of Random Image in Specified Directory Within /resources/
def getRandomImage(directory):
    directory = 'resources/' + directory + '/'
    image = directory + random.choice(os.listdir(directory))
    return image


# Returns Number of Servers Connected
def getServerCount():
    return len(client.servers)


# Loads the Connected Server List from File as a String
def getServerList():
    serverStr = ''
    if getServerCount() > 0:
        connectedServers = list(client.servers)
        for server in connectedServers:
            serverStr += server.name
            # serverStr += ' (' + server.id + ')'
            if (server != connectedServers[-1]):
                serverStr += ', '
    return serverStr


# Returns Total Amount of Users in All Servers Connected To
def getTotalUserCount():
    count = 0;
    for server in list(client.servers):
        count += len(server.members)
    return count;
