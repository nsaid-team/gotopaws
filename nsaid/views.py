from django.http import HttpResponse
from django.template import loader, Template, Context
from django.shortcuts import render, render_to_response
from django.db import connection
from django.conf import settings
from django.core import serializers
from django import http
from nsaid.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime
from elasticsearch import Elasticsearch
import requests
import json
import urllib
import random
import subprocess
from django.core.management import call_command
from django.core.management import execute_from_command_line


def test(request):
    html = "<html><body>Hey that somehow worked!</body></html>"
    return HttpResponse(html)

def home(request):
    template = loader.get_template('Home.html')
    return HttpResponse(template.render())

def shelters(request):
    shelters_list = Shelter.objects.all()
    context = {"shelters_list": shelters_list}
    return render_to_response("Shelters.html", context)

def pets(request):
    pets_list = Pet.objects.all()
    context = {"pets_list": pets_list}
    return render_to_response("Pets.html", context)

def cities(request):
    cities_list = City.objects.all()
    context = {"cities_list": cities_list}
    return render_to_response("Cities.html", context)

def about(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render())

def cats(request):
    template = loader.get_template('Cats.html')
    return HttpResponse(template.render())

def dogs(request):
    template = loader.get_template('Dogs.html')
    return HttpResponse(template.render())

def shelter_apa(request):
    template = loader.get_template('Shelter_APA.html')
    return HttpResponse(template.render())

def cat_sari(request):
    template = loader.get_template('Cat_Sari.html')
    return HttpResponse(template.render())

def dog_earl(request):
    template = loader.get_template('Dog_Earl.html')
    return HttpResponse(template.render())

def dog_Rangel(request):
    template = loader.get_template('Dog_Rangel.html')
    return HttpResponse(template.render())

def shelter_HPPL(request):
    template = loader.get_template('Shelter_HPPL.html')
    return HttpResponse(template.render())

def shelter_Muttville(request):
    template = loader.get_template('Shelter_Muttville.html')
    return HttpResponse(template.render())

def city_Austin(request):
    template = loader.get_template('City_Austin.html')
    return HttpResponse(template.render())

def city_Houston(request):
    template = loader.get_template('City_Houston.html')
    return HttpResponse(template.render())

def city_SF(request):
    template = loader.get_template('City_SF.html')
    return HttpResponse(template.render())

def pet_template(request, identifier):
    pet = Pet.objects.filter(pet_id = identifier)
    context = {'pet': pet[0]}
    return render(request, 'Pet_template.html', context)
    
def shelter_template(request, identifier):
    shelter = Shelter.objects.filter(shelter_id = identifier)
    address = shelter[0].shelter_address + "," + shelter[0].shelter_city + "," + shelter[0].shelter_state
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s" % address.replace(" ", "+")
    response = urllib.request.urlopen(url)
    jsongeocode = response.read()
    pet_list = Pet.objects.filter(pet_shelter = identifier)
    context = {'shelter': shelter[0], 'map_json': jsongeocode, 'pet_list': pet_list}
    return render(request, 'Shelter_template.html', context)
    
def city_template(request, identifier):
    city = City.objects.filter(city_urlized = identifier)
    city_shelter_list = Shelter.objects.filter(shelter_city_urlized = identifier)
    pet_list = Pet.objects.filter(pet_city_urlized = identifier)
    context = {'city': city[0], 'shelter_list' : city_shelter_list, 'pet_list': pet_list}
    return render(request, 'City_template.html', context)

def about(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render())

def navbar(request):
    c = context({'request': request.path})
    nav = loader.get_template('bootstrap-3.3.5-dist/templates/Navbar.html')
    return nav.render(c)

def unit_test(request):
    import os, sys
    from django.conf import settings

    DIRNAME = os.path.dirname(__file__)
    settings.configure(DEBUG = True,
                       DATABASE_ENGINE = 'mysql.connector.django',
                       DATABASE_NAME = os.path.join(DIRNAME, 'database.db'),
                       INSTALLED_APPS = ('django.contrib.auth',
                                         'django.contrib.contenttypes',
                                         'django.contrib.sessions',
                                         'django.contrib.admin',
                                         'nsaid',
                                         'nsaid.tests',))

    from django.test.simple import run_tests

    failures = run_tests(['nsaid',], verbosity=1)
    if failures:
        test = "FAIL" + str(failures)
    else :
        f = open('workfile', 'w')
        test = f.read() 

    return HttpResponse(test)

