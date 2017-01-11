from django.conf import settings
from django.utils import dateformat
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render_to_response

from apps.home.models import Articles


def home(request):
    articles = Articles.objects.all()
    return render_to_response('home/home.html', {'articles': articles})
