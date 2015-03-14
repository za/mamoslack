from slash_util import *
from django.http import JsonResponse 
import json
import urllib2
import requests

def index(request):
    response = {}
    text = request.POST['text']
    key = 'AIzaSyAv6O_Iv5OuQ7LJLokhZdXOuCKT8ypYkYo'
    cx = '016192506177346845611:nf3fvowvnke'

    search_string = 'https://www.googleapis.com/customsearch/v1?cx=%s&q=%s&key=%s' % (cx, stringQuery(text), key)
    response['text'] = search_string
    
    r = requests.get(search_string)
    response['return'] = r.text
    return JsonResponse(returnPayload(r), safe=False)
