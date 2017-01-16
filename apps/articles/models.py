from django.db import models


class Categories(models.Model):
    name = models.CharField('Название категории', max_length=255)
    slug = models.SlugField('Alias категории', unique=True)
    parent_id = models.IntegerField('Родительская категории', default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Articles(models.Model):
    name = models.CharField('Название статьи', max_length=255)
    create_date = models.DateField('Дата публикации')
    short_text = models.TextField('Аннотация статьи', default='')
    text = models.TextField('Текст статьи', default='')
    category_id = models.ForeignKey(Categories)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-create_date']

    def __str__(self):
        return self.name