@api_view(['GET'])
def pet_list(request):
    if request.method == 'GET':
        pet_list = Pet.objects.all()
        info = {}
        for pet_obj in pet_list:
            pet_info = {}
            pet_info["pet_id"]          = pet_obj.pet_id
            pet_info["pet_name"]        = pet_obj.pet_name
            pet_info["pet_age"]         = pet_obj.pet_age
            pet_info["pet_sex"]         = pet_obj.pet_sex
            pet_info["pet_size"]        = pet_obj.pet_size
            pet_info["pet_breed"]       = pet_obj.pet_breed
            pet_info["pet_shelter"]     = pet_obj.pet_shelter
            pet_info["pet_city"]        = pet_obj.pet_city
            pet_info["pet_pic_url"]     = pet_obj.pet_pic_url
            pet_info["pet_pic_large"]   = pet_obj.pet_pic_large
            pet_info["pet_url"]         = pet_obj.pet_url
            pet_info["pet_shelter_url"] = pet_obj.pet_shelter_url
            pet_info["pet_city_url"]    = pet_obj.pet_city_url
            info[pet_obj.pet_id] = pet_info
        return HttpResponse(json.dumps(info), content_type="application/json")

@api_view(['GET'])
def shelter_list(request):
    """
    List all shelters, maybe later create?
    """
    if request.method == 'GET':
        shelter_list = Shelter.objects.all()
        info = {}
        for shelter_obj in shelter_list:
            shelter_info = {}
            shelter_info["shelter_id"]       = shelter_obj.shelter_id
            shelter_info["shelter_name"]     = shelter_obj.shelter_name
            shelter_info["shelter_address" ] = shelter_obj.shelter_address
            shelter_info["shelter_city"]     = shelter_obj.shelter_city
            shelter_info["shelter_state"]    = shelter_obj.shelter_state
            shelter_info["shelter_phone"]    = shelter_obj.shelter_phone
            shelter_info["shelter_email"]    = shelter_obj.shelter_email
            shelter_info["shelter_hours"]    = shelter_obj.shelter_hours
            shelter_info["shelter_pic"]      = shelter_obj.shelter_pic
            shelter_info["shelter_url"]      = shelter_obj.shelter_url
            shelter_info["shelter_city_url"] = shelter_obj.shelter_city_url
            info[shelter_obj.shelter_id] = shelter_info
        return HttpResponse(json.dumps(info), content_type="application/json")

@api_view(['GET'])
def city_list(request):
    """
    List all cities, maybe later create?
    """
    if request.method == 'GET':
        city_list = City.objects.all()
        info = {}
        for city_obj in city_list:
            city_info = {}
            city_info["city_name"]        = city_obj.city_name
            city_info["city_state"]       = city_obj.city_state
            city_info["city_country"]     = city_obj.city_country
            city_info["city_vet_url"]     = city_obj.city_vet_url
            city_info["city_groomer_url"] = city_obj.city_vet_url
            city_info["city_park_url"]    = city_obj.city_park_url
            city_info["city_pic"]           = city_obj.city_pic
            city_info["city_vet_pic"]       = city_obj.city_vet_pic
            city_info["city_park_pic"]      = city_obj.city_park_pic
            city_info["city_groomer_pic"]   = city_obj.city_groomer_pic
            city_info["city_url"]           = city_obj.city_url
            info[str(city_obj.city_name + '_' + city_obj.city_state)] = city_info
        return HttpResponse(json.dumps(info), content_type="application/json")

