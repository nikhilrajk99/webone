
from django.shortcuts import render, get_object_or_404

from .models import Category,Products


# Create your views here.
def allProdCat(request,c_slug=None):
    c_page=None
    product=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        product=Products.objects.all().filter(category=c_page,available=True)
    else:
        product=Products.objects.all().filter(available=True)
    return render(request,"category.html",{'category':c_page,'product':product})

def ProdCatdetail(request,c_slug,products_slug):
    try:
        product=Products.objects.get(category__slug=c_slug,slug=products_slug)
    except Exception as e:
        raise e
    return render(request,"product.html",{'product':product})

