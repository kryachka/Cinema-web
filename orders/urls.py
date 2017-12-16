

from django.conf.urls import url, include
from django.contrib import admin
from .import views


admin.autodiscover()
urlpatterns = [

    #url(r'^login/', views.account, name="account"),

]
