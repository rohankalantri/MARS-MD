from django.urls import path
from django.conf.urls import include, url 
from . import views

urlpatterns = [
	url(r'^$', views.login, name='login'),
    url(r'^home/', views.index, name='index'),
    ]