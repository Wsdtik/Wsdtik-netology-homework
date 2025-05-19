from django.urls import path
from . import views

urlpatterns = [
    path('<str:dish_name>/', views.get_recipe), # type: ignore
]