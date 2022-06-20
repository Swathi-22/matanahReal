from unicodedata import category
from django.shortcuts import render
from web.models import Category,Product,Gallery



def index(request):
    category=Category.objects.all()
    product = Product.objects.all()[:8]
    products=Product.objects.filter(is_popular=True)[:3]
    context = {
        "is_index":True,
        'category':category,
        'product':product,
        'products':products
    }
    return render(request,'web/index.html',context)


def about(request):
    context = {
        "is_about":True
    }
    return render(request,'web/about.html',context)


def product(request,slug):
    product=Product.objects.all()
    category=Category.objects.all()
    if slug != "all":
        product=Product.objects.filter(category__slug=slug)

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


