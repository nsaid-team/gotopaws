from nsaid.models import *

pet_list = [
    {
            "petsid":"A4856",
            "name":"Sari",
            "age":"Adult",
            "size":"S",
            "breed":"Russian Blue",
            "shelter":"TX154",
            "city":"Houston",
            "pic_url":"http://photos.petfinder.com/photos/pets/20758336/3/?bust=1314882859&width=60&-pnt.jpg"
        },
        {
            "petsid":"27958804",
            "name":"Earl",
            "age":"Senior",
            "size":"M",
            "breed":"Poodle",
            "shelter":"CA1287",
            "city":"San Francisco",
            "pic_url":"http://photos.petfinder.com/photos/pets/32607766/1/?bust=1435783518&width=60&-pnt.jpg"
        },
        {
            "petsid":"27921188",
            "name":"Rangel",
            "age":"Young",
            "size":"L",
            "breed":"German Shepherd Dog",
            "shelter":"TX1218",
            "city":"Austin",
            "pic_url":"http://photos.petfinder.com/photos/pets/32251618/1/?bust=1435667817&width=60&-pnt.jpg"
    }
]

for d in pet_list:
    q = 0
    q = Pet(petsid=d["petsid"], pet_name=d["name"], age=d["age"], size=d["size"], breed=d["breed"], pet_shelter=d["shelter"], pet_city=d["city"], pic_url=d["pic_url"])
    q.save()
