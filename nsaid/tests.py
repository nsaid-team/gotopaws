#!/usr/bin/env python3

# -------
# imports
# -------

import requests, json
import unittest
from nsaid.models import *
import coverage
import nose

# -----------
# test
# -----------

class Test (unittest.TestCase) :
    
    # ----
    # City Model
    # ----

    def test_city1 (self) :
        c = City.objects.create(
            city_name = "Dallas",
            city_state = "TX",
            city_country = "US",
            city_vet_url = "veturl",
            city_groomer_url = "groomerurl",
            city_park_url = "parkurl",)

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "Dallas")
        self.assertEqual(c.city_state, "TX")
        self.assertEqual(c.city_country, "US")
        self.assertEqual(c.city_vet_url, "veturl")
        self.assertEqual(c.city_groomer_url, "groomerurl")
        self.assertEqual(c.city_park_url, "parkurl")
        
    def test_city2 (self) :
        c = City.objects.create(
            city_name = "San Francisco",
            city_state = "CA",
            city_country = "US",
            city_vet_url = "veturl",
            city_groomer_url = "groomerurl",
            city_park_url = "parkurl")

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "San Francisco")
        self.assertEqual(c.city_state, "CA")
        self.assertEqual(c.city_country, "US")
        self.assertEqual(c.city_vet_url, "veturl")
        self.assertEqual(c.city_groomer_url, "groomerurl")
        self.assertEqual(c.city_park_url, "parkurl")
        
    def test_city3 (self) :
        c = City.objects.create(
            city_name = "Austin",
            city_state = "TX",
            city_country = "US",
            city_vet_url = "veturl",
            city_groomer_url = "groomerurl",
            city_park_url = "parkurl")

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "Austin")
        self.assertEqual(c.city_state, "TX")
        self.assertEqual(c.city_country, "US")
        self.assertEqual(c.city_vet_url, "veturl")
        self.assertEqual(c.city_groomer_url, "groomerurl")
        self.assertEqual(c.city_park_url, "parkurl")


    # ----
    # Shelter Model
    # ----

    def test_shelter1 (self) :

        s = Shelter.objects.create(
            shelter_id = "TX1218",
            shelter_name = "Austin Pets Alive!",
            shelter_address = "1156 West Cesar Chavez",
            shelter_city = "Dallas",
            shelter_state = "TX",
            shelter_phone = "512 961 6519",
            shelter_email = "adopt@austinpetsalive.org",
            shelter_hours = "10:00am- 6:00pm")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelter_id, "TX1218")
        self.assertEqual(s.shelter_name, "Austin Pets Alive!")
        self.assertEqual(s.shelter_address, "1156 West Cesar Chavez")
        self.assertEqual(s.shelter_city, "Dallas")
        self.assertEqual(s.shelter_state, "TX")
        self.assertEqual(s.shelter_phone, "512 961 6519")
        self.assertEqual(s.shelter_email, "adopt@austinpetsalive.org")
        self.assertEqual(s.shelter_hours, "10:00am- 6:00pm")

    def test_shelter2 (self) :

        s = Shelter.objects.create(
            shelter_id = "CA500",
            shelter_name = "Hound Rescue",
            shelter_address = "Lakeline Petsmart 11066 Pecan Park Blvd, Cedar Park",
            shelter_city = "San Francisco",
            shelter_state = "CA",
            shelter_phone = "512 636 8473",
            shelter_email = "hound@dogs.org",
            shelter_hours = "9:00am- 5:00pm")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelter_id, "CA500")
        self.assertEqual(s.shelter_name, "Hound Rescue")
        self.assertEqual(s.shelter_address, "Lakeline Petsmart 11066 Pecan Park Blvd, Cedar Park")
        self.assertEqual(s.shelter_city, "San Francisco")
        self.assertEqual(s.shelter_state, "CA")
        self.assertEqual(s.shelter_phone, "512 636 8473")
        self.assertEqual(s.shelter_email, "hound@dogs.org")
        self.assertEqual(s.shelter_hours, "9:00am- 5:00pm")
        
    def test_shelter3 (self) :

        s = Shelter.objects.create(
            shelter_id = "TX514",
            shelter_name = "Austin Animal Center",
            shelter_address = "7201 Levander Loop",
            shelter_city = "Austin",
            shelter_state = "TX",
            shelter_phone = "512 978 0500",
            shelter_email = "animal.customerservice@austintexas.gov",
            shelter_hours = "11:00 am - 7:00 pm")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelter_id, "TX514")
        self.assertEqual(s.shelter_name, "Austin Animal Center")
        self.assertEqual(s.shelter_address, "7201 Levander Loop")
        self.assertEqual(s.shelter_city, "Austin")
        self.assertEqual(s.shelter_state, "TX")
        self.assertEqual(s.shelter_phone, "512 978 0500")
        self.assertEqual(s.shelter_email, "animal.customerservice@austintexas.gov")
        self.assertEqual(s.shelter_hours, "11:00 am - 7:00 pm")


    # ----
    # Pet Model
    # ----

    def test_pet1 (self) :

        p = Pet.objects.create(
            pet_id = "24306492",
            pet_name = "Amigo",
            pet_age = "Adult",
            pet_size = "S",
            pet_breed = "Chihuahua",
            pet_shelter = "TX1218",
            pet_city = "Dallas",
            pet_pic_url = "picurl")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.pet_id, "24306492")
        self.assertEqual(p.pet_name, "Amigo")
        self.assertEqual(p.pet_age, "Adult")
        self.assertEqual(p.pet_size, "S")
        self.assertEqual(p.pet_breed, "Chihuahua")
        self.assertEqual(p.pet_shelter, "TX1218")
        self.assertEqual(p.pet_city, "Dallas")
        
    def test_pet2 (self) :

        p = Pet.objects.create(
            pet_id = "32151337",
            pet_name = "Tita",
            pet_age = "Senior",
            pet_size = "L",
            pet_breed = "Applehead Siamese",
            pet_shelter = "CA500",
            pet_city = "San Francisco",
            pet_pic_url = "picurl")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.pet_id, "32151337")
        self.assertEqual(p.pet_name, "Tita")
        self.assertEqual(p.pet_age, "Senior")
        self.assertEqual(p.pet_size, "L")
        self.assertEqual(p.pet_breed, "Applehead Siamese")
        self.assertEqual(p.pet_shelter, "CA500")
        self.assertEqual(p.pet_city, "San Francisco")
    
    def test_pet3 (self) :

        p = Pet.objects.create(
            pet_id = "18620461",
            pet_name = "Little John II",
            pet_age = "Baby",
            pet_size = "M",
            pet_breed = "Tabby",
            pet_shelter = "TX514",
            pet_city = "Austin",
            pet_pic_url = "picurl")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.pet_id, "18620461")
        self.assertEqual(p.pet_name, "Little John II")
        self.assertEqual(p.pet_age, "Baby")
        self.assertEqual(p.pet_size, "M")
        self.assertEqual(p.pet_breed, "Tabby")
        self.assertEqual(p.pet_shelter, "TX514")
        self.assertEqual(p.pet_city, "Austin")
    
    
    # ----
    # API Tests
    # ----

    def test_api_city_1 (self) :
        response = requests.get('http://private-93df0-gotopaws1.apiary-mock.com/cities/89A/')
        self.assertEqual(response.status_code,404)

    def test_api_city_2 (self) :
        response = requests.get('http://private-93df0-gotopaws1.apiary-mock.com/cities/')
        self.assertEqual(response.status_code,200)

    def test_api_shelter_1 (self) :
        response = requests.get('http://private-93df0-gotopaws1.apiary-mock.com/shelters/4567/')
        self.assertEqual(response.status_code,404)

    def test_api_shelter_2 (self) :
        response = requests.get('http://private-93df0-gotopaws1.apiary-mock.com/shelters/')
        self.assertEqual(response.status_code,200)

    def test_api_pet_1 (self) :
        response = requests.get('http://private-93df0-gotopaws1.apiary-mock.com/pets/0123')
        self.assertEqual(response.status_code,404)

    def test_api_pet_2 (self) :
        response = requests.get('http://private-300ca-nsaid.apiary-mock.com/pets/')
        self.assertEqual(response.status_code,200)

# ----
# main
# ----

if __name__ == "__main__" :
    main()
