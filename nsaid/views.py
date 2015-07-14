from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, render_to_response
from django.db import connection
from nsaid.models import *


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

#def pet(request, pet_id):
#    context = {'pet_id': pet_id}
#    return render(request, 'Pet_Page.html', context)

#def shelter(request, shelter_id):
#    context = {'shelter_id': shelter_id}
#    return render(request, 'Shelter_Page.html', context)

#def city(request, city_id):
#    context = {'city_id': city_id}
#    return render(request, 'City_Page.html', context)
