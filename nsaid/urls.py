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
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', views.test),
    url(r'^$', views.home),
    url(r'^home$', views.home),
    url(r'^shelters$', views.shelters),
    url(r'^pets$', views.pets),
    url(r'^cities$', views.cities),
    url(r'^about$', views.about),
    #url(r'^cats$', views.cats),
    #url(r'^dogs$', views.dogs),
    #url(r'^apa$', views.shelter_apa),
    url(r'^sari$', views.pet_template),
    #url(r'^earl$', views.dog_earl),
    #url(r'^rangel$', views.dog_Rangel),
    #url(r'^hppl$', views.shelter_template),
    #url(r'^muttville$', views.shelter_Muttville),
    #url(r'^austin$', views.city_Austin),
    #url(r'^sf$', views.city_SF),
    #url(r'^houston$', views.city_Houston),
    url(r'^extapi$', views.external_api),
    url(r'^navbar$', views.navbar),
    #RESTful API
    #url(r'^api/', include('api.urls')),
    #url(r'^api/', include(ShelterResource().urls)),
    #url(r'^api/', include(CityResource().urls)),

    url(r'^pets/(?P<identifier>[\w-]+)/json$', views.pet_json),
    url(r'^pets/(?P<identifier>[\w-]+)/$', views.pet_template),
    url(r'^shelters/(?P<identifier>[\w-]+)/json$', views.shelter_json),
    url(r'^shelters/(?P<identifier>[\w-]+)/$', views.shelter_template),
    url(r'^cities/(?P<identifier>[\w|\W]+)/json$', views.city_json),
    #url(r'^cities/(?P<identifier>[\w|\W]+)/$', views.city_template),
    url(r'^([A-Z][A-Z][\d]+)$', views.city_template),
    url(r'^api/pets/$', views.pet_list),
    url(r'^api/shelters/$', views.shelter_list),
    url(r'^api/cities/$', views.city_list),
    url(r'^search/$', views.search, name='search'),
    url(r'^unit_test/$', views.unit_test),
]
