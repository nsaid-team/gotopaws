"""nsaid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', views.test),
    url(r'^$', views.home),
    url(r'^Home.html$', views.home),
    url(r'^Shelters.html$', views.shelters),
    url(r'^Pets.html$', views.pets),
    url(r'^Cities.html$', views.cities),
    url(r'^About.html$', views.about),
    url(r'^Cats.html$', views.cats),
    url(r'^Dogs.html$', views.dogs),
    url(r'^Shelter_APA.html$', views.shelter_apa),
]
