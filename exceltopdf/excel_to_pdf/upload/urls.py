from django.contrib import admin
from django.urls import path,include
from upload import views

urlpatterns = [
    path('',views.upload1,name="uploading"),
    path('result/', views.result_page, name='result'),
]
