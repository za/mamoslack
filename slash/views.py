from django.http import HttpResponse

def index(request):
    token = request.GET['token']
    team_id = request.GET['team_id']
    team_domain = request.GET['team_domain']
    channel_id = request.GET['channel_id']
    channel_name = request.GET['channel_name']
    user_id = request.GET['user_id']
    user_name = request.GET['user_name']
    response_string = request.GET
    return HttpResponse(response_string)
