from django.conf.urls import url###patterns, include

from webexample.views import *

urlpatterns = [
    url(r'^/1', basic_one),
    url(r'^/2', template_two),
    url(r'^/3', template_three)
]