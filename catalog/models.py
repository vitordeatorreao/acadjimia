# coding=utf-8

from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Nome', max_length=128)
    slug = models.SlugField('Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('name',)

class CourseManager(models.Manager):

    def featured(self):
        return self.filter(featured=True)

class Course(models.Model):

    name = models.CharField('Nome', max_length=256)
    slug = models.SlugField('Slug')
    category = models.ForeignKey(Category, verbose_name='Categoria')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de Início', blank=True)
    featured = models.BooleanField('Destaque', default=False, blank=True)
    price = models.DecimalField(
        'Preço', default=0, decimal_places=2, max_digits=8
    )
    objects = CourseManager()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ('name',)

    def __str__(self):
        return self.name
