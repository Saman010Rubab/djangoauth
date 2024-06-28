from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product
from .serializers import UserSerializer, ProductSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class= UserSerializer

class SignupView(APIView):

    # queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        # if not data.get('username') or not data.get('email') or not data.get('password'):
        #     return Response({"error": "Please enter all required fields."}, status=status.HTTP_400_BAD_REQUEST)
        
        # user = User.objects.create_user(
        #     username=data['username'],
        #     email=data['email'],
        #     password=data['password'],
        # )
        # user.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SigninView(APIView):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request):
        # serializer = UserSerializer(data=request.data)
        data = request.data
        if not data.get('username') or not data.get('password'):
            return Response({"error": "Please enter all required fields."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request, username=data['username'], password=data['password'])
        if user:
            login(request, user)
            return Response({"message": "Login successful."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Wrong username/password"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]




class signup(View):
    template_name= "polls/signup.html"
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        if request.method== 'POST':
            data = request.POST
            if not data['username'] or not data['email'] or not data['password']:
                return render(request, "polls/signup.html", {
                    "error": "Please enter all required fields.",
                })
            u = User.objects.create_user(
                username=data['username'] ,
                email=data['email'],
                password=data['password'],
            )
            u.save()
            return render(request, "polls/signin.html")
        
class signin(View):
    template_name = "polls/signin.html"
    def get(self, request):
        return render(request, "polls/signin.html")

    def post(self, request):
        if request.method == 'POST': 
            data = request.POST
            if not data['username'] or not data['password']:
                return render(request, "polls/signin.html", {
                    "error": "Please enter all required fields.",
                })
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("polls:products"))
            else:
                return render(request, "polls/signin.html", {
                    "error": "Wrong username/password",
                })

       

@login_required(login_url="/signin")
def logout_user(request):
    username = request.user.username
    logout(request)
    return render(request, "polls/signin.html")

class ProductsView(LoginRequiredMixin, generic.ListView):
    login_url = "/signin"
    template_name = "polls/products.html"
    context_object_name = "products"
    
    def get_queryset(self):
        return Product.objects.all()

class addproduct(LoginRequiredMixin,View):
    login_url = "/signin"
    template_name= "polls/addproduct.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            if not request.POST['p_name'] or not request.FILES['p_img']:
                raise KeyError
        except(KeyError):
            return render(request,
                "polls/addproduct.html", 
                {"error":"something went wrong!"})
        else:
            data = request.POST['p_name']
            files = request.FILES['p_img']
            product = Product(name=data, image=files)
            product.save()
            return HttpResponseRedirect(reverse("polls:products"))


    