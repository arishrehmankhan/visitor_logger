from django.db import models

class Log(models.Model):
    path_info = models.CharField(max_length=1023)
    browser_info = models.CharField(max_length=255)
    request_data = models.CharField(max_length=2047)
    method = models.CharField(max_length=6)
    event_name = models.CharField(max_length=1023)
    visited_by = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.path_info
