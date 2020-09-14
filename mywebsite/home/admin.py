from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.MangaType)
admin.site.register(models.MangaInfo)
admin.site.register(models.ChapInfo)
admin.site.register(models.MangaContent)

