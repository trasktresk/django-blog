from django.contrib import admin

from .models import Categories
from .models import Articles

admin.site.register([Categories, Articles])