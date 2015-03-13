
def isSearch(text):
    words = text.split()
    if len(words) == 0:
        return False
    elif words[0] == 'search':
        return True
    else:
        return False

def isCache(text):
    words = text.split()
    if len(words) == 0:
        return False
    elif words[-1] == '--no-cache':
        return False
    else:
        return True
