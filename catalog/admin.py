from django.contrib import admin
from .models import Category, Course

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug', 'category__name']

admin.site.register(Category)
admin.site.register(Course)