def search (request):
    q = request.GET.get('q')
    es = Elasticsearch()
    rs = es.search(index="gtp_index", body=
        {
            "query": {
                "bool": {
                    "should": [
                        { "match": { "title":           q }},
                        { "match": { "subtitle":        q }},
                        { "match": { "shelters_text":   q }},
                        { "match": { "pets_text":       q }},
                        { "match": { "vets_text":       q }},
                    ]
                }
            },
            "highlight": {
                "fields" : {
                    'title': {},
                    'subtitle': {},
                    "*_text" : {}
                }
            }
        }
    )

    results = {}
    results_list = []
    titles_list = []
    for hit in rs['hits']['hits']:
        if hit["_source"]['title'] not in titles_list :
            titles_list.append(hit["_source"]['title'])  
            results['url'] = hit["_source"]['url']
            if 'shelters_text' in hit['highlight']:
                results['shelters_text'] = hit['highlight']['shelters_text'][0]
                results['shelters_text'] = results['shelters_text'].replace("<em>", "<strong><em>")
                results['shelters_text'] = results['shelters_text'].replace("</em>", "</em></strong>")
            else :
                results['shelters_text'] = None
            if 'pets_text' in hit['highlight'] :
                results['pets_text'] = hit['highlight']['pets_text'][0]
                results['pets_text'] = results['pets_text'].replace("<em>", "<strong><em>")
                results['pets_text'] = results['pets_text'].replace("</em>", "</em></strong>")
            else :
                results['pets_text'] = None
            if 'vets_text' in hit['highlight'] :
                results['vets_text'] = hit['highlight']['vets_text'][0]
                results['vets_text'] = results['vets_text'].replace("<em>", "<strong><em>")
                results['vets_text'] = results['vets_text'].replace("</em>", "</em></strong>")
            else :
                results['vets_text'] = None
            results['title'] = hit["_source"]['title']
            if 'title' in hit['highlight']:
                results['title'] = hit['highlight']['title'][0]
                results['title'] = results['title'].replace("<em>", "<strong><em>")
                results['title'] = results['title'].replace("</em>", "</em></strong>")
            results['subtitle'] = hit["_source"]['subtitle']
            if 'subtitle' in hit['highlight']:
                results['subtitle'] = hit['highlight']['subtitle'][0]
                results['subtitle'] = results['subtitle'].replace("<em>", "<strong><em>")
                results['subtitle'] = results['subtitle'].replace("</em>", "</em></strong>")
            results_list.append({'title':results['title'], 'subtitle':results['subtitle'], 'vets_text':results['vets_text'], 'pets_text': results['pets_text'], 'shelters_text': results['shelters_text']})
    context = {"results_list": results_list} 
    #print({context})
    return render_to_response('search/search.html', context)

def external_api (request) :
    heroes_list = []
    items_list = []
    sets_list = []
    pet_list = []
    pet_url = []
    results_list = []
    item_hero_list = []
    identifiers_list = ['heroes', 'items', 'sets']
    
    url = "http://nsaid.me/api/pets/"
    our_response = urllib.request.urlopen(url).read().decode("utf-8")
    our_api_json = json.loads(our_response)

    for t in our_api_json :
        pet_list.append(our_api_json[t]['pet_name'])
        pet_url.append(our_api_json[t]['pet_url'])
    
    for i in identifiers_list :
        url = "http://hatfancy.me/api/" + i + "/"
        response = urllib.request.urlopen(url).read().decode("utf-8")
        api_json = json.loads(response)
        if (i == 'heroes') :
            heroes_list = api_json
        if (i == 'items') :
            items_list = api_json
        if (i == 'sets') :
            sets_list = api_json

    for j in range(len(heroes_list)) :
        for k in range(len(items_list)) :
            ran_num = random.randrange(len(pet_list))
            h = heroes_list[j]
            m = items_list[k]

            if ((h['name'] == m['hero']) and (h['name'] not in item_hero_list)) :
                results_list.append({'hero': h['name'], 'main_item': m['name'], 'main_set': m['item_set'], 'pet': pet_list[ran_num], 'pet_url': pet_url[ran_num]})
                item_hero_list.append(m['hero'])

    context = {"results_list": results_list}
    #print({context})
    return render_to_response('extapi.html', context)
    
