import random
from features import functions, textformat
from settings import *


class Command:
    def __init__(self, name, desc, alias, acceptsInput, sendsFile, enabled):
        self.name = name
        self.desc = desc
        self.alias = alias
        self.acceptsInput = acceptsInput
        self.sendsFile = sendsFile
        self.enabled = enabled

    def help(self):
        cmdStr = textformat.bold(self.name)
        descStr = '    ' + self.desc
        aliasStr = textformat.italic(str(self.alias))
        return cmdStr + ' - ' + aliasStr + '\n' + descStr + '\n'

    def run(self):
        return


class Help(Command):
    def __init__(self, enabled):
        Command.__init__(self, 'Help', 'Displays Bot Information', ('help', 'about', 'commands', 'cmd'), False, False, enabled)

    def run(self):
        return runHelp()


class Bork(Command):
    def __init__(self, enabled):
        Command.__init__(self, 'Bork', 'Does a Heckin Bork', ('bork', 'woof', 'speak'), False, False, enabled)

    def run(self):
        message = textformat.bold('BORK ' * functions.getRandomNumber(1, 200))
        return message


class Eightball(Command):
    def __init__(self, enabled):
        Command.__init__(self, '8ball', 'Answers Yes/No Questions', ('8ball', 'eightball', 'ask', 'yesorno'), True, False, enabled)

    def run(self, msg):
        if functions.checkMessageNotEmpty(msg, self.alias):
            answers = ['It is certain!', 'It is decidedly so!', 'Without a doubt!', 'Yes definitely!', 'You may rely on it!', 'As I see it yes!', 'Most likely!', 'Outlook good!', 'Yes!', 'Signs point to yes!', 'Reply hazy try again!', 'Ask again later!', 'Better not tell you now!', 'Cannot predict now!', 'Concentrate and ask again!', "Don't count on it!", 'My reply is no!', 'My sources say no!', 'Outlook not so good!', 'Very doubtful!']
            return random.choice(answers)
        else:
            return 'You must enter a Yes/No Question'


class Shibe(Command):
    def __init__(self, enabled):
        Command.__init__(self, 'Shibe', 'Sends a Cute Shibe Picture', ('shibe', 'doggo', 'pic'), False, True, enabled)

    def run(self):
        return functions.getRandomImage('shibes')


# Instances of Command Class
cmds = [Help(True), Bork(True), Eightball(True), Shibe(True)]


def runHelp():
    msg = textformat.bold('ShibeBot Developed by Silver#4636') + '\n' + 'Prefix: ' + textformat.bold(config.prefix) + '\n'
    for cmd in cmds:
        if (cmd.enabled):
            msg += cmd.help()
    return msg


def invalid():
    return 'Invalid Command! For a list of Commands type ' + textformat.bold(config.prefix + ' help')
