from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:dish_name>/', views.get_recipe), 
]