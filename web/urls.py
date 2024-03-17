from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ticket/', views.ticket, name='ticket'),
    path('signup/', views.login, name='signup'),
    path('test/', views.test, name='test1')
]