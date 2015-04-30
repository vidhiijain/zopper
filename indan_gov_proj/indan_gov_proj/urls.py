from django.conf.urls import include, url, patterns
from django.contrib import admin
from indian_gov_app.api import EntryResourceGovLog

admin.autodiscover()

entry_resource = EntryResourceGovLog()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(entry_resource.urls)),
                       url(r'^search/', include('indian_gov_app.urls')),

)
