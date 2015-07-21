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

def pets :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Pets',
        'url': 'pets',
        'text': 'Search for and find your perfect companion. Rescue a pet and give them a forever home. Picture Name Age Sex Size Breed Shelter City pets    Trixie Bell Senior  F   S   Chihuahua   TX1148  Austin pets    Amigo   Adult   M   S   Chihuahua   TX1148  Austin pets    Lillipup    Baby    F   S   Chihuahua   TX1148  Austin pets    Turner  Young   M   S   Chihuahua   TX1148  Austin pets    Nico    Young   F   S   Chihuahua   TX1148  Austin pets    Cody    Adult   M   S   Chihuahua   TX1148  Austin pets    Vivian - Courtesy Listing   Young   F   M   Domestic Short Hair TX1148  Austin pets    Prissy  Adult   F   S   Chihuahua   TX1148  Austin pets    Skeeter Adult   M   S       TX1148  Austin pets    Georgia Senior  F   S   Pomeranian  TX1148  Austin pets    VINCE   Adult   M   L   Shar Pei    TX295   San Antonio pets    FERLIN  Adult   M   L   Catahoula Leopard Dog   TX295   San Antonio pets    ANISHA  Adult   F   M   Labrador Retriever  TX295   San Antonio pets    WHISPER Senior  F   M   Cattle Dog  TX295   San Antonio pets    SUZIE   Adult   F   L   Shepherd    TX295   San Antonio pets    KODIAK  Adult   F   M   Siberian Husky  TX295   San Antonio pets    FROSTIE Young   F   M   Hound   TX295   San Antonio pets    PETRA   Young   F   M   Retriever   TX295   San Antonio pets    MARLOW  Senior  M   L       TX295   San Antonio pets    PRESLEY Senior  M   M   Terrier TX295   San Antonio pets    Nutmeg  Senior  F   M   Basset Hound    TX1051  Houston pets    Scout   Young   M   M   Basset Hound    TX1051  Houston pets    Milo    Senior  M   M   Basset Hound    TX1051  Houston pets    Sherman III Young   M   M   Basset Hound    TX1051  Houston pets    Huntley Senior  M   M   Basset Hound    TX1051  Houston pets    Rufus   Senior  M   M   Basset Hound    TX1051  Houston pets    Albert  Senior  M   XL  Basset Hound    TX1051  Houston pets    Eva Young   F   M   Basset Hound    TX1051  Houston pets    Remy    Senior  M   M   Basset Hound    TX1051  Houstonpets    Buster  Adult   M   M       TX1283  Houston pets    Annabelle   Adult   F   L   Collie  TX1283  Houston pets    Skylar  Adult   F   L   Collie  TX1283  Houston pets    Connor  Young   M   L   Collie  TX1283  Houston pets    Rolo    Young   M   M       TX1283  Houston pets    Boots   Adult   M   L   Collie  TX1283  Houston pets    Marshall    Young   M   L   Collie  TX1283  Houston pets    Kermit  Adult   M   S   Shetland Sheepdog Sheltie   TX1283  Houston pets    Lady Di & Prince Charles    Adult   F   L   Collie  TX1283  Houston pets    Jake    Young   M   M   Australian Cattle Dog (Blue Heeler) TX1283  Houston pets    Hazel   Adult   F   M   Calico  CA1061  San Francisco pets    Nibbler Adult   M   L   Tabby - Brown   CA1061  San Francisco pets    Minnie  Adult   F   S   Tabby   CA1061  San Francisco pets    Purr    Adult   F   S       CA1061  San Francisco pets    Daphne  Adult   F   S       CA1061  San Francisco pets    Maverick    Adult   M   L       CA1061  San Francisco pets    Emerald aka Emmy    Young   F   S   Domestic Short Hair-black   CA1061  San Francisco pets    Mittens Senior  F   M       CA1061  San Francisco pets    Leila   Senior  F   L   Domestic Short Hair-black and white CA1061  San Francisco pets    Sammy Sweet Cheeks  Adult   M   M       CA1061  San Francisco pets    Molly   Young   F   S   Persian CA1063  San Francisco pets    Derek   Young   M   M   Himalayan   CA1063  San Francisco pets    Lady    Young   F   M   Persian CA1063  San Francisco pets    Lisa    Young   F   M   Persian CA1063  San Francisco pets    Ginger  Adult   F   M       LA204   New Orleans pets    Honey   Adult   F   S       LA204   New Orleans pets    Kermit  Adult   M   L   Domestic Short Hair - orange and white  LA204   New Orleans pets    Thelma  Adult   F   S       LA204   New Orleans pets    Daphy   Young   F   L   Labrador Retriever  LA204   New Orleans pets    Joy Young   F   S   Poodle  LA204   New Orleans pets    Lt. Dan Baby    M   S       LA204   New Orleans pets    Mama D  Adult   F   L   Australian Cattle Dog (Blue Heeler) LA204   New Orleans pets    Sergio  Adult   M   L       LA204   New Orleans pets    Romeo   Adult   M   S   Chihuahua   LA204   New Orleans pets    Cayenne Adult   M   XL      LA305   New Orleans pets    Thomas  Adult   M   L       LA305   New Orleans pets    Kayle   Adult   F   M       LA305   New Orleans pets    STAR    Adult   M   L       LA305   New Orleans pets    Angelina    Adult   F   M       LA305   New Orleans pets    Brad    Adult   M   M       LA305   New Orleans pets    Sampson Adult   M   XL      LA305   New Orleans pets    Moine (indoor outdoor)  Adult   F   M   Tortoiseshell   LA305   New Orleans pets    Valinda Adult   F   XL  Siamese LA305   New Orleans pets    Sam Elliott Young   M   L   Tabby - Grey    LA305   New Orleans',
    })





if __name__ == "__main__" :
    