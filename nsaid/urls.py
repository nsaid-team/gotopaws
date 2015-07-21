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

from django.conf.urls import patterns, include, url
from django.conf import settings
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^about$', views.about),
    url(r'^extapi$', views.external_api),
    url(r'^search/$', views.search, name='search'),
    url(r'^unit_test$', views.unit_test),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^home$', views.home),
    url(r'^pets$', views.pets),
    url(r'^shelters$', views.shelters),
    url(r'^cities$', views.cities),
    url(r'^id([\d]+)$', views.pet_template),
    url(r'^([A-Z][A-Z][\d]+)$', views.shelter_template),
    url(r'^([a-z_]+)$', views.city_template),
    # RESTful API
    url(r'^api/pets/$', views.pet_list),
    url(r'^api/shelters/$', views.shelter_list),
    url(r'^api/cities/$', views.city_list),
    
    url(r'^test/$', views.test),
]
