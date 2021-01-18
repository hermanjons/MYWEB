from django.contrib import admin

from news.models import News



class New(admin.ModelAdmin):
    prepopulated_fields={"slug":("Başlık",)}




admin.site.register(News,New)    