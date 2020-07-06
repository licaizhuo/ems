from django.contrib import admin

# Register your models here.
from empapi import models

admin.site.register(models.Employee)