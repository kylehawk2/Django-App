from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^create', views.index),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit', views.edit),
    url(r'^(?P<number>\d+)/delete', views.delete),
    url(r'^new', views.new)
]