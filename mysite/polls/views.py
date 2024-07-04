from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views import View 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Product


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

       

@login_required(login_url="/polls/")
def logout_user(request):
    username = request.user.username
    logout(request)
    return render(request, "polls/signin.html")

class ProductsView( LoginRequiredMixin, generic.ListView):
    login_url="/polls/"
    template_name = "polls/products.html"
    context_object_name = "products"
    paginate_by = 6
    def get_queryset(self):
        return Product.objects.all()

class addproduct(LoginRequiredMixin,View):
    login_url="/polls/"
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


    