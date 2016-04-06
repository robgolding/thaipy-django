from django.conf.urls import url

from thaipy.meetup.views import index, events

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^events/$', events, name='events'),
]
