def isSearch(text):
    "To check the existence of keyword 'search' at the beginning of 'text'"
    words = text.split()
    if len(words) == 0:
        return False
    elif words[0] == 'search':
        return True
    else:
        return False

def isCache(text):
    "To check the existence of option '--no-cache' at the end of the 'text'"
    words = text.split()
    if len(words) == 0:
        return False
    elif words[-1] == '--no-cache':
        return False
    else:
        return True

def stringQuery(text):
    "To build the parameter 'q' in search query"
    return_string = ''
    words = text.split()

    if isSearch(text):
        words = words[1:]

    if isCache(text) == False:
        words.pop()

    if len(words) == 0:
        return return_string
    elif len(words) == 1:
        return_string += words[0]
        return return_string
    else:
        for x in range(0, len(words)-1):
            return_string += words[x]
            if x != len(words)-1:
                return_string += '+'
        return return_string
