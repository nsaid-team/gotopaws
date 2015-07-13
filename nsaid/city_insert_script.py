
from nsaid.models import *

city_list = [
            {
                "name": "Austin",
                "state": "TX",
                "country": "US",
                "shelters": ["TX1218"],
                "pets": ["32251618"],
                "vet_url": "http://www.yelp.com/biz/corner-vet-austin-3",
		"groomer_url": "http://m.yelp.com/biz/groom-envy-austin",
		"park_url": "http://www.yelp.com/biz/auditorium-shores-leash-free-dog-zone-austin-3"
            },
            {
                "name": "San Francisco",
                "state": "CA",
                "country": "US",
                "shelters": ["CA1287"],
                "pets": ["32607766"],
                "vet_url":"http://www.yelp.com/biz/san-francisco-pet-hospital-san-francisco",
		"groomer_url": "http://www.yelp.com/biz/doggie-day-spaw-san-francisco-2",
		"park_url": "http://www.yelp.com/biz/corona-heights-park-san-francisco"
            },
            {
                "name": "Houston",
                "state": "TX",
                "country": "US",
                "shelters": ["TX154"],
                "pets": ["20758336"],
                "vet_url":"http://www.yelp.com/biz/midtown-veterinary-hospital-houston",
		"groomer_url": "http://www.yelp.com/biz/krisers-natural-pet-houston-3",
		"park_url": "http://www.yelp.com/biz/johnny-steele-dog-park-houston"
            }
        ]

for d in city_list:
    q = 0
    q = City(name=d["name"], state=d["state"], country=d["country"], vet_url=d["vet_url"])
    q.save() 
