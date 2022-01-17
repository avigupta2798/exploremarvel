from django.shortcuts import render
from django.core.paginator import Paginator
from dashboard.api import characters_list, comics_list, series_list, events_list, stories_list
from dashboard.models import *
# Create your views here.

def index(request):
    return render(request,'dashboard/index.html')

def characterslist(request):
    #character_list = list(characters_list.list_of_characters().items())
    character_list = Characters.objects.all().order_by('name')
    paginator = Paginator(character_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'dashboard/characterslist.html',{
        'page_obj': page_obj
    })

def comicslist(request):
    comic_list = list(comics_list.list_of_comics().items())
    paginator = Paginator(comic_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'dashboard/comicslist.html',{
        'page_obj': page_obj
    })

def serieslist(request):
    serie_list = list(series_list.list_of_series().items())
    paginator = Paginator(serie_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'dashboard/serieslist.html',{
        'page_obj': page_obj
    })

def eventslist(request):
    event_list = list(events_list.list_of_events().items())
    paginator = Paginator(event_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'dashboard/eventslist.html',{
        'page_obj': page_obj
    })

def storieslist(request):
    story_list = list(stories_list.list_of_stories().items())
    paginator = Paginator(story_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'dashboard/storieslist.html',{
        'page_obj': page_obj
    })
