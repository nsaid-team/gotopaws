#!/usr/bin/env python3

# -------
# imports
# -------

import requests, json
import unittest
from nsaid.models import *

# -----------
# test
# -----------

class Test (unittest.TestCase) :

    # ----
    # City Model
    # ----

    def test_city1 (self) :
        c = State.objects.create(
            name = "Dallas",
            address = "4151 McKinney Ave",
            state = "TX",
            country = "US",
            vet_url = "veturl")

        self.assertTrue(type(s) == City)
        self.assertEqual(c.name, "Dallas")
        self.assertEqual(c.state, "TX")
        self.assertEqual(c.city, "US")
        self.assertEqual(s.vet_url, "veturl")
        
    def test_city2 (self) :
        c = State.objects.create(
            name = "San Francisco",
            address = "1207 Ninth Ave",
            state = "CA",
            country = "US",
            vet_url = "veturl")

        self.assertTrue(type(s) == City)
        self.assertEqual(c.name, "San Francisco")
        self.assertEqual(c.state, "CA")
        self.assertEqual(c.city, "US")
        self.assertEqual(s.vet_url, "veturl")
        
    def test_city3 (self) :
        c = State.objects.create(
            name = "Austin",
            address = "7300 Ranch Road 2222",
            state = "TX",
            country = "US",
            vet_url = "veturl")

        self.assertTrue(type(s) == City)
        self.assertEqual(c.name, "Austin")
        self.assertEqual(c.state, "TX")
        self.assertEqual(c.city, "US")
        self.assertEqual(s.vet_url, "veturl")


# ----
    # Shelter Model
    # ----

    def test_shelter1 (self) :

        s = Shelter.objects.create(
            shelterid = "TX1218",
            name = "Austin Pets Alive!",
            address = "1156 West Cesar Chavez",
            city = "Austin",
            state = "TX",
            phone = "512 961 6519",
            email = "adopt@austinpetsalive.org",
            hours = "10:00am- 6:00pm")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelterid, "TX1218")
        self.assertEqual(s.name, "Austin Pets Alive!")
        self.assertEqual(s.address, "1156 West Cesar Chavez")
        self.assertEqual(s.city, "Austin")
        self.assertEqual(s.state, "TX")
        self.assertEqual(s.phone, "512 961 6519")
        self.assertEqual(s.email, "adopt@austinpetsalive.org")
        self.assertEqual(s.hours, "10:00am- 6:00pm")

    def test_shelter2 (self) :

        s = Shelter.objects.create(
            shelterid = "TX500",
            name = "Hound Rescue",
            address = "Lakeline Petsmart 11066 Pecan Park Blvd, Cedar Park",
            city = "Austin",
            state = "TX",
            phone = "512 636 8473",
            email = "hound@dogs.org",
            hours = "9:00am- 5:00pm")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelterid, "TX500")
        self.assertEqual(s.name, "Hound Rescue")
        self.assertEqual(s.address, "Lakeline Petsmart 11066 Pecan Park Blvd, Cedar Park")
        self.assertEqual(s.city, "Austin")
        self.assertEqual(s.state, "TX")
        self.assertEqual(s.phone, "512 636 8473")
        self.assertEqual(s.email, "hound@dogs.org")
        self.assertEqual(s.hours, "9:00am- 5:00pm")
        
    def test_shelter3 (self) :

        s = Shelter.objects.create(
            shelterid = "TX514",
            name = "Austin Animal Center",
            address = "7201 Levander Loop",
            city = "Austin",
            state = "TX",
            phone = "512 978 0500",
            email = "hound@dogs.org",
            hours = "9:00am- 5:00pm")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelterid, "TX500")
        self.assertEqual(s.name, "Hound Rescue")
        self.assertEqual(s.address, "Lakeline Petsmart 11066 Pecan Park Blvd, Cedar Park")
        self.assertEqual(s.city, "Austin")
        self.assertEqual(s.state, "TX")
        self.assertEqual(s.phone, "512 636 8473")
        self.assertEqual(s.email, "animal.customerservice@austintexas.gov")
        self.assertEqual(s.hours, "11:00 am - 7:00 pm")


    # ----
    # Pet Model
    # ----

    def test_pet1 (self) :

        p = Pet.objects.create(
            petsid = "24306492",
            name = "Amigo",
            age = "Adult",
            size = "S",
            breed = "Chihuahua",
            shelter = "TX1148",
            city = "Austin",
            pic_url = "picurl")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.petsid, "24306492")
        self.assertEqual(p.name, "Amigo")
        self.assertEqual(p.age, "Adult")
        self.assertEqual(p.size, "S")
        self.assertEqual(p.breed, "Chihuahua")
        self.assertEqual(p.shelter, "TX1148")
        self.assertEqual(p.city, "Austin")
        
    def test_pet2 (self) :

        p = Pet.objects.create(
            petsid = "32151337",
            name = "Tita",
            age = "Senior",
            size = "L",
            breed = "Applehead Siamese",
            shelter = "TX1334",
            city = "Austin",
            pic_url = "picurl")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.petsid, "32151337")
        self.assertEqual(p.name, "Tita")
        self.assertEqual(p.age, "Senior")
        self.assertEqual(p.size, "L")
        self.assertEqual(p.breed, "Applehead Siamese")
        self.assertEqual(p.shelter, "TX1334")
        self.assertEqual(p.city, "Austin")
    
    def test_pet3 (self) :

        p = Pet.objects.create(
            petsid = "18620461",
            name = "Little John II",
            age = "Baby",
            size = "M",
            breed = "Tabby",
            shelter = "TX1222",
            city = "Austin",
            pic_url = "picurl")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.petsid, "18620461")
        self.assertEqual(p.name, "Little John II")
        self.assertEqual(p.age, "Baby")
        self.assertEqual(p.size, "M")
        self.assertEqual(p.breed, "Tabby")
        self.assertEqual(p.shelter, "TX1222")
        self.assertEqual(p.city, "Austin")
    
    # ----
    # API Tests
    # ----

    def test_api_city_1 (self) :
        response = requests.get('http://private-300ca-nsaid.apiary-mock.com/cities/89A/')
        self.assertEqual(response.status_code,404)

    def test_api_city_2 (self) :
        response = requests.get('http://private-300ca-nsaid.apiary-mock.com/cities/')
        self.assertEqual(response.status_code,200)

    def test_api_shelter_1 (self) :
        response = requests.get('http://private-300ca-nsaid.apiary-mock.com/shelters/4567/')
        self.assertEqual(response.status_code,404)

    def test_api_shelter_2 (self) :
        response = requests.get('http://private-300ca-nsaid.apiary-mock.com/shelters/')
        self.assertEqual(response.status_code,200)

    def test_api_pet_1 (self) :
        response = requests.get('http://private-300ca-nsaid.apiary-mock.com/pets/0123')
        self.assertEqual(response.status_code,404)

    def test_api_pet_2 (self) :
        response = requests.get('http://private-300ca-nsaid.apiary-mock.com/pets/')
        self.assertEqual(response.status_code,200)

# ----
# main
# ----

if __name__ == "__main__" :
    main()
