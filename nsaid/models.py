from django.db import models

    # ------------
    # City_model
    # ------------

class City(models.Model):
    """
    The model contains a name, state, country, and vet_url 
    The list of pets in a city is handled by Pet having a foreign key Pet.city.
    The list of shelters in a city is handled by Shelter having a foreign key Shelter.city. 
    The __str__ method is used to return the concatenated city and state.
    """

    name = models.CharField(max_length=200)
    state = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    vet_url = models.CharField(max_length=500)
    
    class Meta:
        app_label = 'City'
        
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
    
    shelterid = models.CharField(max_length=50)
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    hours = models.CharField(max_length=200)

    class Meta:
        app_label = 'Shelter'
    
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

    petsid = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    breed = models.CharField(max_length=100)
    shelter = models.ForeignKey(Shelter)
    city = models.ForeignKey(City, related_name='city')
    pic_url = models.CharField(max_length=500)
    
    class Meta:
        app_label = 'Pet'
    
    def __str__ (self):
        return self.petsid
