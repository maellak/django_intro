from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calculate/', 'shapes.views.calculate', name='calculate'),
    url(r'^save/', 'shapes.views.save', name='save'),
    url(r'^$', 'shapes.views.home', name='home'),
)
