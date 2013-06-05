from entries.models import Entry
from entries import medwiki
from django.shortcuts import render, get_object_or_404
import mwclient
from pprint import pprint
from django.http import HttpRequest
import urllib, urllib2, cookielib
import json
import re




def index(request):
    latest_entrie_list = Entry.objects.order_by('pub_date')[:20]
    context = {'latest_entrie_list': latest_entrie_list}

    return render(request, 'entries/index.html', context)
    
       
def urlify(s):
    
    s = re.sub(r"\s+", '_',s)
    
    return s


def entry(request, entry_id):
    
    
    entry = get_object_or_404(Entry, pk=entry_id)
    
    if('save' in request.POST ):
        
        print(request.POST)
        
        title = urlify(entry.title)
        data = urllib2.urlopen('http://debian-wiki/wiki/api.php?format=json&action=query&titles='+ title +'%20&format=json')
        j = json.load(data)
       
        
        for key in j['query']['pages']:                          
        
            print(key)
            entry.location = key
            
        
        if int(entry.location)==-1:
        
            site = mwclient.Site('debian-wiki',path = '/wiki/')
            site.login('stinglsa', 'nosaer') # Optional

            credentials=None
        
            page = site.Pages[entry.title]
            text = page.edit()
        
            credentials = None
            print(medwiki.get_original_article(entry.title,credentials))
            print(medwiki._get_page(medwiki._source_wikipedia, title, credentials))
    
            text2 = entry.content
            page.save(text + text2, summary = 'Test edit')
            
            title = urlify(entry.title)
            data = urllib2.urlopen('http://debian-wiki/wiki/api.php?format=json&action=query&titles='+ title +'%20&format=json')
            j = json.load(data)
        
            for key in j['query']['pages']:                          
       
                entry.location = key
                entry.save()
            
            rootAdr = 'debian-wiki/wiki/index.php/'
        
            entry.wikilink= rootAdr + title
            entry.save()
        
    if(request.GET):
    
        title = entry.title
        title = urlify(title)
       
        data = urllib2.urlopen('http://debian-wiki/wiki/api.php?format=json&action=query&titles='+ title +'%20&format=json')
        
        #########WORKING#############
        #creates a python dict
        j = json.load(data)
        
        
        for key in j['query']['pages']:                          
        
            entry.location = key
            entry.save()
        ###########END################
        
        
      
    return render(request, 'entries/detail.html', {'entry':entry})
    








# Create your views here.
