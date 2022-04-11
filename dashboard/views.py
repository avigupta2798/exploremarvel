from django.shortcuts import render
from django.core.paginator import Paginator
import time, hashlib, requests
from dashboard.api import characters_list, comics_list, series_list, events_list, stories_list
from dashboard.models import *
# Create your views here.

def index(request):
    return render(request,'dashboard/index.html')

def characterslist(request):
    publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
    privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
    baseUrl = 'https://gateway.marvel.com/v1/public/characters'
    ts = str(time.time())
    stringToHash = ts + privatekey + publickey
    hash = hashlib.md5(stringToHash.encode()).hexdigest()
    page_number = request.GET.get('page')
    new_list = []
    if(page_number==None):
        url = baseUrl + "?ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
        r = requests.get(url).json()['data']['results']
    else:
        offset = (int(page_number)-1) * 20
        url = baseUrl + "?limit=20&offset=" + str(offset) + "&ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
        r = requests.get(url).json()['data']['results']
    for i in r:
        temp = {}
        temp['id'] = i['id']
        temp['description'] = i['description']
        temp['thumbnail'] = i['thumbnail']['path']+'/portrait_xlarge.'+i['thumbnail']['extension']
        temp['name'] = i['name']
        new_list.append(temp)
    paginator = Paginator(new_list, 20)
    page_obj = paginator.get_page(page_number)
    page_obj.paginator.num_pages = int(1559/20) + 1
    page_obj_temp = paginator.get_page(page_number)

    return render(request,'dashboard/characterslist.html',{
        'page_obj': page_obj,
        'page_obj_temp': page_obj_temp
    })

def comicslist(request):
    publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
    privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
    baseUrl = 'https://gateway.marvel.com/v1/public/comics'
    ts = str(time.time())
    stringToHash = ts + privatekey + publickey
    hash = hashlib.md5(stringToHash.encode()).hexdigest()
    page_number = request.GET.get('page')
    new_list = []
    if(page_number==None):
        url = baseUrl + "?ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
        r = requests.get(url).json()['data']['results']
    else:
        offset = (int(page_number)-1) * 20
        url = baseUrl + "?limit=20&offset=" + str(offset) + "&ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
        r = requests.get(url).json()['data']['results']
    for i in r:
        temp = {}
        temp['id'] = i['id']
        temp['description'] = i['description']
        temp['thumbnail'] = i['thumbnail']['path']+'/portrait_xlarge.'+i['thumbnail']['extension']
        temp['name'] = i['title']
        new_list.append(temp)
    paginator = Paginator(new_list, 20)
    page_obj = paginator.get_page(page_number)
    page_obj.paginator.num_pages = int(51243/20) + 1
    page_obj_temp = paginator.get_page(page_number)

    return render(request,'dashboard/comicslist.html',{
        'page_obj': page_obj,
        'page_obj_temp': page_obj_temp
    })

def serieslist(request):
    publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
    privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
    baseUrl = 'https://gateway.marvel.com/v1/public/series'
    ts = str(time.time())
    stringToHash = ts + privatekey + publickey
    hash = hashlib.md5(stringToHash.encode()).hexdigest()
    page_number = request.GET.get('page')
    new_list = []
    if(page_number==None):
        url = baseUrl + "?ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
        r = requests.get(url).json()['data']['results']
    else:
        offset = (int(page_number)-1) * 20
        url = baseUrl + "?limit=20&offset=" + str(offset) + "&ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
        r = requests.get(url).json()['data']['results']
    for i in r:
        temp = {}
        temp['id'] = i['id']
        temp['description'] = i['description']
        temp['thumbnail'] = i['thumbnail']['path']+'/portrait_xlarge.'+i['thumbnail']['extension']
        temp['name'] = i['title']
        new_list.append(temp)
    paginator = Paginator(new_list, 20)
    page_obj = paginator.get_page(page_number)
    page_obj.paginator.num_pages = int(12767/20) + 1
    page_obj_temp = paginator.get_page(page_number)

    return render(request,'dashboard/serieslist.html',{
        'page_obj': page_obj,
        'page_obj_temp': page_obj_temp
    })

def eventslist(request):
    publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
    privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
    baseUrl = 'https://gateway.marvel.com/v1/public/events'
    ts = str(time.time())
    stringToHash = ts + privatekey + publickey
    hash = hashlib.md5(stringToHash.encode()).hexdigest()
    page_number = request.GET.get('page')
    new_list = []
    if(page_number==None):
        url = baseUrl + "?ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
        r = requests.get(url).json()['data']['results']
    else:
        offset = (int(page_number)-1) * 20
        url = baseUrl + "?limit=20&offset=" + str(offset) + "&ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
        r = requests.get(url).json()['data']['results']
    for i in r:
        temp = {}
        temp['id'] = i['id']
        temp['description'] = i['description']
        temp['thumbnail'] = i['thumbnail']['path']+'/portrait_xlarge.'+i['thumbnail']['extension']
        temp['name'] = i['title']
        new_list.append(temp)
    paginator = Paginator(new_list, 20)
    page_obj = paginator.get_page(page_number)
    page_obj.paginator.num_pages = int(74/20) + 1
    page_obj_temp = paginator.get_page(page_number)

    #event_list = list(events_list.list_of_events().items())
    #paginator = Paginator(event_list, 20)
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    
    return render(request,'dashboard/eventslist.html',{
        'page_obj': page_obj,
        'page_obj_temp': page_obj_temp
    })

def storieslist(request):
    publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
    privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
    baseUrl = 'https://gateway.marvel.com/v1/public/stories'
    ts = str(time.time())
    stringToHash = ts + privatekey + publickey
    hash = hashlib.md5(stringToHash.encode()).hexdigest()
    page_number = request.GET.get('page')
    new_list = []
    if(page_number==None):
        url = baseUrl + "?ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
        r = requests.get(url).json()['data']['results']
    else:
        offset = (int(page_number)-1) * 20
        url = baseUrl + "?limit=20&offset=" + str(offset) + "&ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
        r = requests.get(url).json()['data']['results']
    for i in r:
        temp = {}
        temp['id'] = i['id']
        temp['description'] = i['description']
        temp['thumbnail'] = i['thumbnail']['path']+'/portrait_xlarge.'+i['thumbnail']['extension']
        temp['name'] = i['title']
        new_list.append(temp)
    paginator = Paginator(new_list, 20)
    page_obj = paginator.get_page(page_number)
    page_obj.paginator.num_pages = int(118624/20) + 1
    page_obj_temp = paginator.get_page(page_number)

    #story_list = list(stories_list.list_of_stories().items())
    #paginator = Paginator(story_list, 20)
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    
    return render(request,'dashboard/storieslist.html',{
        'page_obj': page_obj,
        'page_obj_temp': page_obj_temp
    })
