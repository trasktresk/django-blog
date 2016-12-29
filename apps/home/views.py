from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string

# Create your views here.


def home(request):
    return HttpResponse(render_to_string('home/home.html'))
