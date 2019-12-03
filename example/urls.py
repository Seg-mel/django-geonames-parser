# coding=utf-8
from __future__ import unicode_literals, print_function

from django.urls import path

from views import SearchView


urlpatterns = [
    path('', SearchView.as_view(), name='search'),
]
