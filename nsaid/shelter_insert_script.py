from nsaid.models import *

shelter_list = [
        {
            "id":"TX1218",
            "name":"Austin Pets Alive!",
            "address1":"1156 West Cesar Chavez",
            "city":"Austin",
            "state":"TX",
            "phone":"512 961 6519",
            "email":"adopt@austinpetsalive.org",
            "pets":["32251618"]
        },{
            "id":"CA1287",
            "name":"Muttville Senior Dog Rescue",
            "address1":"255 Alabama St",
            "city":"San Francisco",
            "state":"CA",
            "phone":"415 842 0320",
            "email":"adoption@muttville.org",
            "pets":["32607766"]
        },{
            "id":"TX154",
            "name":"Homeless Pet Placement League",
            "address1":"P. O. Box 273027",
            "city":"Houston",
            "state":"TX",
            "phone":"713 862 7387",
            "email":"hppl@hppl.org",
            "pets":["20758336"]
        }
    ]

for d in shelter_list:
    q = 0
    q = Shelter(shelterid=d["id"], name=d["name"], address=d["address1"], city=d["city"], state=d["state"], phone=d["phone"], email=d["email"])
    q.save()
