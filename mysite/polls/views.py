from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required



from .models import Product


def index(request):
    return render(request, "polls/signin.html")


def signup(request):
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
    else:  
        return render(request, "polls/signup.html")

    

def signin(request):
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
    else:  
        return render(request, "polls/signin.html")

@login_required(login_url="/polls/signin")
def logout_user(request):
    username = request.user.username
    logout(request)
    return render(request, "polls/signin.html")

@login_required(login_url="/polls/signin")
def products(request):
    products= Product.objects.all()
    return render(request, "polls/products.html" , {"products": products})


@login_required(login_url="/polls/signin")
def addproduct(request):
    return render(request, "polls/addproduct.html")

@login_required(login_url="/polls/signin")
def newproduct(request):
    data = request.POST['p_name']
    files = request.FILES['p_img']
    try:
        if not data or not files:
            raise KeyError
    except(KeyError):
        return render(request,
            "polls/addproduct.html", 
            {"error":"something went wrong!"})
    else:
        product = Product(name=data, image=files)
        product.save()
        return HttpResponseRedirect(reverse("polls:index"))
    