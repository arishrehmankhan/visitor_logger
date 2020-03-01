"""visitor_logger_beta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from logger import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls), # to handle admin pages
    path('homepage/', views.index, name="home"), # to serve homepage
    path('graph_data/', views.graphData, name="graph-data"), # to serve data for graph of dashboard
    path('request_on_date/', views.requestsOnDate, name="request-on-date"), # to get number of requests at particular date
    path('requests_between_dates/', views.requestsBetweenDates, name="request-between-dates"), # to get number of requests between two dates
    path('requests_from_countries/', views.requestsFromCountry, name="request-from-countries"), # to get number of requests from different locations (countries)
    path('dashboard/', views.dashboard, name="dashboard"), # to serve dashboard page
    path('file/', views.jsonData, name="get-json-data"), # to send json file
    path('', RedirectView.as_view(url='homepage/', permanent=True)), # redirect / to homepage
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # to server static files
