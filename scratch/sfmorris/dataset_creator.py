#!/usr/bin/env python3

import rauth
import requests
import sys
import json
import pprint

def create_cities_file(city_list_parameter):
    """
    returns a success code for printing a city json file 
    """

    fixture_list = []
    pk = 1
    for city_name, city_name_urlized in city_list_parameter:
        fields = {  "city_urlized" : "",
                    "city_name" : "",
                    "city_state" : "",
                    "city_country" : "",
                    "city_vet_url" : "",
                    "city_groomer_url" : "",
                    "city_park_url" : "",
                    "city_pic" : "",
                    "city_park_pic" : "",
                    "city_vet_pic" : "",
                    "city_groomer_pic" : "",
                    "city_url" : "",
                    "city_blurb" : ""
                 }
        try:
            fields["city_urlized"] = city_name_urlized
        except:
            print("   city_urlized was not found")
        try:
            fields["city_name"] = city_name
        except:
            print("   city_name was not found")   
        try:
            fields["city_state"] = city_name
        except:
            print("   city_name was not found")                       
        try:
            fields["city_country"] = "US"
        except:
            print("   city_country was not found")
        try:
            fields["city_vet_url"] = yelp_query(city_name, "veterinarian", "url")
        except:
            print("   city_vet_url was not found")
        try:
            fields["city_groomer_url"] = yelp_query(city_name, "pet+groomer", "url")
        except:
            print("   city_groomer_url was not found")
        try:
            fields["city_park_url"] = yelp_query(city_name, "dog+park", "url")
        except:
            print("   city_park_url was not found")
        try:
            fields["city_pic"] = yelp_query(city_name, "city", "image_url")
        except:
            print("   city_pic was not found")
        try:
            fields["city_vet_pic"] = yelp_query(city_name, "veterinarian", "image_url")
        except:
            print("   city_vet_pic was not found")
        try:
            fields["city_groomer_pic"] = yelp_query(city_name, "pet+groomer", "image_url")
        except:
            print("   city_groomer_pic was not found")
        try:
            fields["city_park_pic"] = yelp_query(city_name, "dog+park", "image_url")
        except:
            print("   city_park_pic was not found")
        try:
            fields["city_url"] = city_name_urlized
        except:
            print("   city_url was not found in query")
        try:
            fields["city_blurb"] = yelp_query(city_name, "city", "snippet_text")
        except:
            print("   city_blurb was not found in query")
        fixture_element = {"model" : "nsaid.City", "pk" : pk, "fields" : fields}
        fixture_list.append(fixture_element)
        pk += 1
    #    fixture_superlist += fixture_list
    city_file = open("../../nsaid/fixtures/cities_fixture.json", "w")
    json.dump(fixture_list, city_file, indent = 4)
    city_file.close()
    
def yelp_query(city, term, field_name):

    # setup for yelp requests
    yelp_params = {}
    consumer_key = "KUvBeJ9O5nV23Bg5lBGLUA"
    consumer_secret = "K-xQZ9Y8moKw1C71Qsn61MaM0t0"
    token = "VchJDQRV1LyH_ZHoawrotybgyuuVN-IW"
    token_secret = "eWqGCYQrFV9QcE2Ok6LuTvx6p7g"

    session = rauth.OAuth1Session(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = token, access_token_secret = token_secret)

    yelp_params["location"] = city 
    yelp_params["term"] = term
    yelp_params["limit"] = 1
    yelp_response = session.get("http://api.yelp.com/v2/search", params = yelp_params)
    d = yelp_response.json()
    #print(json.dumps(d, indent = 4))
    result = str(d["businesses"][0][field_name])
    #print("yelp " + field_name + " " + result)
    #session.close()
    #print("yelp " + field_name + " " + result)
    return result

def google_query(term):
    url = 'http://ajax.googleapis.com/ajax/services/search/web'
    payload = {"v" : 1.0, "q" : term}
    r = requests.get(url, params = payload)
    #print(json.dumps(r.json(), indent = 4))
    #print("google " + r.json()["responseData"]["results"][0]["visibleUrl"])
    result = str(r.json()["responseData"]["results"][0]["visibleUrl"])
    #print("google " + term + " " + result)
    return result 

