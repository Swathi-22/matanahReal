from unicodedata import category
from django.shortcuts import render
from web.models import Category,Product,Gallery



def index(request):
    context = {
        "is_index":True
    }
    return render(request,'web/index.html',context)


def about(request):
    context = {
        "is_about":True
    }
    return render(request,'web/about.html',context)


def product(request):
    product=Product.objects.all()
    category=Category.objects.all()
    context = {
        "is_product":True,
        "product":product,
        "category":category
    }
    return render(request,'web/product.html',context)


def gallery(request):
    gallery=Gallery.objects.all()
    context = {
        "is_gallery":True,
        "gallery":gallery
    }
    return render(request,'web/gallery.html',context)


def contact(request):
    context = {
        "is_contact":True
    }
    return render(request,'web/contact.html',context)
