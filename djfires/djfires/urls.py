from django.conf.urls import patterns, include, url
from django.contrib import admin
import fires_app

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djfires.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/salmonella/', include('salmonella.urls')),
    url(r'^fire/', include('fires_app.urls')),
)
