from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns =[
    path("admin/", admin.site.urls),
    path("", mainapp.main, name = 'main'),
    path("products/", mainapp.products, name='products'),
    path("products/all", mainapp.products, name='product_all'),
    path("products/home", mainapp.products, name='product_home'),
    path("products/office", mainapp.products, name='product_office'),
    path("products/modern", mainapp.products, name='product_modern'),
    path("products/classic", mainapp.products, name='product_classic'),
    path("contact/", mainapp.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
