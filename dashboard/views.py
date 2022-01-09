from django.shortcuts import render
from dashboard.api import characters_list, comics_list, series_list, events_list, stories_list
# Create your views here.

def index(request):
    return render(request,'dashboard/index.html')

def characterslist(request):
    return render(request,'dashboard/characterslist.html',{"characters_list":characters_list.list_of_characters()})

def comicslist(request):
    return render(request,'dashboard/comicslist.html',{"comics_list":comics_list.list_of_comics()})

def serieslist(request):
    return render(request,'dashboard/serieslist.html',{"series_list":series_list.list_of_series()})

def eventslist(request):
    return render(request,'dashboard/eventslist.html',{"events_list":events_list.list_of_events()})

def storieslist(request):
    return render(request,'dashboard/storieslist.html',{"stories_list":stories_list.list_of_stories()})