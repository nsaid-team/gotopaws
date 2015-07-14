from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^pets/$', 'pet_list', name='pet_list'),
    #url(r'^pets/(?P<pk>[0-9]+)$', 'pet_detail', name='pet_detail'),
    url(r'^shelters/$', 'shelter_list', name='shelter_list'),
    url(r'^cities/$', 'city_list', name='city_list'),
)
