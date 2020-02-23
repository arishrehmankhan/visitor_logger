import datetime
from django.utils.deprecation import MiddlewareMixin
from .models import Log
from .IPAddressLocation import getGeoData

class LogEntry(MiddlewareMixin):
    def process_request(self, request):
        
        new_log = Log()
        
        new_log.path_info = request.path_info
        new_log.browser_info = request.headers['User-Agent']
        method = request.method

        new_log.method = method 
        
        new_log.request_data = request.GET.dict() if method == 'GET' else request.POST.dict()
        new_log.event_name = f'{request.method} {request.path_info}' # enent name is request method and path url requested

        ip_address = request.META['REMOTE_ADDR'] # ip address of the request

        # getting the location of request
        # getGeoData(ip) return list of Geolocation data such as city, region, country, etc
        # all the data which it returns can be found here : https://ipwhois.io/documentation
        geoData = getGeoData(ip_address) 

        # Extracting address from returned data
        city = geoData['city']
        region = geoData['region']
        country = geoData['country']

        new_log.location = f'{city}, {region}, {country}' # location of request
        new_log.ip_address = ip_address
        new_log.timestamp = datetime.datetime.now() # time of request

        # checking if user is logged in or not
        # if user is not logged in, request.user contains 'AnonymousUser'
        new_log.visited_by = '' if str(request.user) == str('AnonymousUser') else request.user
        
        new_log.save() # saving log entry into the database