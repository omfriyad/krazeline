from django.urls import path
from . import views
from django.contrib.auth.views import auth_login

urlpatterns = [
    path('', views.index, name='landing'),
    path('error', views.error, name = 'error'),
    path('register', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

]
