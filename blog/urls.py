from django.urls import path
from .views import *
urlpatterns =[
    path('',index,name='index'),
    path('detel/<int:id>',index_detel,name="detel")
    ]