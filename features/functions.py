import os
import random

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


# Loads the Connected Server List from File as a String
def getServerList(client):
    serverStr = '[' + str(len(client.servers)) + '] '
    if len(client.servers) > 0:
        connectedServers = list(client.servers)
        for server in connectedServers:
            serverStr += server.name + ' (' + server.id + ')'
            if (server != connectedServers[-1]):
                serverStr += ', '
    return serverStr
