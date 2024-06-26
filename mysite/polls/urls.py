from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # path("", views.index, name="index"),
    path("signup/", views.signup.as_view(), name="signup"),
    path("", views.signin.as_view(), name="signin"),
    path("logout/", views.logout_user, name="logout"),
    path("products/", views.ProductsView.as_view(), name="products"),
    path("addproduct/", views.addproduct.as_view(), name="add_product"),
]