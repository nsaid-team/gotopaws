
from nsaid.models import *

city_list = [
            {
                "name": "Austin",
                "state": "TX",
                "country": "US",
                "shelters": ["TX1218"],
                "pets": ["32251618"],
                "vet_url": "http://www.yelp.com/biz/corner-vet-austin-3"
            },
            {
                "name": "San Francisco",
                "state": "CA",
                "country": "US",
                "shelters": ["CA1287"],
                "pets": ["32607766"],
                "vet_url":"http://www.yelp.com/biz/san-francisco-pet-hospital-san-francisco"
            },
            {
                "name": "Houston",
                "state": "TX",
                "country": "US",
                "shelters": ["TX154"],
                "pets": ["20758336"],
                "vet_url":"http://www.yelp.com/biz/midtown-veterinary-hospital-houston"
            }
        ]

for d in city_list:
    q = 0
    q = City(name=d["name"], state=d["state"], country=d["country"], vet_url=d["vet_url"])
    q.save() 
