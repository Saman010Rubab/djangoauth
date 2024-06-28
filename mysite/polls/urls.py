from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import SignupView, SigninView, LogoutView, ProductListView, ProductDetailView, UserView
from . import views
# from .views import MyModelViewSet

# router = DefaultRouter()
# router.register(r'signup', SignupView, basename='signup')
# router.register(r'signin', SigninView, basename='signin')
# router.register(r'logout', SigninView, basename='logout')
# router.register(r'products', ProductListView, basename='products')
# router.register(r'productdetail', ProductDetailView, basename='productdetail')
# router.register(r'user', UserView, basename='user')

app_name = "polls"

urlpatterns = [
    # path('api/', include(router.urls)),
    # path('mymodel/', MyModelListView.as_view(), name='mymodel_list'),
    path('api/user/', UserView.as_view(), name='user_api'),
    path('api/signup/', SignupView.as_view(), name='signup_api'),
    path('api/signin/', SigninView.as_view(), name='signin_api'),
    path('api/logout/', LogoutView.as_view(), name='logout_api'),
    path('api/products/', ProductListView.as_view(), name='product-list_api'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail_api'),
    path("signup/", views.signup.as_view(), name="signup"),
    path("signin/", views.signin.as_view(), name="signin"),
    path("logout/", views.logout_user, name="logout"),
    path("products/", views.ProductsView.as_view(), name="products"),
    path("addproduct/", views.addproduct.as_view(), name="add_product"),
]

# from django.urls import path
# from rest_framework import routers,

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# from django.urls import path

# from . import views

# app_name = "polls"
# urlpatterns = [
#     # path("", views.index, name="index"),
#     path("signup/", views.signup.as_view(), name="signup"),
#     path("", views.signin.as_view(), name="signin"),
#     path("logout/", views.logout_user, name="logout"),
#     path("products/", views.ProductsView.as_view(), name="products"),
#     path("addproduct/", views.addproduct.as_view(), name="add_product"),
# ]