from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("addproduct", views.addproduct, name="add_product")
]