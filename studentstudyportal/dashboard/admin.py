from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
# Register your models here.


admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)