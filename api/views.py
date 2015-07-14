# from nsaid.models import *

from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from nsaid.models import Pet
import json

# Create your views here.

# @api_view(['GET', 'POST'])
@api_view(['GET'])
def pet_list(request):
    """
    List all pets, maybe later create a new pet
    """
    if request.method == 'GET':
        #petcheck = Pet(pet_id="asdf",pet_name="figaro",pet_age="12",pet_size="big",pet_breed="mutt",pet_shelter="my house",pet_city="austin")
        pet_list = Pet.objects.all()

        info = {}
        for pet_obj in pet_list:
            pet_info = {}
            pet_info["pet_id"]      = pet_obj.pet_id
            pet_info["pet_name"]    = pet_obj.pet_name
            pet_info["pet_age"]     = pet_obj.pet_age
            pet_info["pet_size"]    = pet_obj.pet_size
            pet_info["pet_breed"]   = pet_obj.pet_breed
            pet_info["pet_shelter"] = pet_obj.pet_shelter
            pet_info["pet_city"]    = pet_obj.pet_city
            pet_info["pet_pic_url"] = pet_obj.pet_pic_url
            info[pet_obj.pet_id] = pet_info
        return HttpResponse(json.dumps(info), content_type="application/json")

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


