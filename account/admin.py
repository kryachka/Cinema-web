from django.contrib import admin

from account.models import *


class Admin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    list_filter = ['name']
    search_fields = ['name', 'user']
    fields = ["user", 'name']


class Meta:
    model = Profile


admin.site.register(Profile, Admin)


# Register your models here.
