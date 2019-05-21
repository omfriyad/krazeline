from django.urls import path
from blog.views import *

urlpatterns = [
    path('', index, name='blog'),
    path('new', new, name='new')
]
