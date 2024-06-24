from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


from .models import Product


def index(request):
    products= Product.objects.all()
    return render(request, "polls/products.html" , {"products": products})

def addproduct(request):
    # products= Products.objects.all()
    return HttpResponse("Hello, world. You're at the polls index.")