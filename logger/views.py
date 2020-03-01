import json
import mimetypes
import os

from django.shortcuts import render
from django.core import serializers
from .models import Log
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from datetime import date, datetime, timedelta
from django.db.models import Count, Q

# This view saves all logs to a file the serves the file
def jsonData(request):

    # Writing logs to the file 'logs.json'
    logs = Log.objects.all()
    with open('logs.json', "w") as out:
        logs_json = serializers.serialize("json", logs)
        out.write(logs_json)
        
    # sending file to user
    file_path = 'logs.json'

    file = open(file_path, 'r')
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(file, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % file_path

    size = os.path.getsize(file_path)
    response['Content-Length'] = size

    return response


# This view serves the homepage
def index(request):

    # number of time a user visits the homepage
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits
    }

    return render(request, 'homepage.html', context)

def dashboard(request):
    total_requests = Log.objects.all().count() 
    total_anonymous_requests = Log.objects.filter(visited_by='').count()
    total_signed_in_requests = total_requests - total_anonymous_requests
    total_signed_in_users = Log.objects.values('visited_by').distinct().count() - 1 # -1 to discard anonymous users
    
    # if there are no authenticated users, total_signed_in_users will be -1
    if total_signed_in_users == -1:
        total_signed_in_users = 0
    
    total_requests_today = Log.objects.filter(timestamp__contains=date.today()).count()

    todays_date = datetime.today()
    week_before_date = datetime.today() - timedelta(days=7)
    
    # get number of requests of last 7 days
    total_requests_in_previous_week = Log.objects.filter(Q(timestamp__gte=week_before_date)&Q(timestamp__lte=todays_date)).count()
    
    # get diffents countries stored in database
    countries = Log.objects.values('location_country').distinct()

    context = {
        'total_requests': total_requests,
        'total_signed_in_requests': total_signed_in_requests,
        'total_anonymous_requests': total_anonymous_requests,
        'todays_date': todays_date.strftime("%Y-%m-%d"),
        'total_signed_in_users': total_signed_in_users,
        'total_requests_today': total_requests_today,
        'week_before_date': week_before_date.strftime("%Y-%m-%d"),
        'total_requests_in_previous_week': total_requests_in_previous_week,
        'countries': countries,
    }
    return render(request, 'dashboard.html', context)

# this view serves the data required to plot graph on dashboard
def graphData(request):
    # Getting data
    obj = Log.objects.extra({'timestamp' : "date(timestamp)"}).values('timestamp').annotate(total=Count('id'))
    data = json.dumps(list(obj), cls=DjangoJSONEncoder) # converting data to json
    return JsonResponse(data, safe=False) # sending data

# this view returns the number of requests of particular date
def requestsOnDate(request):
    # Getting data
    requests_on_date = Log.objects.filter(timestamp__contains=request.GET['date']).count()
    return JsonResponse({'requests_on_date': requests_on_date }, safe=False) # sending data

# this view returns the number of requests between two dates
def requestsBetweenDates(request):
    from_date = request.GET['from_date']
    to_date = request.GET['to_date']
    # Getting data
    requests_between_dates = Log.objects.filter(Q(timestamp__gte=from_date)&Q(timestamp__lte=to_date)).count()
    return JsonResponse({'requests_between_dates': requests_between_dates }, safe=False) # sending data

# this view reuturns the number of requests came from different countries
def requestsFromCountry(request):
    country = request.GET['country']
    # Getting data
    requests_from_countries = Log.objects.filter(location_country=country).count()
    return JsonResponse({'requests_from_countries': requests_from_countries}, safe=False) # sending data