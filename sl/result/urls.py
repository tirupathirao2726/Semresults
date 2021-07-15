from django.urls import path
from result import views
urlpatterns=[
    path('',views.home,name='home'),#this url for displaying results url page
]
