from django.contrib import admin
from .models import Product, Service, Client, Testomonial
# Register your models here.
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Testomonial)