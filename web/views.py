from unicodedata import category
from django.shortcuts import render
from web.models import Category,Product,Gallery,Advertisement
from .forms import ContactForm
from django.http import HttpResponse
import json


def index(request):
    category=Category.objects.all()
    product = Product.objects.all()[:6]
    # sub_category=SubCategory.objects.all()
    products=Product.objects.filter(is_popular=True)[:6]
    # products_featured=Product.objects.filter(is_featured=True)[:6]
    ad=Advertisement.objects.all()
    context = {
        "is_index":True,
        'category':category,
        'product':product,  
        'products':products,
        # 'products_featured':products_featured,
        'ad':ad,
        # 'sub_category':sub_category
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
    category_name="All Products"
    if slug != "all":
        product=Product.objects.filter(category__slug=slug)
        category_name=Category.objects.get(slug=slug).title

 
    context = {
        "is_product":True,
        "product":product,
        "category":category,
        "category_name":category_name
      
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



def popular(request):
    popular_products=Product.objects.filter(is_popular=True)
    context = {
        'popular_products':popular_products
    }
    return render(request,'web/popular-items.html',context)