from django.urls import path
from django.conf.urls import include, url 
from . import views

urlpatterns = [
	url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^forgot_password/', views.forgot_password, name='forgot_password'),
    url(r'^doc/', views.docSignUp, name='docSignUp'),
    url(r'^otp_confirmation/', views.otp_confirmation, name='otp'),
    url(r'^$', views.index, name='index'),
    url(r'news/$', views.news, name='news'),
    url(r'appointments/$', views.appointments, name='appointments'),
    url(r'blog1/$', views.blog1, name='blog1'),
    url(r'blog2/$', views.blog2, name='blog2'),
    url(r'blog3/$', views.blog3, name='blog3'),
    url(r'about/$', views.about, name='about'),
    url(r'location/$', views.location, name='location'),
    #sbadmin
    url(r'^admin_index/', views.sbadminIndex, name='index'),
    url(r'^admin_Login/', views.adminLogin, name='index'),
    url(r'^tables/', views.tables, name='index'),
    url(r'^charts/', views.charts, name='index'),
    url(r'^register/', views.register, name='index'),
    url(r'^activity/', views.activity, name='index'),
    url(r'^familyadded/', views.familyadded, name='index'),
    url(r'^history/', views.history, name='index'),
    url(r'^hearts/', views.hearts, name='index'),
    url(r'^nutrition/', views.nutrition, name='index'),
    url(r'^appointment_display/', views.appointment_display, name='index'),
    ]