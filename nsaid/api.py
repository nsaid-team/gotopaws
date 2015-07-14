
"""
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from . import models
#from wc_app.prettyPrint import *
from tastypie.constants import *
from django.conf.urls import *
"""

from models import Pet
#from nsaid.models import Pet
from tastypie.resources import ModelResource

"""
class PetResource(ModelResource):
    class Meta:
        queryset = Pet.objects.all()
        resource_name = 'pets'
        settings.configure()
        authorization = Authorization()
        serializer = PrettyJSONSerializer()
        filtering = {
            "pet_name" : ALL,
            "pet_id"   : ALL
        }
        detail_uri_name = 'pet_name'

    def prepend_urls(self):
        return [ url(r"^(?P<resource_name>%s)/(?P<pet_name>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"), ]

    def determine_format(self, request):
        return "application/json"
"""

class PetResource(ModelResource):
    class Meta:
        queryset = Pet.objects.all()
        resource_name = 'pets'
