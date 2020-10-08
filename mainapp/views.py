from django.conf import settings
from django.utils import timezone
from django.shortcuts import render

from .models import Product, ProductCategory

def main(request):
    title = 'главная'
    products = Product.objects.all()
    
    content = {'title': title, 'products': products, 'media_url':settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    similar_products = Product.objects.all()
    content = {
        'title': title, 
        'links_menu': links_menu,
        'similar_products': similar_products,
        'media_url': settings.MEDIA_URL,
        }
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = 'контакты'
    visit_date = timezone.now()
    locations = [
        {'city': 'Москва', 'phone': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'},
        {'city': 'Ростов-на-Дону', 'phone': '+7-999-999-9999', 'email': 'valera@mail.ru', 'address': 'За городом'},
        {'city': 'Челябинск', 'phone': '+7-777-777-7777', 'email': 'atom@rambler.ru', 'address': 'В городе'},
        
    ]
    content = {'title': title, 'visit_date': visit_date, 'locations': locations}
    return render(request, "mainapp/contact.html", content)
