# coding=utf-8
from __future__ import unicode_literals, print_function

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView


from geo_names.models import City


class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search', '')
        return render(
            request,
            self.template_name,
            {'search': search,
             'cities': City.objects.filter(
                Q(name__istartswith=search) |
                Q(cityalternate__name__istartswith=search) |
                Q(citylocalename__name__istartswith=search)
             ).distinct()},
        )
