
from django.shortcuts import render
from django.views.generic import View, UpdateView
from .models import Product, Service, Client, Testomonial
from homepage.models import CompanyInformation
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from staff.models import Blog
from django.contrib.auth.models import User
from .models import Product, Client, Service, Testomonial
from .forms import UserCreateForm, UserUpdateForm, ProductForm, ServiceForm, ClientForm, TestomonialForm, CompanyInformationForm
# Create your views here.


class Dashboard(View):
    template_name = "manager/dashboard.html"
    def get(self, request, *args, **kwargs, ):
        blog = Blog.objects.all()[:4]

        dist = {
            'blog':blog,
        }
        blog_count = Blog.objects.all().count()
        staff_count = User.objects.all().count()
        client_count = Client.objects.all().count()
        product_count = Product.objects.all().count()
        service_count = Service.objects.all().count()
        testo_count = Testomonial.objects.all().count()

        public = {
            'blog_count':blog_count,
            'staff':staff_count,
            'client_count':client_count,
            'product':product_count,
            'service':service_count,
            'testo_count':testo_count
        }

        dist.update(public)
        
        return render(request, self.template_name, dist)

# ADMIN CRUD
class AddAdmin(View):
    template_name = "staff/addAdmin.html"

    def get(self, request, *args, **kwargs ):
        form = UserCreateForm()
        blog = User.objects.all().order_by('-id')
        dist = {
            'form':form,
            'blog':blog,
            'button':'Add Admin',
        }
        blog_count = Blog.objects.all().count()
        staff_count = User.objects.all().count()
        client_count = Client.objects.all().count()
        product_count = Product.objects.all().count()
        service_count = Service.objects.all().count()
        testo_count = Testomonial.objects.all().count()

        public = {
            'blog_count':blog_count,
            'staff':staff_count,
            'client_count':client_count,
            'product':product_count,
            'service':service_count,
            'testo_count':testo_count
        }
        dist.update(public)

        return render(request, self.template_name, dist)
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added Admin")
            return HttpResponseRedirect(reverse('manager:addAdmin'))
        else:
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('manager:addAdmin'))
  
class UpdateAdmin(SuccessMessageMixin, UpdateView):
    template_name = "staff/editAdmin.html"
    model = User
    form_class = UserUpdateForm
    success_message = "Successfully Updated Admin"
    
    def get_success_url(self, *args, **kwargs):
        id = self.kwargs['pk']
        return reverse('manager:updateAdmin', args=[id])
def deleteAdmin(request, id):
    blog = User.objects.get(id = id)
    blog.delete()
    messages.success(request, "Succesfully Deleted Admin")
    return HttpResponseRedirect(reverse('manager:addAdmin')) 

# -----------CRUD PRODUCT----------------------->
# Product CRUD
class AddProduct(View):
    template_name = "manager/addProduct.html"

    def get(self, request, *args, **kwargs ):
        form = ProductForm()
        blog = Product.objects.all().order_by('-id')
        dist = {
            'form':form,
            'blog':blog,
            'button':'Add Product',
        }
        blog_count = Blog.objects.all().count()
        staff_count = User.objects.all().count()
        client_count = Client.objects.all().count()
        product_count = Product.objects.all().count()
        service_count = Service.objects.all().count()
        testo_count = Testomonial.objects.all().count()

        public = {
            'blog_count':blog_count,
            'staff':staff_count,
            'client_count':client_count,
            'product':product_count,
            'service':service_count,
            'testo_count':testo_count
        }
        dist.update(public)

        return render(request, self.template_name, dist)
    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added Product")
            return HttpResponseRedirect(reverse('manager:addProduct'))
        else:
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('manager:addProduct'))
  

class UpdateProduct(SuccessMessageMixin, UpdateView):
    template_name = "manager/editProduct.html"
    model = Product
    form_class = ProductForm
    success_message = "Successfully Updated Product"
    
    def get_success_url(self, *args, **kwargs):
        id = self.kwargs['pk']
        return reverse('manager:updateProduct', args=[id])
def deleteProduct(request, id):
    blog = Product.objects.get(id = id)
    blog.delete()
    messages.success(request, "Succesfully Deleted Product")
    return HttpResponseRedirect(reverse('manager:addProduct')) 

# -------------------------------------------->
# CRUD Service -------------------------------->
# -------------------------------------------->
class AddService(View):
    template_name = "manager/service/addService.html"

    def get(self, request, *args, **kwargs ):
        form = ServiceForm()
        blog = Service.objects.all().order_by('-id')
        dist = {
            'form':form,
            'blog':blog,
            'button':'Add Service',
        }
        blog_count = Blog.objects.all().count()
        staff_count = User.objects.all().count()
        client_count = Client.objects.all().count()
        product_count = Product.objects.all().count()
        service_count = Service.objects.all().count()
        testo_count = Testomonial.objects.all().count()

        public = {
            'blog_count':blog_count,
            'staff':staff_count,
            'client_count':client_count,
            'product':product_count,
            'service':service_count,
            'testo_count':testo_count
        }
        dist.update(public)

        return render(request, self.template_name, dist)
    def post(self, request, *args, **kwargs):
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added Service")
            return HttpResponseRedirect(reverse('manager:addService'))
        else:
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('manager:addService'))
  

