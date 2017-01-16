from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.utils import dateformat
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from django.shortcuts import render
from django.views import View

from .models import Articles


class ArticlesView(View):
    articles = Articles.objects.all()

    def get(self, request):
        return render(request, 'articles/articles.html', {'articles': self.articles})


class ArticleView(View):
    def get(self, request, article_id):
        try:
            article = Articles.objects.get(id=article_id)
            return render(request, 'articles/article.html', {'article': article})
        except ObjectDoesNotExist:
            raise Http404
