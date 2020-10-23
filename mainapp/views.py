import random

from basketapp.models import Basket
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Contact, Product, ProductCategory


def main(request):
    title = "главная"
    products = Product.objects.all()[:4]

    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_similar_products(hot_product):
    similar_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return similar_products


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by("price")
            category = {"name": "все"}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by("price")
        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products,
            "media_url": settings.MEDIA_URL,
            "basket": basket,
        }
        return render(request, "mainapp/products_list.html", content)
    hot_product = get_hot_product()
    similar_products = get_similar_products(hot_product)
    content = {
        "title": title,
        "links_menu": links_menu,
        "similar_products": similar_products,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
        "hot_product": hot_product,
    }
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "контакты"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)


@login_required
def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    title = product.name
    basket = get_basket(request.user)
    links_menu = ProductCategory.objects.all()
    content = {
        "title": title,
        "product": product,
        "links_menu": links_menu,
        "basket": basket,
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/product.html", content)
