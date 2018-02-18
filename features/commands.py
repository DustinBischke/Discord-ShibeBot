import math
import random
from features import functions, textformat
from settings import config


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


class Cleverbot(Command):
    def __init__(self):
        Command.__init__(self, 'Cleverbot', 'Chat with Cleverbot AI', ('cleverbot', 'chat'), 'Message', False, config.cleverbot)

    def run(self, message):
        if message.content:
            return functions.get_cleverbot_response(message.content)
        else:
            return 'You must enter a Message'


class CoinFlip(Command):
    random_outcomes = (
        'Wow! It landed on its side', 'Oops, it rolled under the bed', 'Oops, it fell in a crack',
        'Oops, it rolled down the drain', 'Oops, it slipped through a void to the fifth dimension',
        'In the multiverse, the coin is both heads, tails, and non-existent simultaneously'
    )

    def __init__(self):
        Command.__init__(self, 'CoinFlip', 'Flips a Coin Revealing Heads or Tails', ('coinflip', 'flipcoin', 'coin'), '', False, config.coinflip)

    def run(self, message):
        flip = random.randint(1, 501)
        if flip > 0 and flip <= 250:
            result = 'Heads!'
        elif flip > 250 and flip <= 500:
            result = 'Tails!'
        else:
            result = random.choice(self.random_outcomes)
        return 'Flipping a Coin... ' + textformat.bold(result)


class Eightball(Command):
    answers_positive = (
        'It is certain!', 'It is decidedly so!', 'Without a doubt!', 'Yes definitely!',
        'You may rely on it!', 'As I see it yes!', 'Most likely!', 'Outlook good!', 'Yes!',
        'Signs point to yes!'
    )
    answers_negative = (
        "Don't count on it!", 'My reply is no!', 'My sources say no!',
        'Outlook not so good!', 'Very doubtful!'
    )
    answers_nocommit = (
        'Reply hazy try again!', 'Ask again later!', 'Better not tell you now!',
        'Cannot predict now!', 'Concentrate and ask again!'
    )

    def __init__(self):
        Command.__init__(self, '8ball', 'Answers Yes/No Questions', ('8ball', 'ask', 'yesorno'), 'Question', False, config.eightball)

    def run(self, message):
        if message.content:
            value = random.randint(1, 100)
            if value > 0 and value <= 50:
                return random.choice(self.answers_positive)
            elif value > 50 and value <= 90:
                return random.choice(self.answers_negative)
            else:
                return random.choice(self.answers_nocommit)
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


class Invite(Command):
    def __init__(self):
        Command.__init__(self, 'Invite', 'Sends the Bot Invite URL', 'invite', '', False, config.invite)

    def run(self, message):
        return functions.get_bot_invite()


class LoveCalc(Command):
    emojis = {
        -1: ':broken_heart: :sob: :broken_heart: :sob: :broken_heart:', 0: ':broken_heart:',
        5: ':sob:', 10: ':cry:', 15: ':disappointed_relieved:', 20: ':worried:', 25: ':anguished:',
        30: ':frowning:', 35: 'confused', 40: ':neutral_face:', 45: ':slight_smile:',
        50: ':grinning:', 55: ':wink:', 60: ':smirk:', 65: ':kissing_heart:', 70: ':heart_eyes:',
        75: ':hearts:', 80: ':sparkling_heart:', 85: ':gift_heart:', 90: ':two_hearts:',
        95: ':revolving_hearts:', 100: ':heartpulse:',
        101: ':sparkling_heart: :revolving_hearts: :heartpulse: :revolving_hearts: :sparkling_heart:'
    }

    def __init__(self):
        Command.__init__(self, 'LoveCalc', 'Calculates Love between 2 Users', ('lovecalc', 'love'), ('Name1', 'Name2'), False, config.lovecalc)

    def getLoveEmoji(self, value):
        if value > 0 and value < 100:
            if value % 5 == 0:
                return self.emojis.get(value)
            else:
                # Rounds Down to Nearest 5 to select Emoji from Dictionary
                return self.emojis.get(math.floor(value / 5) * 5)
        else:
            return self.emojis.get(value)

    def run(self, message):
        # If only 2 Words, Split at Space
        if len(message.content.split()) == 2:
            users = message.content.split()
        else:
            users = message.content.split(',')
        if len(users) >= 2:
            love = random.randint(-1, 101)
            emoji = self.getLoveEmoji(love)
            return textformat.bold(str(love) + '%') + ' Love Between ' + users[0].title().strip() + ' and ' + users[1].title().strip() + ' ' + emoji
        else:
            return 'You must Enter Exactly 2 People. If more than 2 Words, Split with a Comma'


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

    def run(self):
        return functions.get_random_image('shibes')


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
            return functions.get_youtube_search_result(message.content)
        else:
            return 'You must Enter a Search Query'


# Instances of Command Class
cmds = [
    Help(), Eightball(), Bork(), Cleverbot(), CoinFlip(), FuckMarryKill(), Giphy(), Invite(),
    LoveCalc(), Members(), Roll(), Shibe(), Stats(), Youtube()
]


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
