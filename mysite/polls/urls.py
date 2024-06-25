from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout_user, name="logout"),

    path("products/", views.products, name="products"),
    path("addproduct/", views.addproduct, name="add_product"),
    path("newproduct/", views.newproduct, name="new_product")

]