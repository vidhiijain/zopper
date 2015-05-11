from tastypie.resources import ModelResource
from models import DataStore
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie.cache import SimpleCache
from tastypie.resources import ModelResource


cache = SimpleCache(cache_name='resources', timeout=10)


class EntryResourceGovLog(ModelResource):

    class Meta:
        queryset = DataStore.objects.all()
        resource_name = 'entry'
        authorization = Authorization()
        filtering = {"device_name": ALL, "magnification": ALL, "field_of_view": ALL, "range": ['exact', 'gt', 'lt', 'lte', 'gte']}
	cache = SimpleCache(timeout=10)
