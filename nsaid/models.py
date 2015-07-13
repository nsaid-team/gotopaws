from django.db import models

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

    city_name = models.CharField(max_length=200)
    city_state = models.CharField(max_length=300)
    city_country = models.CharField(max_length=100)
    city_vet_url = models.CharField(max_length=500)
    city_groomer_url = models.CharField(max_length=500)
    city_park_url = models.CharField(max_length=500)
    
    """
    class Meta:
        app_label = 'City'
    """
        
    def __str__ (self):
        return self.name


    # ------------
    # Shelter_model
    # ------------

class Shelter(models.Model):
    """
    The model contains a shelterid id string, name, address line, city, state, phone, email, and hours listing
    The list of pets in a shelter is handled by Pet having a foreign key Pet.shelter. 
    The __str__ method is used to return the shelterid identifier.
    """
    
    shelter_id = models.CharField(max_length=50)
    shelter_name = models.CharField(max_length=300)
    shelter_address = models.CharField(max_length=200)
    shelter_city = models.ForeignKey(City, related_name = 'shelter_city')
    shelter_state = models.CharField(max_length=50)
    shelter_phone = models.CharField(max_length=50)
    shelter_email = models.CharField(max_length=100)
    shelter_hours = models.CharField(max_length=200)
    
    """
    class Meta:
        app_label = 'Shelter'
    """
    
    def __str__ (self):
        return self.shelterid


    # -------------
    # Pet_model
    # -------------

class Pet(models.Model):
    """
    The model contains a petsid id string, name, age, size, breed, shelter, city, and a pic_url
    The __str__ method is used to return the petid identifier.
    """

    pet_id = models.CharField(max_length=50)
    pet_name = models.CharField(max_length=100)
    pet_age = models.CharField(max_length=20)
    pet_size = models.CharField(max_length=20)
    pet_breed = models.CharField(max_length=100)
    pet_shelter = models.ForeignKey(Shelter, related_name = 'pet_shelter')
    pet_city = models.ForeignKey(City, related_name='pet_city')
    pet_pic_url = models.CharField(max_length=500)
    
    """
    class Meta:
        app_label = 'Pet'
    """
    
    def __str__ (self):
        return self.petsid