def create_shelters_file(city_list, shelter_count):
    """
    given a city, find <25 shelters associated with it and only include them if their city field matches
    return the list of shelter objects
    costs one request per city in city_list
    """
    # query petfinder using shelters.find
    # parse the json as a list of shelter objects
    # later, do filtering
    # return it
    # http://api.petfinder.com/shelter.find?key=2933122e170793b4d4b60358e67ecb65&location=78723&format=json

    fixture_superlist = []
    pk = 1

    for city, city_urlized in city_list:
        petfinder_url = "http://api.petfinder.com/shelter.find"
        payload = {"key" : "2933122e170793b4d4b60358e67ecb65", "location" : city, "count" : shelter_count, "format" : "json"}
        r = requests.get(petfinder_url, params=payload)
        fixture_list = []
        #print(json.dumps(r.json(), indent = 4))
        for sh in r.json()["petfinder"]["shelters"]["shelter"]:
            #print(str(sh))
            try:
                shelter_fields = {"shelter_id" : "", "shelter_name" : "", "shelter_city_urlized" : "", "shelter_hours" : "", 
                                  "shelter_address" : "", "shelter_phone" : "", "shelter_email" : "", "shelter_city" : "",
                                  "shelter_state" : "", "shelter_lattitude" : "", "shelter_longitude" : "",
                                  "shelter_pic" : "", "shelter_url" : "", "shelter_blurb" : ""
                                 }
                try:
                    shelter_fields["shelter_id"] = sh["id"]["$t"]
                except:
                    print("\nshelter_id\n")
                try:
                    shelter_fields["shelter_name"] = sh["name"]["$t"]
                except:
                    print("\nshelter_name\n")
                try:
                    shelter_fields["shelter_city_urlized"] = city_urlized
                except:
                   print("\nshelter_city_urlized\n")
                try:
                    shelter_fields["shelter_hours"] = ""
                except:
                    print("\nshelter_hours\n")
                try:
                    shelter_fields["shelter_address"] = sh["address1"]["$t"]
                except:
                    print("\nshelter_address\n")
                try:
                    shelter_fields["shelter_phone"] = sh["phone"]["$t"]
                except:
                    print("\nshelter_phone\n")
                try:
                    shelter_fields["shelter_email"] = sh["email"]["$t"]
                except:
                    print("\nshelter_email\n")
                try:
                    shelter_fields["shelter_city"] = sh["city"]["$t"]
                except:
                    print("\nshelter_city\n")
                try:
                    shelter_fields["shelter_state"] = sh["state"]["$t"]
                except:
                    print("\nshelter_state\n")
                try:
                    shelter_fields["shelter_lattitude"] = sh["latitude"]["$t"]
                except:
                    print("\nshelter_lattitude\n")
                try:
                    shelter_fields["shelter_longitude"] = sh["longitude"]["$t"]
                except:
                    print("\nshelter_longitude\n")
                try:
                    shelter_fields["shelter_pic"] = yelp_query(city, sh["name"]["$t"], "image_url")
                except Exception as e:
                    print("\nshelter_pic\n" + str(e))
                try:
                    shelter_fields["shelter_url"] = google_query(sh["name"]["$t"])
                except Exception as e:
                    print("\nshelter_url\n" + str(e))
                try:
                    shelter_fields["shelter_blurb"] = yelp_query(city, sh["name"]["$t"], "snippet_text")
                except Exception as e:
                    print("\nshelter_blurb\n" + str(e))
              
            except Exception as e:
                # do nothing on KeyError, but don't append an object missing essential attributes to the list
                #pass
                print("\ncreating shelter " + sh["name"]["$t"] + "\n" + str(e) + "\n" + str(json.dumps(sh, indent = 4)))
            else:
                fixture_element = {"model" : "nsaid.Shelter", "pk" : pk, "fields" : shelter_fields}
                fixture_list.append(fixture_element)
                pk += 1
        fixture_superlist += fixture_list
    shelter_file = open("../../nsaid/fixtures/shelters_fixture.json", "w")
    json.dump(fixture_superlist, shelter_file, indent = 4)
    shelter_file.close()



