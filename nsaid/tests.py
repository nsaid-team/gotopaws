#!/usr/bin/env python3

# -------
# imports
# -------

import requests, json
from django.test import TestCase
from nsaid.models import *
import unittest
import coverage

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

    def test_city4 (self) :
        
        c = City.objects.create(
            city_name = "Empty Case Test",
            city_state = "",
            city_country = "",
            city_vet_url = "",
            city_groomer_url = "",
            city_park_url = "",)

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "Empty Case Test")
        self.assertEqual(c.city_state, "")
        self.assertEqual(c.city_country, "")
        self.assertEqual(c.city_vet_url, "")
        self.assertEqual(c.city_groomer_url, "")
        self.assertEqual(c.city_park_url, "")
        
    def test_city5 (self) :
        
        c = City.objects.create(
            city_name = "Sacramento",
            city_state = "CA",
            city_country = "US",
            city_vet_url = "vet.url",
            city_groomer_url = "groomer.url",
            city_park_url = "park.url",)

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "Sacramento")
        self.assertEqual(c.city_state, "CA")
        self.assertEqual(c.city_country, "US")
        self.assertEqual(c.city_vet_url, "vet.url")
        self.assertEqual(c.city_groomer_url, "groomer.url")
        self.assertEqual(c.city_park_url, "park.url")
        
    def test_city6 (self) :
        
        c = City.objects.create(
            city_name = "Totally a real city",
            city_state = "Denial",
            city_country = "USA",
            city_vet_url = "www.totallyrealvets.com",
            city_groomer_url = "www.alsorealgroomers.net",
            city_park_url = "www.bestparkever.gov",)

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "Totally a real city")
        self.assertEqual(c.city_state, "Denial")
        self.assertEqual(c.city_country, "USA")
        self.assertEqual(c.city_vet_url, "www.totallyrealvets.com")
        self.assertEqual(c.city_groomer_url, "www.alsorealgroomers.net")
        self.assertEqual(c.city_park_url, "www.bestparkever.gov")
        
    def test_city7 (self) :
        
        c = City.objects.create(
            city_name = "Phase 2",
            city_state = "Almost Done",
            city_country = "CS 373",
            city_vet_url = "gotopaws.me",
            city_groomer_url = "gotopaws.me",
            city_park_url = "gotopaws.me",)

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "Phase 2")
        self.assertEqual(c.city_state, "Almost Done")
        self.assertEqual(c.city_country, "CS 373")
        self.assertEqual(c.city_vet_url, "gotopaws.me")
        self.assertEqual(c.city_groomer_url, "gotopaws.me")
        self.assertEqual(c.city_park_url, "gotopaws.me")
        
    def test_city8 (self) :
        
        c = City.objects.create(
            city_name = "New York",
            city_state = "New York",
            city_country = "US",
            city_vet_url = "vet url",
            city_groomer_url = "groomer url",
            city_park_url = "park url",)

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "New York")
        self.assertEqual(c.city_state, "New York")
        self.assertEqual(c.city_country, "US")
        self.assertEqual(c.city_vet_url, "vet url")
        self.assertEqual(c.city_groomer_url, "groomer url")
        self.assertEqual(c.city_park_url, "park url")
        
    def test_city9 (self) :
        
        c = City.objects.create(
            city_name = "Testing for city with a really long name that should not break the database",
            city_state = "Texas",
            city_country = "USA",
            city_vet_url = "vet url",
            city_groomer_url = "groomer url",
            city_park_url = "park url",)

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "Testing for city with a really long name that should not break the database")
        self.assertEqual(c.city_state, "Texas")
        self.assertEqual(c.city_country, "USA")
        self.assertEqual(c.city_vet_url, "vet url")
        self.assertEqual(c.city_groomer_url, "groomer url")
        self.assertEqual(c.city_park_url, "park url")
        
    def test_city10 (self) :
        
        c = City.objects.create(
            city_name = "Testing state name length",
            city_state = "Really long state name that the database should handle just fine",
            city_country = "USA",
            city_vet_url = "vet url",
            city_groomer_url = "groomer url",
            city_park_url = "park url",)

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "Testing state name length")
        self.assertEqual(c.city_state, "Really long state name that the database should handle just fine")
        self.assertEqual(c.city_country, "USA")
        self.assertEqual(c.city_vet_url, "vet url")
        self.assertEqual(c.city_groomer_url, "groomer url")
        self.assertEqual(c.city_park_url, "park url")
        
    def test_city11 (self) :
        
        c = City.objects.create(
            city_name = "Country Length",
            city_state = "Test",
            city_country = "Country with a really unnecessarily long name to be put in the database",
            city_vet_url = "another vet url",
            city_groomer_url = "groomer url",
            city_park_url = "best park ever url",)

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "Country Length")
        self.assertEqual(c.city_state, "Test")
        self.assertEqual(c.city_country, "Country with a really unnecessarily long name to be put in the database")
        self.assertEqual(c.city_vet_url, "another vet url")
        self.assertEqual(c.city_groomer_url, "groomer url")
        self.assertEqual(c.city_park_url, "best park ever url")
        
    def test_city12 (self) :
        
        c = City.objects.create(
            city_name = "Url",
            city_state = "Length",
            city_country = "Test",
            city_vet_url = "really really really long url that should be easily handled by the database without any problems.com",
            city_groomer_url = "ditto",
            city_park_url = "another url",)

        self.assertTrue(type(c) == City)
        self.assertEqual(c.city_name, "Url")
        self.assertEqual(c.city_state, "Length")
        self.assertEqual(c.city_country, "Test")
        self.assertEqual(c.city_vet_url, "really really really long url that should be easily handled by the database without any problems.com")
        self.assertEqual(c.city_groomer_url, "ditto")
        self.assertEqual(c.city_park_url, "another url")

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
        
    def test_shelter4 (self) :

        s = Shelter.objects.create(
            shelter_id = "",
            shelter_name = "Empty Case Test",
            shelter_address = "",
            shelter_city = "Foreign Key",
            shelter_state = "",
            shelter_phone = "",
            shelter_email = "",
            shelter_hours = "")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelter_id, "")
        self.assertEqual(s.shelter_name, "Empty Case Test")
        self.assertEqual(s.shelter_address, "")
        self.assertEqual(s.shelter_city, "Foreign Key")
        self.assertEqual(s.shelter_state, "")
        self.assertEqual(s.shelter_phone, "")
        self.assertEqual(s.shelter_email, "")
        self.assertEqual(s.shelter_hours, "")
        
    def test_shelter5 (self) :

        s = Shelter.objects.create(
            shelter_id = "CA765",
            shelter_name = "Animal Shelter",
            shelter_address = "1234 Shelter Dr.",
            shelter_city = "Sacramento",
            shelter_state = "CA",
            shelter_phone = "123 456 7890",
            shelter_email = "shelter.email@internet.google",
            shelter_hours = "4-5 Weekends Only")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelter_id, "CA765")
        self.assertEqual(s.shelter_name, "Animal Shelter")
        self.assertEqual(s.shelter_address, "1234 Shelter Dr.")
        self.assertEqual(s.shelter_city, "Sacramento")
        self.assertEqual(s.shelter_state, "CA")
        self.assertEqual(s.shelter_phone, "123 456 7890")
        self.assertEqual(s.shelter_email, "shelter.email@internet.google")
        self.assertEqual(s.shelter_hours, "4-5 Weekends Only")
        
    def test_shelter6 (self) :

        s = Shelter.objects.create(
            shelter_id = "129802",
            shelter_name = "Turtle Pond",
            shelter_address = "UT Austin",
            shelter_city = "Austin",
            shelter_state = "TX",
            shelter_phone = "1 800 TURTLE",
            shelter_email = "turtle.pond@ut.austin",
            shelter_hours = "all day")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelter_id, "129802")
        self.assertEqual(s.shelter_name, "Turtle Pond")
        self.assertEqual(s.shelter_address, "UT Austin")
        self.assertEqual(s.shelter_city, "Austin")
        self.assertEqual(s.shelter_state, "TX")
        self.assertEqual(s.shelter_phone, "1 800 TURTLE")
        self.assertEqual(s.shelter_email, "turtle.pond@ut.austin")
        self.assertEqual(s.shelter_hours, "all day")
        
    def test_shelter7 (self) :

        s = Shelter.objects.create(
            shelter_id = "TX192837",
            shelter_name = "Pet Shelter for Pets",
            shelter_address = "Shelter Barkway",
            shelter_city = "Austin",
            shelter_state = "TX",
            shelter_phone = "574839",
            shelter_email = "email@internets.com",
            shelter_hours = "9-5")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelter_id, "TX192837")
        self.assertEqual(s.shelter_name, "Pet Shelter for Pets")
        self.assertEqual(s.shelter_address, "Shelter Barkway")
        self.assertEqual(s.shelter_city, "Austin")
        self.assertEqual(s.shelter_state, "TX")
        self.assertEqual(s.shelter_phone, "574839")
        self.assertEqual(s.shelter_email, "email@internets.com")
        self.assertEqual(s.shelter_hours, "9-5")
        
    def test_shelter8 (self) :

        s = Shelter.objects.create(
            shelter_id = "TEST104",
            shelter_name = "Test Shelter",
            shelter_address = "Infinity Cir.",
            shelter_city = "New York",
            shelter_state = "NY",
            shelter_phone = "1 800 800",
            shelter_email = "test@shelter",
            shelter_hours = "9-5")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelter_id, "TEST104")
        self.assertEqual(s.shelter_name, "Test Shelter")
        self.assertEqual(s.shelter_address, "Infinity Cir.")
        self.assertEqual(s.shelter_city, "New York")
        self.assertEqual(s.shelter_state, "NY")
        self.assertEqual(s.shelter_phone, "1 800 800")
        self.assertEqual(s.shelter_email, "test@shelter")
        self.assertEqual(s.shelter_hours, "9-5")
        
    def test_shelter9 (self) :

        s = Shelter.objects.create(
            shelter_id = "IDLENGHTTEST1234567890",
            shelter_name = "Really Long Name That Should Fit In The Database",
            shelter_address = "1234567890 Really Long Street Name Dr. St.",
            shelter_city = "Very Long City Name To Test The Database And Its Ability To Handle Long Names",
            shelter_state = "Nevada",
            shelter_phone = "1 023 843 3534",
            shelter_email = "unit@tests",
            shelter_hours = "12-12")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelter_id, "IDLENGHTTEST1234567890")
        self.assertEqual(s.shelter_name, "Really Long Name That Should Fit In The Database")
        self.assertEqual(s.shelter_address, "1234567890 Really Long Street Name Dr. St.")
        self.assertEqual(s.shelter_city, "Very Long City Name To Test The Database And Its Ability To Handle Long Names")
        self.assertEqual(s.shelter_state, "Nevada")
        self.assertEqual(s.shelter_phone, "1 023 843 3534")
        self.assertEqual(s.shelter_email, "unit@tests")
        self.assertEqual(s.shelter_hours, "12-12")
        
    def test_shelter10 (self) :

        s = Shelter.objects.create(
            shelter_id = "ID54321",
            shelter_name = "Long Attribute Test",
            shelter_address = "1405 Database",
            shelter_city = "Django City",
            shelter_state = "Unusually Long State Name For A State",
            shelter_phone = "1 234 567 8901 2345 67890",
            shelter_email = "really.long.email.for.a.shelter.to.have@unit.tests.nsaid.me",
            shelter_hours = "1:30 to 9:35 MWF and 2:03 to 3:31 TTH")

        self.assertTrue(type(s) == Shelter)
        self.assertEqual(s.shelter_id, "ID54321")
        self.assertEqual(s.shelter_name, "Long Attribute Test")
        self.assertEqual(s.shelter_address, "1405 Database")
        self.assertEqual(s.shelter_city, "Django City")
        self.assertEqual(s.shelter_state, "Unusually Long State Name For A State")
        self.assertEqual(s.shelter_phone, "1 234 567 8901 2345 67890")
        self.assertEqual(s.shelter_email, "really.long.email.for.a.shelter.to.have@unit.tests.nsaid.me")
        self.assertEqual(s.shelter_hours, "1:30 to 9:35 MWF and 2:03 to 3:31 TTH")

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
    
    def test_pet4 (self) :

        p = Pet.objects.create(
            pet_id = "",
            pet_name = "",
            pet_age = "",
            pet_size = "",
            pet_breed = "",
            pet_shelter = "Empty Case Test",
            pet_city = "Foreign Key",
            pet_pic_url = "")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.pet_id, "")
        self.assertEqual(p.pet_name, "")
        self.assertEqual(p.pet_age, "")
        self.assertEqual(p.pet_size, "")
        self.assertEqual(p.pet_breed, "")
        self.assertEqual(p.pet_shelter, "Empty Case Test")
        self.assertEqual(p.pet_city, "Foreign Key")
    
    def test_pet5 (self) :

        p = Pet.objects.create(
            pet_id = "72727272",
            pet_name = "Alexander",
            pet_age = "Adult",
            pet_size = "M",
            pet_breed = "Homo Sapien",
            pet_shelter = "UT",
            pet_city = "Austin",
            pet_pic_url = "awesomepic.url")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.pet_id, "72727272")
        self.assertEqual(p.pet_name, "Alexander")
        self.assertEqual(p.pet_age, "Adult")
        self.assertEqual(p.pet_size, "M")
        self.assertEqual(p.pet_breed, "Homo Sapien")
        self.assertEqual(p.pet_shelter, "UT")
        self.assertEqual(p.pet_city, "Austin")
    
    def test_pet6 (self) :

        p = Pet.objects.create(
            pet_id = "626",
            pet_name = "Stitch",
            pet_age = "Young",
            pet_size = "S",
            pet_breed = "Alien",
            pet_shelter = "Disneyland",
            pet_city = "Disneyland",
            pet_pic_url = "stich.instagram")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.pet_id, "626")
        self.assertEqual(p.pet_name, "Stitch")
        self.assertEqual(p.pet_age, "Young")
        self.assertEqual(p.pet_size, "S")
        self.assertEqual(p.pet_breed, "Alien")
        self.assertEqual(p.pet_shelter, "Disneyland")
        self.assertEqual(p.pet_city, "Disneyland")
    
    def test_pet7 (self) :

        p = Pet.objects.create(
            pet_id = "1234567890",
            pet_name = "Mr. Fluffy",
            pet_age = "Baby",
            pet_size = "L",
            pet_breed = "Fuzzball",
            pet_shelter = "Shelter",
            pet_city = "Austin",
            pet_pic_url = "pet pic url")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.pet_id, "1234567890")
        self.assertEqual(p.pet_name, "Mr. Fluffy")
        self.assertEqual(p.pet_age, "Baby")
        self.assertEqual(p.pet_size, "L")
        self.assertEqual(p.pet_breed, "Fuzzball")
        self.assertEqual(p.pet_shelter, "Shelter")
        self.assertEqual(p.pet_city, "Austin")
    
    def test_pet8 (self) :

        p = Pet.objects.create(
            pet_id = "19283746",
            pet_name = "Pet McPetson",
            pet_age = "Senior",
            pet_size = "L",
            pet_breed = "Walrus",
            pet_shelter = "Super Shelter",
            pet_city = "Washington D. C.",
            pet_pic_url = " ")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.pet_id, "19283746")
        self.assertEqual(p.pet_name, "Pet McPetson")
        self.assertEqual(p.pet_age, "Senior")
        self.assertEqual(p.pet_size, "L")
        self.assertEqual(p.pet_breed, "Walrus")
        self.assertEqual(p.pet_shelter, "Super Shelter")
        self.assertEqual(p.pet_city, "Washington D. C.")
    
    def test_pet9 (self) :

        p = Pet.objects.create(
            pet_id = "Pet ID Length Test Is Here",
            pet_name = "Really Long and Complicated Name for A Pet",
            pet_age = "12034 Days Old",
            pet_size = "Enormous",
            pet_breed = "Poodle",
            pet_shelter = "Shelter of Pets",
            pet_city = "Austin",
            pet_pic_url = " ")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.pet_id, "Pet ID Length Test Is Here")
        self.assertEqual(p.pet_name, "Really Long and Complicated Name for A Pet")
        self.assertEqual(p.pet_age, "12034 Days Old")
        self.assertEqual(p.pet_size, "Enormous")
        self.assertEqual(p.pet_breed, "Poodle")
        self.assertEqual(p.pet_shelter, "Shelter of Pets")
        self.assertEqual(p.pet_city, "Austin")
    
    def test_pet10 (self) :

        p = Pet.objects.create(
            pet_id = "101",
            pet_name = "More Length Tests",
            pet_age = "Baby",
            pet_size = "S",
            pet_breed = "American Purebred Mix of German Shepard and a Tiger",
            pet_shelter = "Long Name Shelter for Pets that like to test databases",
            pet_city = "Animal City where the names are long and the databases are awesome",
            pet_pic_url = "url for the pet that has all the pictures with really long url names")

        self.assertTrue(type(p) == Pet)
        self.assertEqual(p.pet_id, "101")
        self.assertEqual(p.pet_name, "More Length Tests")
        self.assertEqual(p.pet_age, "Baby")
        self.assertEqual(p.pet_size, "S")
        self.assertEqual(p.pet_breed, "American Purebred Mix of German Shepard and a Tiger")
        self.assertEqual(p.pet_shelter, "Long Name Shelter for Pets that like to test databases")
        self.assertEqual(p.pet_city, "Animal City where the names are long and the databases are awesome")
    
    # ----
    # API Tests
    # ----

    def test_api_city_1 (self) :
        response = requests.get('http://private-93df0-gotopaws1.apiary-mock.com/cities/89A/')
        self.assertEqual(response.status_code,404)

    def test_api_city_2 (self) :
        response = requests.get('http://private-93df0-gotopaws1.apiary-mock.com/cities/')
        self.assertEqual(response.status_code,200)
    
    def test_api_city_3 (self) :
        response = requests.get('http://gotopaws.me/api/cities/')
        self.assertEqual(response.status_code,200)

    def test_api_shelter_1 (self) :
        response = requests.get('http://private-93df0-gotopaws1.apiary-mock.com/shelters/4567/')
        self.assertEqual(response.status_code,404)

    def test_api_shelter_2 (self) :
        response = requests.get('http://gotopaws.me/api/shelters/')
        self.assertEqual(response.status_code,200)

    def test_api_pet_1 (self) :
        response = requests.get('http://gotopaws.me/pets/0123_illlllllegal_valueeeee')
        self.assertEqual(response.status_code,404)

    def test_api_pet_2 (self) :
        response = requests.get('http://gotopaws.me/api/pets/')
        self.assertEqual(response.status_code,200)

# ----
# main
# ----

if __name__ == "__main__" :
    main()
