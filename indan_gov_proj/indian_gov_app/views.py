from django.shortcuts import render_to_response
import os
from django.http import HttpResponse
from models import DataStore
from forms import DSFilterForm


def search(request):
    data = DSFilterForm(request.GET, queryset=DataStore.objects.all())
    return render_to_response('query.html', {'data': data})
