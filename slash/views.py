from slash_util import *
from django.http import JsonResponse 
import json
import urllib2
import requests

def index(request):
    response = {}
    text = request.POST['text']

    search_string = 'https://sites.google.com/feeds/content/site/juwaini?alt=json&q=%s' % (stringQuery(text))
    
    r = requests.get(search_string)
    return JsonResponse(returnPayload(r), safe=False)
