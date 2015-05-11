import django_filters
from models import *


class DSFilterForm(django_filters.FilterSet):

    class Meta:
        model = DataStore
        fields = {'device_name' : ['icontains'],
                  'magnification': ['icontains'],
                  'field_of_view':['icontains'],
                  'range': ['gt', 'lt', 'exact']
        }
