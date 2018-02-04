import random
from features import functions, textformat
from settings import *

client = functions.client


class Command:
    def __init__(self, name, desc, alias, args, acceptsInput, sendsFile, enabled):
        self.name = name
        self.desc = desc
        self.alias = alias
        self.args = args
        self.acceptsInput = acceptsInput
        self.sendsFile = sendsFile
        self.enabled = enabled

    def help_short(self):
        return textformat.bold(self.name) + ' - ' + self.desc + '\n'

    def help_long(self):
        command_name = textformat.bold(self.name + ' Help:')
        command_args = ''
        # If only 1 Argument
        if type(self.args) is str:
            # Adds Args only if Not Empty
            if self.args:
                command_args += '<' + self.args.lower() + '>'
        else:
            # If Multiple Arguments
            for arg in self.args:
                command_args += '<' + arg.lower() + '>'
                if arg != self.args[-1]:
                    command_args += ' '
        command_usage = 'Usage: ' + config.prefix + ' ' + self.name.lower() + ' ' + command_args
        command_desc = 'Description: ' + self.desc
        command_alias = 'Aliases: ' + str(self.alias)
        return command_name + '\n' + command_usage + '\n' + command_desc + '\n' + command_alias + '\n'

    def run(self):
        return


class Help(Command):
    def __init__(self, enabled):
        Command.__init__(self, 'Help', 'Displays Bot Information', ('help', 'about', 'commands'), 'Command', True, False, enabled)

    def run(self, message):
        if not message.content:
            return help_all()
        else:
            for command in cmds:
                # If Command Exists, Print Longer Help
                if message.content.startswith(command.alias):
                    return command.help_long()
            # If Command doesn't Exist
            return invalid_command()


class Bork(Command):
    def __init__(self, enabled):
        Command.__init__(self, 'Bork', 'Does a Heckin Bork', ('bork', 'woof', 'speak'), '', False, False, enabled)

    def run(self):
        return textformat.bold('BORK ' * random.randint(1, 200))


class CoinFlip(Command):
    def __init__(self, enabled):
        Command.__init__(self, 'CoinFlip', 'Flips a Coin Revealing Heads or Tails', ('coinflip', 'flipcoin', 'headsortails'), (''), False, False, enabled)

    def run(self):
        return random.choice(['Heads', 'Tails'])


class Eightball(Command):
    def __init__(self, enabled):
        Command.__init__(self, '8ball', 'Answers Yes/No Questions', ('8ball', 'ask', 'yesorno'), 'Question', True, False, enabled)

    def run(self, message):
        if message.content:
            answers = ['It is certain!', 'It is decidedly so!', 'Without a doubt!', 'Yes definitely!', 'You may rely on it!', 'As I see it yes!', 'Most likely!', 'Outlook good!', 'Yes!', 'Signs point to yes!', 'Reply hazy try again!', 'Ask again later!', 'Better not tell you now!', 'Cannot predict now!', 'Concentrate and ask again!', "Don't count on it!", 'My reply is no!', 'My sources say no!', 'Outlook not so good!', 'Very doubtful!']
            return random.choice(answers)
        else:
            return 'You must enter a Yes/No Question'


class Roll(Command):
    def __init__(self, enabled):
        Command.__init__(self, 'Roll', 'Rolls a Random Number', ('roll', 'randomnumber'), 'Max', True, False, enabled)

    def run(self, message):
        if message.content:
            if message.content.isdigit() and int(message.content) > 1:
                return random.randint(1, int(message.content))
            else:
                return 'Invalid Max Number Entered'
        else:
            return random.randint(1, 10)


class Shibe(Command):
    def __init__(self, enabled):
        Command.__init__(self, 'Shibe', 'Sends a Cute Shibe Picture', ('shibe', 'doggo', 'pic'), '', False, True, enabled)

    def run(self):
        return functions.get_random_picture('shibes')


class Stats(Command):
    def __init__(self, enabled):
        Command.__init__(self, 'Stats', 'Displays Connected Server Information', ('stats', 'servers'), '', False, False, enabled)

    def run(self):
        serverStr = ' Server'
        if functions.get_server_count() != 1:
            serverStr += 's'
        stats_message = textformat.bold(functions.get_bot_name()) + ' is connected to ' + textformat.bold(str(functions.get_server_count()) + serverStr) + '\n'
        stats_message += 'Serving a Total of ' + textformat.bold(str(functions.get_user_count()) + ' Users') + '\n'
        stats_message += textformat.seperator()
        stats_message += functions.get_server_list()
        return stats_message


class Youtube(Command):
    def __init__(self, enabled):
        Command.__init__(self, 'Youtube', 'Searches for Youtube Videos', ('youtube', 'yt'), 'Search', True, False, enabled)

    def run(self, message):
        if message.content:
            return functions.search_youtube(message.content)
        else:
            return 'You must Enter a Search Query'


# Instances of Command Class
cmds = [Help(True), Eightball(True), Bork(True), CoinFlip(False), Roll(True), Shibe(True), Stats(True), Youtube(True)]


def help_all():
    msg = textformat.bold(functions.get_bot_name() + ' Developed by ' + config.dev_name) + '\n' + 'Prefix: ' + textformat.bold(config.prefix) + '\n'
    msg += textformat.seperator()
    for command in cmds:
        if (command.enabled):
            msg += command.help_short()
    return msg


def invalid_command():
    return 'Invalid Command! For a list of Commands type ' + textformat.bold(config.prefix + ' help')
