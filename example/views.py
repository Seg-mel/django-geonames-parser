# coding=utf-8
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
            {'search': search, 'cities': City.objects.filter(name__icontains=search.lower())},
        )
