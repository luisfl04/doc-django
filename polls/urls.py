from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "frist_index"),
    path("", views.secondindex, name = "second_index")
]