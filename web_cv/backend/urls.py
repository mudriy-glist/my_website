from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('playground/', views.playground, name='playground')
]