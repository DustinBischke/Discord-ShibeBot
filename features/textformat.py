# Returns Text in Italic
def italic(text):
    return '*' + text + '*'


# Returns Text in Bold
def bold(text):
    return '**' + text + '**'


# Returns Text in Bold and Italic
def bolditalic(text):
    return '***' + text + '***'


# Returns a Seperator Line
def seperator():
    return bold('-' * 40) + '\n'
