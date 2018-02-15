import math
import random
from features import functions, textformat
from settings import *

client = functions.client


class Command:
    def __init__(self, name, desc, aliases, args, sendsFile, enabled):
        self.name = name
        self.desc = desc
        self.aliases = aliases
        self.args = args
        self.sendsFile = sendsFile
        self.enabled = enabled

    def help_short(self):
        return textformat.bold(self.name) + ' - ' + self.desc

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
                    command_args += ', '
        command_usage = 'Usage: ' + config.prefix + ' ' + self.name.lower() + ' ' + command_args
        command_desc = 'Description: ' + self.desc
        command_aliases = 'Aliases: ' + str(self.aliases)
        return command_name + '\n' + command_usage + '\n' + command_desc + '\n' + command_aliases

    def run(self, message):
        return


class Help(Command):
    def __init__(self):
        Command.__init__(self, 'Help', 'Shows Bot Information and Commands', ('help', 'about', 'commands'), 'Command', False, config.help)

    def run(self, message):
        if not message.content:
            return help_all()
        else:
            for command in cmds:
                # If Command Exists, Print Longer Help
                if message.content.startswith(command.aliases):
                    return command.help_long()
            # If Command doesn't Exist
            return invalid_command()


class Bork(Command):
    def __init__(self):
        Command.__init__(self, 'Bork', 'Does a Heckin Bork', ('bork', 'woof', 'speak'), '', False, config.bork)

    def run(self, message):
        return textformat.bold('BORK ' * random.randint(1, 200))


class CoinFlip(Command):
    def __init__(self):
        Command.__init__(self, 'CoinFlip', 'Flips a Coin Revealing Heads or Tails', ('coinflip', 'flipcoin', 'headsortails'), '', False, config.coinflip)

    def run(self, message):
        return random.choice(['Heads', 'Tails'])


class Eightball(Command):
    def __init__(self):
        Command.__init__(self, '8ball', 'Answers Yes/No Questions', ('8ball', 'ask', 'yesorno'), 'Question', False, config.eightball)

    def run(self, message):
        if message.content:
            answers = ['It is certain!', 'It is decidedly so!', 'Without a doubt!', 'Yes definitely!', 'You may rely on it!', 'As I see it yes!', 'Most likely!', 'Outlook good!', 'Yes!', 'Signs point to yes!', 'Reply hazy try again!', 'Ask again later!', 'Better not tell you now!', 'Cannot predict now!', 'Concentrate and ask again!', "Don't count on it!", 'My reply is no!', 'My sources say no!', 'Outlook not so good!', 'Very doubtful!']
            return random.choice(answers)
        else:
            return 'You must enter a Yes/No Question'


class FuckMarryKill(Command):
    def __init__(self):
        Command.__init__(self, 'FuckMarryKill', 'Tells who to Fuck, Marry, and Kill', ('fuckmarrykill', 'fmk'), ('P1', 'P2', 'P3'), False, config.fuckmarrykill)

    def run(self, message):
        words = message.content.split(',')
        random.shuffle(words)
        return textformat.bold('Fuck: ') + words[0].strip() + textformat.bold(' Marry: ') + words[1].strip() + textformat.bold(' Kill: ') + words[2].strip()


class Giphy(Command):
    def __init__(self):
        Command.__init__(self, 'Giphy', 'Searches Giphy for Reaction GIFs', ('giphy', 'gif'), 'Search', False, config.giphy)

    def run(self, message):
        if message.content:
            return functions.get_random_giphy(message.content)
        else:
            return 'You must Enter a Search Query'


class LoveCalc(Command):
    def __init__(self):
        Command.__init__(self, 'LoveCalc', 'Calculates Love between 2 Users', ('lovecalc', 'love'), ('Name1', 'Name2'), False, config.lovecalc)

    def run(self, message):
        users = message.content.split(',')
        if len(users) >= 2:
            love = random.randint(0, 100)
            emojis = {0: ':broken_heart:', 10: ':disappointed_relieved:', 20: ':worried:', 30: ':frowning:', 40: ':neutral_face:', 50: ':wink:', 60: ':smirk:', 70: ':hearts:', 80: ':revolving_hearts:', 90: ':sparkling_heart:', 100: ':gift_heart: :sparkling_heart: :heartpulse: :sparkling_heart: :gift_heart:'}
            # Rounds Down to Nearest 10 to select Emoji from Dictionary
            emoji = emojis.get(math.floor(love / 10) * 10)
            return textformat.bold(str(love) + '%') + ' Love Between ' + users[0].title().strip() + ' and ' + users[1].title().strip() + ' ' + emoji
        else:
            return 'You must Enter Exactly 2 People'


class Members(Command):
    def __init__(self):
        Command.__init__(self, 'Members', 'Shows Member Count of Server', ('members', 'users'), '', False, config.members)

    def run(self, message):
        msg = message.server.name + ' has ' + textformat.bold(str(functions.get_user_count(message.server))) + ' Members'
        return msg


class Roll(Command):
    def __init__(self):
        Command.__init__(self, 'Roll', 'Rolls a Random Number', ('roll', 'randomnumber'), 'Max', False, config.roll)

    def run(self, message):
        if message.content:
            if message.content.isdigit() and int(message.content) > 1:
                return random.randint(1, int(message.content))
            else:
                return 'Invalid Max Number Entered'
        else:
            return random.randint(1, 10)


class Shibe(Command):
    def __init__(self):
        Command.__init__(self, 'Shibe', 'Sends a Cute Shibe Picture', ('shibe', 'doggo', 'pic'), '', True, config.shibe)

    def run(self, message):
        return functions.get_random_picture('shibes')


class Stats(Command):
    def __init__(self):
        Command.__init__(self, 'Stats', 'Shows Connected Server Information', ('stats', 'servers'), '', False, config.stats)

    def run(self, message):
        serverStr = ' Server'
        if functions.get_server_count() != 1:
            serverStr += 's'
        stats_message = textformat.bold(functions.get_bot_name()) + ' is connected to ' + textformat.bold(str(functions.get_server_count()) + serverStr) + '\n'
        stats_message += 'Serving a Total of ' + textformat.bold(str(functions.get_total_user_count()) + ' Users') + '\n'
        stats_message += textformat.seperator()
        stats_message += functions.get_server_list()
        return stats_message


class Youtube(Command):
    def __init__(self):
        Command.__init__(self, 'Youtube', 'Searches Youtube for Videos', ('youtube', 'yt'), 'Search', False, config.youtube)

    def run(self, message):
        if message.content:
            return functions.search_youtube(message.content)
        else:
            return 'You must Enter a Search Query'


# Instances of Command Class
cmds = [Help(), Eightball(), Bork(), CoinFlip(), FuckMarryKill(), Giphy(), LoveCalc(), Members(), Roll(), Shibe(), Stats(), Youtube()]


def help_all():
    msg = textformat.bold(functions.get_bot_name() + ' Developed by ' + config.dev_name) + '\n' + 'Prefix: ' + textformat.bold(config.prefix) + '\n'
    msg += textformat.seperator()
    for command in cmds:
        if (command.enabled):
            msg += command.help_short() + '\n'
    return msg


# Returns Message if Invalid Command Entered
def invalid_command():
    return 'Invalid Command! For a list of Commands type ' + textformat.bold(config.prefix + ' help')
