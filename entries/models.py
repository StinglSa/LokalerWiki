from django.db import models
from django.utils import timezone 
import datetime

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    location = models.CharField(max_length=30)
    wikilink = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title