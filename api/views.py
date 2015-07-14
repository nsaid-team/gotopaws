# from nsaid.models import *

from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from models import *
from nsaid.models import Pet
from api.serializers import PetSerializer

# Create your views here.

# @api_view(['GET', 'POST'])
@api_view(['GET'])
def pet_list(request):
    """
    List all pets, maybe later create a new pet
    """
    pets_list = Pet.objects.all()
    #for name in pets_list:
    #    print(name.pet_name)
    #    print(name.pet_shelter)
    if request.method == 'GET':
        #petcheck = Pet(pet_id="asdf",pet_name="figaro",pet_age="12",pet_size="big",pet_breed="mutt",pet_shelter="my house",pet_city="austin")
        petcheck = pets_list[0]
        #petcheck.save()
        pet_list = Pet.objects.all()
        #serializer = PetSerializer(pet_list)
        context = {"pet_list" : pet_list}
        serializer = PetSerializer((petcheck))
        #####HtmlToReturn += "<div class=\"col-lg-4 col-sm-6 col-xs-12\"><a href=/api/pets" + Pet.objects.get(name=pet_name) + "\" class=\"thumbnail img-responsive\"><div class=\"homepage\"><h2>" + state +  "</h2></a></div></div>"
        #return Response(serializer.data) 
        #####return render(request, 'http://gotopaws.me/api/pets/', {"HTML" : HtmlToReturn})
        #return Response(petcheck.pet_name) 
    #elif request.method == 'POST':
    #    pass

    # 6:04

# @api_view(['GET', 'PUT', 'DELETE'])
@api_view(['GET'])
def pet_detail(request, pk):
    """
    Get a specific pet, maybe later update/delete
    """
    try:
        pet = Pet.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(pet)
        return Response(serializer.data)


