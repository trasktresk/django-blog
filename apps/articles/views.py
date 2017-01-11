from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.utils import dateformat
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from django.shortcuts import render_to_response

from apps.home.models import Articles


def show_articles(request):
    articles = Articles.objects.all()
    return render_to_response('articles/articles.html', {'articles': articles})


def show_article(request, article_id):
    try:
        article = Articles.objects.get(id=article_id)
        return render_to_response('articles/article.html', {'article': article})
    except ObjectDoesNotExist:
        raise Http404
