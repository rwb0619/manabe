from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Action)
admin.site.register(models.Permission)
