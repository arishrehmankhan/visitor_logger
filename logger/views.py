import json
import mimetypes
import os

from django.shortcuts import render
from django.core import serializers
from .models import Log
from django.http import HttpResponse
from django.db.models import Count

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