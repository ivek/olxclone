from django.shortcuts import render
from .models import Product

# Create your views here.
def productlist(request):
    productlist= Product.objects.all()

    context= {'products_list':productlist}
    template= 'product/product_list.html'
    return render(request, template, context)


def productdetail(request,product_slug):
    productdetail= Product.objects.get(slug=product_slug)
    template= 'product/product_detail.html'
    context= {'product_detail':productdetail}
    return render(request, template, context)

