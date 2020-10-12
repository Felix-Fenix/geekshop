from django.conf import settings
from django.utils import timezone
from django.shortcuts import render

from .models import Product, ProductCategory, Contact

def main(request):
    title = 'главная'
    products = Product.objects.all()
    
    content = {'title': title, 'products': products, 'media_url':settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    similar_products = Product.objects.all()
    content = {
        'title': title, 
        'links_menu': links_menu,
        'similar_products': similar_products,
        'media_url': settings.MEDIA_URL,
        }
    if pk:
        print(f'Юзер выбрал категорию {pk}')
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = 'контакты'
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {'title': title, 'visit_date': visit_date, 'locations': locations}
    return render(request, "mainapp/contact.html", content)
