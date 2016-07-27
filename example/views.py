# coding=utf-8
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from geo_names.models import CityAlternate


class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search', u'')
        return render(
            request,
            self.template_name,
            {'search': search,
             'cities': set([ca.city for ca in CityAlternate.objects.filter(
                 Q(name__istartswith=search) |
                 Q(city__name__istartswith=search)
             )])},
        )
