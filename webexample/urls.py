from django.conf.urls import url###patterns, include

from webexample.views import basic_one

urlpatterns = [
url(r'^/1', basic_one)
]