class UpdateService(SuccessMessageMixin, UpdateView):
    template_name = "manager/service/editService.html"
    model = Service
    form_class = ServiceForm
    success_message = "Successfully Updated Service"
    
    def get_success_url(self, *args, **kwargs):
        id = self.kwargs['pk']
        return reverse('manager:updateService', args=[id])
def deleteService(request, id):
    blog = Service.objects.get(id = id)
    blog.delete()
    messages.success(request, "Succesfully Deleted Service")
    return HttpResponseRedirect(reverse('manager:addService')) 







# -------------------------------------------->
# CRUD Client -------------------------------->
# -------------------------------------------->
class AddClient(View):
    template_name = "manager/client/addClient.html"

    def get(self, request, *args, **kwargs ):
        form = ClientForm()
        blog = Client.objects.all().order_by('-id')
        dist = {
            'form':form,
            'blog':blog,
            'button':'Add Client',
        }
        blog_count = Blog.objects.all().count()
        staff_count = User.objects.all().count()
        client_count = Client.objects.all().count()
        product_count = Product.objects.all().count()
        service_count = Service.objects.all().count()
        testo_count = Testomonial.objects.all().count()

        public = {
            'blog_count':blog_count,
            'staff':staff_count,
            'client_count':client_count,
            'product':product_count,
            'service':service_count,
            'testo_count':testo_count
        }
        dist.update(public)

        return render(request, self.template_name, dist)
    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added Client")
            return HttpResponseRedirect(reverse('manager:addClient'))
        else:
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('manager:addClient'))
  

class UpdateClient(SuccessMessageMixin, UpdateView):
    template_name = "manager/client/editClient.html"
    model = Client
    form_class = ClientForm
    success_message = "Successfully Updated Client"
    
    def get_success_url(self, *args, **kwargs):
        id = self.kwargs['pk']
        return reverse('manager:updateClient', args=[id])
def deleteClient(request, id):
    blog = Client.objects.get(id = id)
    blog.delete()
    messages.success(request, "Succesfully Deleted Client")
    return HttpResponseRedirect(reverse('manager:addClient')) 






# -------------------------------------------->
# CRUD Testomonial -------------------------------->
# -------------------------------------------->

class AddTestomonial(View):
    template_name = "manager/testomonial/addTestomonial.html"

    def get(self, request, *args, **kwargs ):
        form = TestomonialForm()
        blog = Testomonial.objects.all().order_by('-id')
        dist = {
            'form':form,
            'blog':blog,
            'button':'Add Testomonial',
        }
        blog_count = Blog.objects.all().count()
        staff_count = User.objects.all().count()
        client_count = Client.objects.all().count()
        product_count = Product.objects.all().count()
        service_count = Service.objects.all().count()
        testo_count = Testomonial.objects.all().count()

        public = {
            'blog_count':blog_count,
            'staff':staff_count,
            'client_count':client_count,
            'product':product_count,
            'service':service_count,
            'testo_count':testo_count
        }
        dist.update(public)
        return render(request, self.template_name, dist)
    def post(self, request, *args, **kwargs):
        form = TestomonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added Testomonial")
            return HttpResponseRedirect(reverse('manager:addTestomonial'))
        else:
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('manager:addTestomonial'))
  

class UpdateTestomonial(SuccessMessageMixin, UpdateView):
    template_name = "manager/testomonial/editTestomonial.html"
    model = Testomonial
    form_class = TestomonialForm
    success_message = "Successfully Updated Testomonial"
    
    def get_success_url(self, *args, **kwargs):
        id = self.kwargs['pk']
        return reverse('manager:updateTestomonial', args=[id])
def deleteTestomonial(request, id):
    blog = Testomonial.objects.get(id = id)
    blog.delete()
    messages.success(request, "Succesfully Deleted Testomonial")
    return HttpResponseRedirect(reverse('manager:addTestomonial')) 


# Company Information:

def Company(request):
    sett = CompanyInformation.objects.all()
    form = CompanyInformationForm()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
        form.fields['name'].initial = setting.name
        form.fields['short'].initial = setting.short
        form.fields['aims'].initial = setting.aims

    dist = {
        'setting':setting,
        'form':form
    }
    blog_count = Blog.objects.all().count()
    staff_count = User.objects.all().count()
    client_count = Client.objects.all().count()
    product_count = Product.objects.all().count()
    service_count = Service.objects.all().count()
    testo_count = Testomonial.objects.all().count()

    public = {
        'blog_count':blog_count,
        'staff':staff_count,
        'client_count':client_count,
        'product':product_count,
        'service':service_count,
        'testo_count':testo_count
    }
    dist.update(public)
    if request.method == 'POST':
        form = CompanyInformationForm(request.POST, request.FILES)
        if form.is_valid():
            
            if sett:
                setting.name = request.POST['name']
                setting.short = request.POST['short']
                setting.aims = request.POST['aims']
                try:
                    setting.logo = request.FILES['logo']
                except:
                    pass
                setting.save()
            else:
                form.save()
            messages.success(request, "Successfully Updated Settings")
            return HttpResponseRedirect(reverse("manager:company"))
    else:
        return render(request, "staff/other/setting.html", dist)