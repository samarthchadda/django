from django.contrib import admin

# Register your models here.

from .models import PostModel

#registering in admin
admin.site.register(PostModel)
