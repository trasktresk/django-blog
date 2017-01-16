from django.conf import settings
from django.utils import dateformat
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render

from apps.articles.models import Articles
from apps.articles.views import ArticlesView


class HomeView(ArticlesView):
    def get(self, request):
        return render(request, 'home/home.html', {'articles': self.articles})
