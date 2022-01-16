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

class CharactersImport:
    def __init__(self, kwargs):
        self.URL = URLCreation('characters')
        self.URL = self.URL.create_url(kwargs)

    def import_characters(self):
        characters_url = self.URL
        for url in characters_url:
            r = requests.get(url)
            characters = r.json()['data']['results']
            print(url)
            for i in characters:
                i['thumbnail']['path'] = i['thumbnail']['path']+'/portrait_xlarge.'+i['thumbnail']['extension']
                characters_data = Characters(
                    id = i['id'],
                    name = i['name'],
                    description = i['description'],
                    char_thumbnail_path = i['thumbnail']['path']
                )
                characters_data.save()
  
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        kwargs={}
        start_range = int(input('Enter Start Range: '))
        end_range = int(input('Enter End Range: '))
        kwargs['start_range'] = start_range
        kwargs['end_range'] = end_range
        character_import = CharactersImport(kwargs)
        character_import.import_characters()