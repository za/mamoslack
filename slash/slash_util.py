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
            if x != len(words)-1 and x != 0:
                return_string += '+'
        return return_string
    
def getCorrectUrl(list_of_url):
    "To find the correct url and return it"
    url_total = len(list_of_url)
    for x in range (0, url_total):
        if list_of_url[x]['rel'] == 'alternate' and list_of_url[x]['type'] == 'text/html':
            return list_of_url[x]['href']

def returnPayload(search_result):
    "To process and return payload to Slack"
    payload_string = {} 
    payload_string['searchResult'] = []
    r = search_result.json()
    totalResults = len(r['feed']['entry']) 
    payload_string['totalResults'] = 0 

    for x in range(0, totalResults):
        tempData = {}
        tempData['title'] = r['feed']['entry'][x]['title']['$t']

        if tempData['title'] == '':
            continue
        else:
            tempData['url'] = getCorrectUrl(r['feed']['entry'][x]['link'])
            #tempData['url'] = r['feed']['entry'][x]['link'][0]['href']
            payload_string['searchResult'].append(tempData)
            payload_string['totalResults'] += 1

    return payload_string
