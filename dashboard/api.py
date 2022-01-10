import time
import hashlib
import requests


class URLCreation:
    def __init__(self, select):
        self.publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
        self.privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
        self.baseurl = 'https://gateway.marvel.com/v1/public/'+ select
        self.ts = str(time.time())
        #self.offset = '0'
    def create_url(self):
        stringToHash = self.ts + self.privatekey + self.publickey
        hash = hashlib.md5(stringToHash.encode()).hexdigest()
        list_of_url=[]
        for l in range(0,500,20):
            l = str(l)
            url = self.baseurl + "?limit=20&offset=" + l + "&ts=" + self.ts + "&apikey=" + self.publickey + "&hash=" + hash
            list_of_url.append(url)
        return list_of_url

class CharactersList:   
    def __init__(self):
        self.URL = URLCreation('characters')
        self.URL = self.URL.create_url()
    
    def list_of_characters(self):
        new_list={}
        for m in range(len(self.URL)):
            r = requests.get(self.URL[m])
            lst = r.json()['data']['results']
            for i in range(len(lst)):
                lst[i]['thumbnail']['path'] = lst[i]['thumbnail']['path']+'/portrait_xlarge.'+lst[i]['thumbnail']['extension']
                new_list[lst[i]['name']]=lst[i]['thumbnail']['path']
        return(new_list)

class ComicsList:
    def __init__(self):
        self.URL = URLCreation('comics')
        self.URL = self.URL.create_url()
    
    def list_of_comics(self):
        new_list={}
        #import pdb; pdb.set_trace()
        for m in range(len(self.URL)):
            r = requests.get(self.URL[m])
            lst = r.json()['data']['results']
            for i in range(len(lst)):
                lst[i]['thumbnail']['path'] = lst[i]['thumbnail']['path']+'/portrait_xlarge.'+lst[i]['thumbnail']['extension']
                new_list[lst[i]['title']]=lst[i]['thumbnail']['path']
        return(new_list)

class CreatersList:
    def __init__(self):
        self.URL = URLCreation('creaters')
        self.URL = self.URL.create_url()
    
    def list_of_creaters(self):
        new_list={}
        for m in range(len(self.URL)):
            r = requests.get(self.URL[m])
            lst = r.json()['data']['results']
            for i in range(len(lst)):
                lst[i]['thumbnail']['path'] = lst[i]['thumbnail']['path']+'/portrait_xlarge.'+lst[i]['thumbnail']['extension']
                new_list[lst[i]['title']]=lst[i]['thumbnail']['path']
        return(new_list)

class SeriesList:
    def __init__(self):
        self.URL = URLCreation('series')
        self.URL = self.URL.create_url()
    
    def list_of_series(self):
        new_list={}
        for m in range(len(self.URL)):
            r = requests.get(self.URL[m])
            lst = r.json()['data']['results']
            for i in range(len(lst)):
                lst[i]['thumbnail']['path'] = lst[i]['thumbnail']['path']+'/portrait_xlarge.'+lst[i]['thumbnail']['extension']
                new_list[lst[i]['title']]=lst[i]['thumbnail']['path']
        return(new_list)

class EventsList:
    def __init__(self):
        self.URL = URLCreation('events')
        self.URL = self.URL.create_url()
    
    def list_of_events(self):
        new_list={}
        for m in range(len(self.URL)):
            r = requests.get(self.URL[m])
            lst = r.json()['data']['results']
            for i in range(len(lst)):
                lst[i]['thumbnail']['path'] = lst[i]['thumbnail']['path']+'/portrait_xlarge.'+lst[i]['thumbnail']['extension']
                new_list[lst[i]['title']]=lst[i]['thumbnail']['path']
        return(new_list)

class StoriesList:
    def __init__(self):
        self.URL = URLCreation('stories')
        self.URL = self.URL.create_url()
    
    def list_of_stories(self):
        new_list={}
        for m in range(len(self.URL)):
            r = requests.get(self.URL[m])
            lst = r.json()['data']['results']
            for i in range(len(lst)):
                lst[i]['thumbnail']['path'] = lst[i]['thumbnail']['path']+'/portrait_xlarge.'+lst[i]['thumbnail']['extension']
                new_list[lst[i]['title']]=lst[i]['thumbnail']['path']
        return(new_list)

'''lst = [
    'characters',
    'comics',
#    'creaters',
    'series',
    'events',
    'stories'
]
url_list_temp = []
url_list = {}
for k in range(len(lst)):
    URL = URLCreation(lst[k])
    URL_Created = URL.create_url()
    url_list_temp.append(URL_Created)

for q in range(len(url_list_temp)):
    url_list[lst[q]+'_URL']=url_list_temp[q]'''

characters_list = CharactersList()
comics_list = ComicsList()
creaters_list = CreatersList()
series_list = SeriesList()
events_list = EventsList()
stories_list = StoriesList()


#print(characters_list.list_of_characters().keys())
#print(comics_list.list_of_comics())
#print(creaters_list.list_of_creaters())
#print(series_list.list_of_series())
#print(events_list.list_of_events())
#print(stories_list.list_of_stories())