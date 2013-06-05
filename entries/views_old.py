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
    latest_entrie_list = Entry.objects.order_by('pub_date')[:10]
    context = {'latest_entrie_list': latest_entrie_list}
    
    #import pdb; pdb.set_trace()
   
    
    return render(request, 'entries/index.html', context)
    
       

def urlify(s):
    
    #s = re.sub(r"[^\w\s]", '', s)
    s = re.sub(r"\s+", '_',s)
    
    return s




def entry(request, entry_id):
    
    
    entry = get_object_or_404(Entry, pk=entry_id)
    
    if('foo' in request.POST ):
        
        print(request.POST)
    
        #verbindung mit mediawiki
        
        
        #abfrage ob eintrag existiert
        
        title = urlify(entry.title)
        data = urllib2.urlopen('http://debian-wiki/wiki/api.php?format=json&action=query&titles='+ title +'%20&format=json')
        j = json.load(data)
        #print(j['query']['pages'])
        
        for key in j['query']['pages']:                          
        #    print(j[key])
            print(key)
            entry.location = key
            
        
        if int(entry.location)==-1:
        
            site = mwclient.Site('debian-wiki',path = '/wiki/')
            site.login('stinglsa', 'nosaer') # Optional


        
            credentials=None
        
        #setzt title nach momentanen Beitrag
        
        #title= 'robert_koch'
        
        
        #print(urlify(title))
        #pprint(medwiki._get_page(medwiki._source_wikipedia,title, credentials))
        
        #title = urlify(title)
            page = site.Pages[entry.title]
            text = page.edit()
        
        
        
        #pprint(page)
        #help(page)
            credentials = None
            print(medwiki.get_original_article(entry.title,credentials))
            print(medwiki._get_page(medwiki._source_wikipedia, title, credentials))
        #pprint(page + '2')
        #pprint(page.__str__() +'3')
        #pprint(urllib2.quote(link.encode("utf8")))
        
        #print 'Text in sandbox:', text.encode('utf-8')
            text2 = entry.content
            page.save(text + text2, summary = 'Test edit')
            
            
            
            title = urlify(entry.title)
            data = urllib2.urlopen('http://debian-wiki/wiki/api.php?format=json&action=query&titles='+ title +'%20&format=json')
            j = json.load(data)
        #print(j['query']['pages'])
        
            for key in j['query']['pages']:                          
        #    print(j[key])
            #print(key)
                entry.location = key
                entry.save()
            
        
        #print('http://debian-wiki/wiki/api.php?format=json&action=query&titles='+ title +'%20&format=json')
        
        
        
        
            rootAdr = 'debian-wiki/wiki/index.php/'
        
        
            entry.wikilink= rootAdr + title
            entry.save()
        #entry.content = 'was los hier//'
        #return render(request, 'entries/detail.html', {'entry':entry})
        
    if(request.GET):
    
        
        
        title = entry.title
        title = urlify(title)
        #print('http://debian-wiki/wiki/api.php?format=json&action=query&titles='+ title +'%20&format=json')
        data = urllib2.urlopen('http://debian-wiki/wiki/api.php?format=json&action=query&titles='+ title +'%20&format=json')
        ######jsonTest###############################
        #data = urllib2.urlopen('http://debian-wiki/wiki/api.php?format=json&action=query&titles=Apfelbrause%20&format=json')
        
        
        
        #########WORKING#############
        #creates a python dict
        j = json.load(data)
        #print(j)
        #print(j['query']['pages'])
        
        for key in j['query']['pages']:                          
        #    print(j[key])
            #print(key)
            entry.location = key
            entry.save()
        ###########END################
        
        
        #print(j)
        
        # access dict via key and array via index
        
        #print(j['query']['pages'])
        #print(j['query']['pages']['18']['pageid'])
        
        #test for array
        
        #print(j['query']['normalized'][0])
        
        #print(j['query']['pages'])
        
        
        
        
        
        #k = [i for i, j, k in j[3]]
        #l = json.dumps(k)
        
        
        
        ######END#####################################
    #entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'entries/detail.html', {'entry':entry})
    








# Create your views here.
