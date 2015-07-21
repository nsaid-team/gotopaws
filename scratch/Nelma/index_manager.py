#!/usr/bin/env python
import elasticsearch

def home :


def cities :

    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='cities', body={
        'title': 'Cities',
        'url': 'cities',
        'text': 'New to the area? Traveling to a nearby city to find that purrfect pal? Or just looking for something fun to do? Find the top rated vet, groomer, and dog park in the area. Austin TX  US  cities Austin vet  cities Austin park cities Austin groomer city    San Antonio TX  US  cities San Antonio vet cities San Antonio park    cities San Antonio groomer city    Houston TX  US  cities Houston vet cities Houston park    cities Houston groomer city    San Francisco   CA  US  cities San Francisco vet   cities San Francisco park  cities San Francisco groomer city    New Orleans LA  US  cities New Orleans vet cities New Orleans park    cities New Orleans groomer',
    })

def city_1 :

    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Austin',
        'url': 'austin',
        'text': 'TX  US  Bat City, The City of the Violet Crown, The Live Music Capital of the World, The Blueberry in a Red State. These are some of the names that characterize Shelters in Austin Pets in Austin Vets in Austin',
    })

def city_2 :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'San Antonio',
        'url': 'san_antonio',
        'text': 'TX  US I could put on my teacher\'s glasses and give you a history lesson on San Antonio. I could put on some tennis shoes and transform into a tour guide through Shelters in San Antonio Pets in San Antonio Vets in San Antonio',
    })

def city_3 :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Houston',
        'url': 'houston',
        'text': 'TX  US LOL.  The only thing I don\'t like about this city is the damn rain!  So many memories.  -Being Miss Upward Bound at Texas Southern University.  What up Shelters in Houston Pets in Houston Vets in Houston',
    })

def city_4 :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'San Francisco',
        'url': 'san_francisco',
        'text': 'CA  US Sang to the tune of the \"Twelve Days of Christmas \") Fivvvvve parking tickets ....4 rainbow flags....., 3 Union Squares......., 2 Uber rides........ Shelters in San Francisco Pets in San Francisco Vets in San Francisco ',
    })

def city_5 :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'New Orleans',
        'url': 'new_orleans',
        'text': 'LA  US Had an excellent time here in New Orleans or NOLA as a lot of people say! We ate so much wonderful food. I feel like I was always full. Never hungry',
    })








    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', id=2, body={
        'title': 'San Francisco, California',
        'subtitle': 'Gold in peace, iron in war',
        'url': 'sf',
        'shelters_text': 'Shelters in San Francisco... It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)',
        'pets_text': 'Pets in San Francisco... It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)',
        'vets_text': 'Vets in San Francisco... \"5 stars for SF Pet hospital isn\'t enough!\nMy 14 year old cat, Titan got sick from a digestion issue. I brought him to SF Pet Hospital. The staff and vets...\"'
    })

def city_3

    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', id=3, body={
        'title': 'Houston, Texas',
        'subtitle': 'Space City',
        'url': 'City_Houston.html',
        'shelters_text': 'Shelters in Houston... It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)',
        'pets_text': 'Pets in Houston... It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)',
        'vets_text': 'Vets in Houston... \"5 stars for SF Pet hospital isn\'t enough!\nMy 14 year old cat, Titan got sick from a digestion issue. I brought him to SF Pet Hospital. The staff and vets...\"'
    })

def pets :




def shelters :


if __name__ == "__main__" :
    