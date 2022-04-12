"""exploremarvel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characterslist/', views.characterslist, name='characterslist'),
    path('characters/<int:pk>/', views.characters, name='characters'),
    path('comicslist/', views.comicslist, name='comicslist'),
    path('comics/<int:pk>/', views.comics, name='comics'),
    path('serieslist/', views.serieslist, name='serieslist'),
    path('series/<int:pk>/', views.series, name='series'),
    path('eventslist/', views.eventslist, name='eventslist'),
    path('events/<int:pk>/', views.events, name='events'),
    path('storieslist/', views.storieslist, name='storieslist'),
    path('stories/<int:pk>/', views.stories, name='stories'),
    path('admin/', admin.site.urls),
]
