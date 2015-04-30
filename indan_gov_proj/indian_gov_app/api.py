from tastypie.resources import ModelResource
from models import DataStore
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource


class EntryResourceGovLog(ModelResource):

    class Meta:
        queryset = DataStore.objects.all()
        resource_name = 'entry'
        authorization = Authorization()
        filtering = {"device_name": ALL, "magnification": ALL, "field_of_view": ALL, "range": ALL}