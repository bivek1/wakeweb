from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from staff.models import Category
from manager.models import Product, Service, Testomonial
from staff.models import Blog
from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login
from .models import CompanyInformation
# Create your views here.
class Homepage(TemplateView):
    com = CompanyInformation.objects.all()
    cm = None
    for i in com:
        cm = i
        break

    template_name = 'homepage/index.html'
    def get(self, request, *args, **kwargs):
        dist = {
            'company':self.cm,
            'product':Product.objects.all()[:6],
            'service':Service.objects.all()[:3],
            'testo':Testomonial.objects.all()[:5]
        }
        return render(request, self.template_name, dist)

def BlogV(request, id):
   
    template_name = "homepage/blogV.html"
    blog = Blog.objects.get(id = id)
    dist = {
        'blog':blog,
        'related':Blog.objects.filter(category=blog.category)
    }
    return render(request, template_name, dist)


def LoginV(request):
    com = CompanyInformation.objects.all()
    cm = None
    for i in com:
        cm = i
        break
    dist = {
            'company':cm,
            'blog':Blog.objects.all()
    }
    tempate_name = 'homepage/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        use = authenticate(request, username = username, password = password)
        if use is not None:
            login(request, use)
            return HttpResponseRedirect(reverse('manager:dashboard'))
        else:
            messages.error(request, "Incorrect Username and Password")
            return render(request, tempate_name, dist)
    else:
        return render(request, tempate_name,dist)

# Showing Service
class ServiceView(TemplateView):
    com = CompanyInformation.objects.all()
    cm = None
    for i in com:
        cm = i
        break

    template_name = 'homepage/service.html'
    def get(self, request, *args, **kwargs):
        dist = {
            'company':self.cm,
            'service':Service.objects.all()
        }
        return render(request, self.template_name, dist)

def ServiceDetail(request, id):
    service = Service.objects.get(id = id)
    dist = {
        'service':service
    }
    return render(request, 'homepage/per_service.html', dist)


# Showing Service
class AllProduct(TemplateView):
    com = CompanyInformation.objects.all()
    cm = None
    for i in com:
        cm = i
        break

    template_name = 'homepage/allProduct.html'
    def get(self, request, *args, **kwargs):
        dist = {
            'company':self.cm,
            'product':Product.objects.all()
        }
        return render(request, self.template_name, dist)


class Contactus(TemplateView):
   
    template_name = 'homepage/contact.html'


def productDetail(request, id):
    service = Product.objects.get(id = id)
    dist = {
        'product':service
    }
    return render(request, 'homepage/per_product.html', dist)


# Showing Service
class ShowingBlog(TemplateView):
  
    template_name = 'homepage/blog.html'
    def get(self, request, *args, **kwargs):
        dist = {
         
            'blog':Blog.objects.all(),
            'category':Category.objects.all()[:3]
        }
        return render(request, self.template_name, dist)


class Team(TemplateView):
    template_name = 'homepage/team.html'


class Ceo(TemplateView):
    template_name = 'homepage/ceo.html'

class Privacy(TemplateView):
    template_name = 'homepage/privacy.html'

class Term(TemplateView):
    template_name = 'homepage/ceo.html'