from unicodedata import category
from django.shortcuts import render
from web.models import Category,Product,Gallery
from .forms import ContactForm
from django.http import HttpResponse
import json


def index(request):
    category=Category.objects.all()
    product = Product.objects.all()[:6]
    products=Product.objects.filter(is_popular=True)[:6]
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
    forms = ContactForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted"
            }
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_contact": True,
            "forms": forms,

        }
        return render(request, 'web/contact.html', context)