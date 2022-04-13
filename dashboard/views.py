from django.shortcuts import render
from django.core.paginator import Paginator
import time, hashlib, requests
import re
from dashboard.models import *
# Create your views here.

def index(request):
    return render(request,'dashboard/index.html')

def search(request, name):
    page_number = request.GET.get('page')
    element = request.GET.get('search')
    publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
    privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
    baseUrl = 'https://gateway.marvel.com/v1/public/' + str(name)
    ts = str(time.time())
    stringToHash = ts + privatekey + publickey
    hash = hashlib.md5(stringToHash.encode()).hexdigest()
    new_list = []
    if (name == "characters"):
        if(page_number==None):
            url = baseUrl + "?nameStartsWith=" + element + "&ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
            r = requests.get(url).json()['data']['results']
        else:
            offset = (int(page_number)-1) * 20
            url = baseUrl + "?nameStartsWith=" + element + "&limit=20&offset=" + str(offset) + "&ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
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

    else:
        if(page_number==None):
            url = baseUrl + "?titleStartsWith=" + element + "&ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
            r = requests.get(url).json()['data']['results']
        else:
            offset = (int(page_number)-1) * 20
            url = baseUrl + "?titleStartsWith=" + element + "&limit=20&offset=" + str(offset) + "&ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
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
        page_obj.paginator.num_pages = int(1559/20) + 1
        page_obj_temp = paginator.get_page(page_number)

    return render(request,'dashboard/search.html',{
        'page_obj': page_obj,
        'page_obj_temp': page_obj_temp,
        'name' : name,
        'element' : element
    }) 

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

def characters(request, pk):
    publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
    privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
    baseUrl = 'https://gateway.marvel.com/v1/public/characters/'+str(pk)
    ts = str(time.time())
    stringToHash = ts + privatekey + publickey
    hash = hashlib.md5(stringToHash.encode()).hexdigest()
    url = baseUrl + "?ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
    r = requests.get(url).json()['data']['results']
    try:
        for i in range(len(r[0]['comics']['items'])):
            r[0]['comics']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['comics']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['series']['items'])):
            r[0]['series']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['series']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['stories']['items'])):
            r[0]['stories']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['stories']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['events']['items'])):
            r[0]['events']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['events']['items'][i]['resourceURI'])[-1]
    except Exception as e:
        pass
    r[0]['thumbnail'] = r[0]['thumbnail']['path']+'/portrait_uncanny.'+r[0]['thumbnail']['extension']
    return render(request,'dashboard/characters.html',{
        'r' : r[0]
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

def comics(request, pk):
    publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
    privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
    baseUrl = 'https://gateway.marvel.com/v1/public/comics/'+str(pk)
    ts = str(time.time())
    stringToHash = ts + privatekey + publickey
    hash = hashlib.md5(stringToHash.encode()).hexdigest()
    url = baseUrl + "?ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
    r = requests.get(url).json()['data']['results']
    try:
        for i in range(len(r[0]['characters']['items'])):
            r[0]['characters']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['characters']['items'][i]['resourceURI'])[-1]
        r[0]['series']['resourceURI'] = re.findall(r'\d+', r[0]['series']['resourceURI'])[-1]
        for i in range(len(r[0]['stories']['items'])):
            r[0]['stories']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['stories']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['events']['items'])):
            r[0]['events']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['events']['items'][i]['resourceURI'])[-1]
    except Exception as e:
        pass
    r[0]['thumbnail'] = r[0]['thumbnail']['path']+'/portrait_uncanny.'+r[0]['thumbnail']['extension']

    return render(request,'dashboard/comics.html',{
        'r' : r[0]
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

def series(request, pk):
    publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
    privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
    baseUrl = 'https://gateway.marvel.com/v1/public/series/'+str(pk)
    ts = str(time.time())
    stringToHash = ts + privatekey + publickey
    hash = hashlib.md5(stringToHash.encode()).hexdigest()
    url = baseUrl + "?ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
    r = requests.get(url).json()['data']['results']
    try:
        for i in range(len(r[0]['characters']['items'])):
            r[0]['characters']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['characters']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['comics']['items'])):
            r[0]['comics']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['comics']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['stories']['items'])):
            r[0]['stories']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['stories']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['events']['items'])):
            r[0]['events']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['events']['items'][i]['resourceURI'])[-1]
    except Exception as e:
        pass
    r[0]['thumbnail'] = r[0]['thumbnail']['path']+'/portrait_uncanny.'+r[0]['thumbnail']['extension']
    return render(request,'dashboard/series.html',{
        'r' : r[0]
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
    
    return render(request,'dashboard/eventslist.html',{
        'page_obj': page_obj,
        'page_obj_temp': page_obj_temp
    })

def events(request, pk):
    publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
    privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
    baseUrl = 'https://gateway.marvel.com/v1/public/events/'+str(pk)
    ts = str(time.time())
    stringToHash = ts + privatekey + publickey
    hash = hashlib.md5(stringToHash.encode()).hexdigest()
    url = baseUrl + "?ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
    r = requests.get(url).json()['data']['results']
    try:
        for i in range(len(r[0]['characters']['items'])):
            r[0]['characters']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['characters']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['series']['items'])):
            r[0]['series']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['series']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['stories']['items'])):
            r[0]['stories']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['stories']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['comics']['items'])):
            r[0]['comics']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['comics']['items'][i]['resourceURI'])[-1]
    except Exception as e:
        pass
    r[0]['thumbnail'] = r[0]['thumbnail']['path']+'/portrait_uncanny.'+r[0]['thumbnail']['extension']
    return render(request,'dashboard/events.html',{
        'r' : r[0]
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
        temp['thumbnail'] = 'http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available'+'/portrait_xlarge.'+'jpg'
        temp['name'] = i['title']
        new_list.append(temp)
    paginator = Paginator(new_list, 20)
    page_obj = paginator.get_page(page_number)
    page_obj.paginator.num_pages = int(118624/20) + 1
    page_obj_temp = paginator.get_page(page_number)
    
    return render(request,'dashboard/storieslist.html',{
        'page_obj': page_obj,
        'page_obj_temp': page_obj_temp
    })

def stories(request, pk):
    publickey = '9231808ae7a4012c6aa600c80d1bfc2e'
    privatekey = '24dc7be05edc50d5053cc66ad431cb574c9049f2'
    baseUrl = 'https://gateway.marvel.com/v1/public/stories/'+str(pk)
    ts = str(time.time())
    stringToHash = ts + privatekey + publickey
    hash = hashlib.md5(stringToHash.encode()).hexdigest()
    url = baseUrl + "?ts=" + ts + "&apikey=" + publickey + "&hash=" + hash
    r = requests.get(url).json()['data']['results']
    try:
        for i in range(len(r[0]['characters']['items'])):
            r[0]['characters']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['characters']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['series']['items'])):
            r[0]['series']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['series']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['comics']['items'])):
            r[0]['comics']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['comics']['items'][i]['resourceURI'])[-1]
        for i in range(len(r[0]['events']['items'])):
            r[0]['events']['items'][i]['resourceURI'] = re.findall(r'\d+', r[0]['events']['items'][i]['resourceURI'])[-1]
    except Exception as e:
        pass
    r[0]['thumbnail'] = 'http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available'+'/portrait_xlarge.'+'jpg'
    return render(request,'dashboard/stories.html',{
        'r' : r[0]
    })