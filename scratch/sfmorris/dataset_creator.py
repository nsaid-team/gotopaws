#!/usr/bin/env python3

import rauth
import sys
import json
import pprint

def create_city_file(city_list):
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

    for location in (city_list):
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

def shelters_per_city(city):
    """
    given a city, find <25 shelters associated with it and only include them if their city field matches
    return the list of shelter objects
    """

if __name__ == "__main__" :
    city_list = ["austin+tx", "san+antonio+tx", "houston+tx", "san+francisco+ca", "dallas+tx", "el+paso+tx", "new+orleans+la"]
    #create_city_file(city_list)
    master_spc = []
    for city in city_list:
        spc = shelters_per_city(city)
        master_spc += spc
    for shelter in master_spc:
        # grab a bunch of pets, only if their city name matches a city
    # drop any empty shelters?