def create_pets_file(pet_count):
    """
    given a shelter (json object)
    query for all pets associated with a shelter
    return a list of pets (json objects)
    costs one request per shelter (4) in EACH city
    """
    fixture_superlist = []
    pk = 1

    print("count is " + str(pet_count))
    shelters_file = json.loads(open("../../nsaid/fixtures/shelters_fixture.json").read())
    master_pets = []
    for shelter in shelters_file:
        #pets = pet_validate(city.city_name, city.city_state, "pet_city", "pet_state", pets_per_shelter(shelter))
        #print(shelter["fields"]["shelter_id"] + " " + shelter["fields"]["shelter_city"])
        petfinder_url = "http://api.petfinder.com/shelter.getPets"
        payload = {"key" : "2933122e170793b4d4b60358e67ecb65", "id" : shelter["fields"]["shelter_id"], "count" : pet_count, "format" : "json"}
        print("\ncreating pets for shelter " + shelter["fields"]["shelter_id"])
        r = requests.get(petfinder_url, params = payload)
        fixture_list = []
        #print("*** " + json.dumps(r.json()["petfinder"]["pets"], indent = 4))
        try:
            pet_list = r.json()["petfinder"]["pets"]["pet"]
            #print("pet_list " + json.dumps(pet_list, indent = 4))
            print("type of pet list is " + str(type(pet_list)) + " and len of pet_list is " + str(len(pet_list)))
            assert type(pet_list) == list
            assert len(pet_list) > 1
            for p in pet_list:
                print("\n   about to create a pet: " + p["name"]["$t"] + " from shelter " + p["shelterId"]["$t"] + " " + shelter["fields"]["shelter_name"])
                try:
                    thumb = ""
                    big = ""
                    photo_list = p["media"]["photos"]["photo"]
                    for photo in photo_list:
                        if photo["@id"] == "1":
                            if photo["@size"] == "pnt":
                                thumb = photo["$t"]
                            elif photo["@size"] == "x":
                                big = photo["$t"]
                    #print("thumb = " + thumb + " big = " + big + "\n" + str(json.dumps(p, indent = 4)))
                    pet_fields = {}
                    try:
                        pet_fields["pet_id"] = p["id"]["$t"]
                    except:
                        print("pet_id")
                    try:
                        pet_fields["pet_name"] = p["name"]["$t"]
                    except:
                        print("pet_name")
                    try:
                        pet_fields["pet_age"] = p["age"]["$t"]
                    except:
                        print("pet_age")
                    try:
                        pet_fields["pet_sex"] = p["sex"]["$t"]
                    except:
                        print("pet_sex")
                    try:
                        pet_fields["pet_size"] = p["size"]["$t"]
                    except:
                        print("pet_size")
                    try:
                        pet_fields["pet_breed"] = p["breeds"]["breed"]["$t"]
                    except:
                        print("pet_breed")
                    try:
                        pet_fields["pet_shelter"] = p["shelterId"]["$t"]
                    except:
                        print("pet_shelter")
                    try:
                        pet_fields["pet_city"] = shelter["fields"]["shelter_city"]
                    except:
                        print("pet_city")
                    try:
                        pet_fields["pet_city_urlized"] = shelter["fields"]["shelter_city_urlized"]
                    except:
                        print("pet_city_urlized")
                    try:
                        pet_fields["pet_state"] = shelter["fields"]["shelter_state"]
                    except:
                        print("pet_state")
                    try:
                        pet_fields["pet_pic_url"] = thumb
                    except:
                        print("pet_pic_url")
                    try:
                        pet_fields["pet_pic_large"] = big
                    except:
                        print("pet_pic_large")
                    try:
                        pet_fields["pet_url"] = "id" + p["id"]["$t"]
                    except:
                        print("pet_url")
                    try:
                        pet_fields["pet_shelter_url"] = p["shelterId"]["$t"]
                    except:
                        print("pet_shelter_url")
                    try:
                        pet_fields["pet_city_url"] = shelter["fields"]["shelter_city_urlized"]
                    except:
                        print("pet_city_url")
                    try:
                        pet_fields["pet_shelter_name"] = shelter["fields"]["shelter_name"]
                    except:
                        print("pet_shelter_name")
                except Exception as e:
                    #pass
                    print("   problem creating pet " + p["id"]["$t"] + " no photos")
                else:
                    fixture_element = {"model" : "nsaid.Pet", "pk" : pk, "fields" : pet_fields}
                    fixture_list.append(fixture_element)
                    pk += 1
                #break
        except Exception as e:
            #pass
            print("*** Exception creating pets from shelter " + shelter["fields"]["shelter_id"]  + " " + shelter["fields"]["shelter_name"]);
            #print(json.dumps(r.json()["petfinder"]["pets"]["pet"], indent = 4))
        fixture_superlist += fixture_list
        #break
    pet_file = open("../../nsaid/fixtures/pets_fixture.json", "w")
    json.dump(fixture_superlist, pet_file, indent = 4)    
    #rint(json.dumps(fixture_superlist, indent = 4))
    #return fixture_superlist



if __name__ == "__main__" :
    #city_list = [("austin tx", "austin")] #, "san antonio tx", "houston+tx", "san+francisco+ca", "dallas+tx", "el+paso+tx", "new+orleans+la"]

    city_list = [("Austin TX", "austin"), ("San Antonio TX", "san_antonio"), ("Houston TX", "houston"), ("San Francisco CA", "san_francisco"), ("New Orleans LA", "new_orleans")]
    
    create_cities_file(city_list)

    #print(yelp_query("austin tx", "vetrinarian", "image_url"))
    #print(google_query("Austin pets alive"))

    #create_shelters_file(city_list, 2)
    #create_pets_file(10)
    
    #create_city_file(city_list)

