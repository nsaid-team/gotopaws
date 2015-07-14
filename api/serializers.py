from rest_framework import serializers

#from models import * 
from nsaid.models import Pet 

petcheck = Pet(pet_id="asdf",pet_name="figaro",pet_age="12",pet_size="big",pet_breed="mutt",pet_shelter="my house",pet_city="austin")

class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ('pet_id', 'pet_name', 'pet_age', 'pet_size', 'pet_breed', 'pet_shelter', 'pet_city', 'pet_pic_url')
        #fields = ('pet_name',)
        #fields = ('id',)

