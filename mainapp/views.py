import datetime
from django.shortcuts import render


def main(request):
    title = 'главная'
    products = [
        {
            'name': 'Отличная лампа',
            'desc': 'Осветит весь ваш дом.',
            'image_src': 'product-1.jpg',
            'image_href': '/product/1/',
            'alt': 'Продукт 1',
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'image_src': 'product-2.jpg',
            'image_href': '/product/2/',
            'alt': 'Продукт 1',
        },
    ]
    content = {'title': title, 'products': products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = 'продукты'
    content = {'title': title}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = 'контакты'
    content = {'title': title}
    return render(request, "mainapp/contact.html", content)