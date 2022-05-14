from django.contrib import admin
from .models import CompanyInformation, Worker, Proff
# Register your models here.
admin.site.register(CompanyInformation)
admin.site.register(Proff)
admin.site.register(Worker)