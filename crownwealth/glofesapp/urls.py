from django.urls import path
from . import views
# i CREATED THIS FILE MYSELF
urlpatterns = [path('', views.index, name='index'),]