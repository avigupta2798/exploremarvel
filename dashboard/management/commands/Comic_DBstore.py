from django.core.management.base import BaseCommand
import time
import hashlib
import requests
from dashboard.models import *

class URLCreation:
    def __init__(self, select):
        self.publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
        self.privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
        self.baseurl = 'https://gateway.marvel.com/v1/public/'+ select
        self.ts = str(time.time())
    def create_url(self, kwargs):
        stringToHash = self.ts + self.privatekey + self.publickey
        hash = hashlib.md5(stringToHash.encode()).hexdigest()
        list_of_url=[]
        for l in range(kwargs['start_range'],kwargs['end_range'],100):
            l = str(l)
            url = self.baseurl + "?limit=100&offset=" + l + "&ts=" + self.ts + "&apikey=" + self.publickey + "&hash=" + hash
            list_of_url.append(url)
        return list_of_url

class ComicsImport:
    def __init__(self, kwargs):
        self.URL = URLCreation('comics')
        self.URL = self.URL.create_url(kwargs)

    def import_comics(self):
        comics_url = self.URL
        for url in comics_url:
            ComicsImport.temp = url.partition('&ts')[0].rsplit('=', 1)[-1]
            r = requests.get(url)
            comics = r.json()
            comics = comics['data']
            comics = comics['results']
            print(url)
            for i in comics:
                i['thumbnail']['path'] = i['thumbnail']['path']+'/portrait_xlarge.'+i['thumbnail']['extension']
                comics_data = Comic(
                    id = i['id'], 
                    title = i['title'], 
                    description = i['description'], 
                    issueNumber = i['issueNumber'], 
                    comic_thumbnail_path = i['thumbnail']['path']
                )
                comics_data.save()
class Command(BaseCommand, ComicsImport):

    def handle(self, *args, **options):
        kwargs={}
        start_range = int(input('Enter Start Range: '))
        end_range = int(input('Enter End Range: '))
        try:
            kwargs['start_range'] = start_range
            kwargs['end_range'] = end_range
            comics_import = ComicsImport(kwargs)
            comics_import.import_comics()
        except Exception as e:
            print("\nwent to exception\n")
            kwargs['start_range'] = int(ComicsImport.temp)
            kwargs['end_range'] = end_range
            comics_import = ComicsImport(kwargs)
            comics_import.import_comics()