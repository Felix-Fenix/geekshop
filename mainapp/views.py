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
            'alt': 'Продукт 2',
        },
    ]
    content = {'title': title, 'products': products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = 'продукты'
    links_menu = [
        {'href' : 'product_all', 'name': 'всё'},
        {'href' : 'product_home', 'name': 'дом'},
        {'href' : 'product_office', 'name': 'офис'},
        {'href' : 'product_modern', 'name': 'модерн'},
        {'href' : 'product_classic', 'name': 'классика'},
    ]
    similar_products = [
                {
            'name': 'Отличная лампа',
            'desc': 'Осветит весь ваш дом.',
            'image_src': 'product-11.jpg',
            'image_href': '/product/11/',
            'alt': 'Продукт 1',
        },
                {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'image_src': 'product-21.jpg',
            'image_href': '/product/21/',
            'alt': 'Продукт 2',
        },
                {
            'name': 'Лампа премиального качества',
            'desc': 'Произведение искусства, а не лампа.',
            'image_src': 'product-31.jpg',
            'image_href': '/product/31/',
            'alt': 'Продукт 3',
        },
    ]
    content = {'title': title, 'links_menu': links_menu, 'similar_products': similar_products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = 'контакты'
    visit_date = datetime.datetime.now()
    locations = [
        {'city': 'Москва', 'phone': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'},
        {'city': 'Ростов-на-Дону', 'phone': '+7-999-999-9999', 'email': 'valera@mail.ru', 'address': 'За городом'},
        {'city': 'Челябинск', 'phone': '+7-777-777-7777', 'email': 'atom@rambler.ru', 'address': 'В городе'},
        
    ]
    content = {'title': title, 'visit_date': visit_date, 'locations': locations}
    return render(request, "mainapp/contact.html", content)