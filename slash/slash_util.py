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
        for x in range(0, len(words)):
            return_string += words[x]
            if x != len(words)-1:
                return_string += '+'
        return return_string
    
def returnPayload(search_result):
    "To process and return payload to Slack"
    payload_string = {} 
    payload_string['searchResult'] = []
    r = search_result.json()
    totalResults = int(r['searchInformation']['formattedTotalResults'])
    payload_string['totalResults'] = totalResults

    for x in range(0, totalResults):
        tempData = {}
        tempData['formattedUrl'] = r['items'][x]['formattedUrl']
        tempData['htmlSnippet'] = r['items'][x]['htmlSnippet']
        payload_string['searchResult'].append(tempData)

    return payload_string
