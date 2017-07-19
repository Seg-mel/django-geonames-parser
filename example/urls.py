# coding=utf-8
from __future__ import unicode_literals, print_function

from django.conf.urls import url

from views import SearchView


urlpatterns = [
    url(r'^$', SearchView.as_view(), name='search'),
]
