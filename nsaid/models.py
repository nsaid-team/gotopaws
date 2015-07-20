from django.db import models
from django.contrib.auth.models import User

    # ------------
    # City_model
    # ------------

class City(models.Model):
    """
    The model contains a name, state, country, and vet_url 
    The list of pets in a city is handled by Pet having a foreign key Pet.city.
    The list of shelters in a city is handled by Shelter having a foreign key Shelter.city. 
    The __str__ method is used to return the city.
    """

    #city_urlized = models.CharField(max_length=300)
    city_name = models.CharField(max_length=300) # text field
    city_state = models.CharField(max_length=50) # text field
    city_country = models.CharField(max_length=200) # text field
    city_vet_url = models.CharField(max_length=1000) # external link
    city_groomer_url = models.CharField(max_length=1000) # external link
    city_park_url = models.CharField(max_length=1000) # external link
    city_pic = models.CharField(max_length=1000) # reference to picture of city
    city_vet_pic = models.CharField(max_length=1000) # reference to picture of vet in city
    city_park_pic = models.CharField(max_length=1000) # reference to picture of park in city
    city_groomer_pic = models.CharField(max_length=1000) # reference to picture of groomer in city
    city_url = models.CharField(max_length=1000) # link to the City_Page
    
    """
    class Meta:
        app_label = 'City'
    """
        
    def __str__ (self):
        return str(self.city_name + '_' + self.city_state)


    # ------------
    # Shelter_model
    # ------------

class Shelter(models.Model):
    """
    The model contains a shelterid id string, name, address line, city, state, phone, email, and hours listing
    The list of pets in a shelter is handled by Pet having a foreign key Pet.shelter. 
    The __str__ method is used to return the shelterid identifier.
    """
    
    shelter_id = models.CharField(max_length=50) # id from petfinder
    shelter_name = models.CharField(max_length=300) # text field
    shelter_address = models.CharField(max_length=1000) # text field
    #shelter_city = models.ForeignKey(City, related_name = 'shelter_city')
    shelter_city = models.CharField(max_length=300) # text field
    shelter_state = models.CharField(max_length=50) # text field
    #shelter_lattitude = models.CharField(max_length=50) # text field
    #shelter_longitude = models.CharField(max_length=50) # text field
    shelter_phone = models.CharField(max_length=50) # text field
    shelter_email = models.CharField(max_length=200) # text field
    shelter_hours = models.CharField(max_length=200) # text field
    shelter_pic = models.CharField(max_length=1000) # logo picture of shelter
    shelter_url = models.CharField(max_length=1000) # link to Shelter_Page
    shelter_city_url = models.CharField(max_length=1000) # link to City_Page
    #shelter_blurb = models.CharField(max_length=1000) # blurb from yelp or google
    
    """
    class Meta:
        app_label = 'Shelter'
    """
    
    def __str__ (self):
        return self.shelter_id


    # -------------
    # Pet_model
    # -------------

class Pet(models.Model):
    """
    The model contains a petsid id string, name, age, size, breed, shelter, city, and a pic_url
    The __str__ method is used to return the petid identifier.
    """

    pet_id = models.CharField(max_length=50) # pet id from petfinder
    pet_name = models.CharField(max_length=300) # text field
    pet_age = models.CharField(max_length=50) # text field
    pet_sex = models.CharField(max_length=50) # text field
    pet_size = models.CharField(max_length=50) # text field
    pet_breed = models.CharField(max_length=200) # text field
    #pet_shelter = models.ForeignKey(Shelter, related_name = 'pet_shelter')
    pet_shelter = models.CharField(max_length=300) # shelter id from petfinder
    #pet_city = models.ForeignKey(City, related_name='pet_city')
    pet_city = models.CharField(max_length=300) # text field
    #pet_state = models.CharField(max_length=50)
    pet_pic_url = models.CharField(max_length=1000) # thumbnail-ish picture of pet
    pet_pic_large = models.CharField(max_length=1000) # larger picture of pet
    pet_url = models.CharField(max_length=1000) # link to Pet_Page
    pet_shelter_url = models.CharField(max_length=1000) # link to Shelter_Page
    pet_city_url = models.CharField(max_length=1000) # link to City_Page
    
    """
    class Meta:
        app_label = 'Pet'
    """
    
    def __str__ (self):
        return self.pet_id
