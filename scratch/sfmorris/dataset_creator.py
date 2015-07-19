#!/usr/bin/env python3

import rauth
import sys
import json
import pprint

def create_city_file():
    """
    returns a dict 
    """

    params = {}
    params["limit"] = "3"

    consumer_key = "KUvBeJ9O5nV23Bg5lBGLUA"
    consumer_secret = "K-xQZ9Y8moKw1C71Qsn61MaM0t0"
    token = "VchJDQRV1LyH_ZHoawrotybgyuuVN-IW"
    token_secret = "eWqGCYQrFV9QcE2Ok6LuTvx6p7g"

    session = rauth.OAuth1Session(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = token, access_token_secret = token_secret)
    biz_list = []

    for location in ("austin+tx", "san+antonio+tx", "houston+tx"):
        params["location"] = location
        for term in ("veterinarian", "pet+groomer", "dog+park"):
            params["term"] = term
            # Get a json response and stuff it in response_r
            response_r = session.get("http://api.yelp.com/v2/search", params=params)
            # Create a (single-quoted) dict object out of response_r
            d = response_r.json()
            # Give the key value "businesses" and get just the (single-quoted) list_of_businesses value
            list_of_businesses = d["businesses"]
            # Add every business in list_of_businesses to biz_list
            biz_list += list_of_businesses

    # json.dumps() expects a dict    
    dict_to_dump = { "biz" : biz_list }
    # Print the double-quoted json string -- it will be parseable to later programs
    print(json.dumps(dict_to_dump))

    session.close()

def get_valid_shelters(city_list):
    """
    given a list of cities, query petfinder for all shelters in the city and only filter through
    if they have certain fields filled and if their city matches for simplicity. list < 25 for simplicity too.
    return the list of verified cities
    """
    return['TX21', 'TX1051',]

def build_pets_info(valid_shelter_list):
    """
    given a list of shelters, query the top 25 pets
    return the pet info in a json string suitable for printing to Pets.json
    """
    return '[{"model":"nsaid.Pet", "pk":10, "fields":{"pet_name":"Gracie"}}]'

if __name__ == "__main__" :
    #create_city_file()
    city_list = ['Austin+TX', 'Houston+TX',]
    valid_shelter_list = get_valid_shelters(city_list)
    pets_info = build_pets_info(valid_shelter_list)

        
