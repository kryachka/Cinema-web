from django.conf.urls import url
from . import views
urlpatterns = [
# post views
url(r'^log/$', views.user_login, name='log'),
]