from django.http import JsonResponse 
import json

def index(request):
    response_data = {}
    response_data['token'] = request.POST['token']
    return JsonResponse(response_data)
