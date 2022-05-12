from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, update_session_auth_hash
from django.urls import reverse
from django.views.generic import View, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from manager.models import Client, Product, Service, Testomonial
from .forms import BlogForm, CategoryForm, FormChangePassword, SubCategoryForm
from .models import Blog, SubCategory, Category
from django.contrib import messages
from manager.forms import UserUpdateForm
from homepage.models import CompanyInformation
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.




# CRUD BLOG
class AddBlog(View):
    template_name = "staff/addBlog.html"

    def get(self, request, *args, **kwargs ):
        form = BlogForm()
        blog = Blog.objects.all().order_by('-id')

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
            'testo_count':testo_count,
            'company' : CompanyInformation.objects.get(id = 1)
        }
        dist = {
            'form':form,
            'blog':blog,
            'button':'Add Blog',
        }
        dist.update(public)

        return render(request, self.template_name, dist)
    def post(self, request, *args, **kwargs):
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added Blog")
            return HttpResponseRedirect(reverse('staff:addBlog'))
        else:
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('staff:addBlog'))


class UpdateBlog(SuccessMessageMixin,UpdateView):
    template_name = "staff/editBlog.html"
    model = Blog
    form_class = BlogForm
    success_message = "Successfully Updated Blog"
    
    def get_success_url(self, *args, **kwargs):
        id = self.kwargs['pk']
        return reverse('staff:updateBlog', args=[id])
def deleteBlog(request, id):
    blog = Blog.objects.get(id = id)
    blog.delete()
    messages.success(request, "Succesfully Deleted Blog")
    return HttpResponseRedirect(reverse('staff:addBlog')) 


# CATEGORY CRUD
class AddCategory(View):
    template_name = "staff/addCategory.html"

    def get(self, request, *args, **kwargs ):
        form = CategoryForm()
        blog = Category.objects.all().order_by('-id')
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
            'testo_count':testo_count,
            'company' : CompanyInformation.objects.get(id = 1)
        }
        dist = {
            'form':form,
            'blog':blog,
            'button':'Add Category',
        }
        dist.update(public)
        return render(request, self.template_name, dist)
    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added Category")
            return HttpResponseRedirect(reverse('staff:addCategory'))
        else:
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('staff:addCategory'))
  

class UpdateCategory(SuccessMessageMixin, UpdateView):
    template_name = "staff/editCategory.html"
    model = Category
    form_class = CategoryForm
    success_message = "Successfully Updated Category"
    
    def get_success_url(self, *args, **kwargs):
        id = self.kwargs['pk']
        return reverse('staff:updateCategory', args=[id])
def deleteCategory(request, id):
    blog = Category.objects.get(id = id)
    blog.delete()
    messages.success(request, "Succesfully Deleted Category")
    return HttpResponseRedirect(reverse('staff:addCategory')) 

#############################
# Sub CATEGORY CRUD
class AddSubCategory(View):
    template_name = "staff/addSubCategory.html"

    def get(self, request, *args, **kwargs ):
        form = SubCategoryForm()
        blog = SubCategory.objects.all().order_by('-id')
        dist = {
            'form':form,
            'blog':blog,
            'button':'Add Sub Category',
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
            'testo_count':testo_count,
            'company' : CompanyInformation.objects.get(id = 1)
        }
        dist.update(public)
        return render(request, self.template_name, dist)
    def post(self, request, *args, **kwargs):
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added Sub Category")
            return HttpResponseRedirect(reverse('staff:addSubCategory'))
        else:
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('staff:addSubCategory'))
  

class UpdateSubCategory(SuccessMessageMixin, UpdateView):
    template_name = "staff/editSubCategory.html"
    model = SubCategory
    form_class = SubCategoryForm
    success_message = "Successfully Updated Sub Category"
    
    def get_success_url(self, *args, **kwargs):
        id = self.kwargs['pk']
        return reverse('staff:updateSubCategory', args=[id])
def deleteSubCategory(request, id):
    blog = SubCategory.objects.get(id = id)
    blog.delete()
    messages.success(request, "Succesfully Deleted Sub Category")
    return HttpResponseRedirect(reverse('staff:addSubCategory')) 


# Profle Crud>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Profile(UpdateView, SuccessMessageMixin):
    template_name = "staff/other/profile.html"
    model = User
    form_class = UserUpdateForm
    success_message = "Successfully Updated Profile"
    
    def get_success_url(self, *args, **kwargs):
        id = self.kwargs['pk']
        return reverse('manager:updateAdmin', args=[id])

# ------------------------------------------->
# ------------------------------------------->
# Password Change      ---------------------->
# ------------------------------------------->
# -------------------------------------------->
def changePassword(request):
    if request.method == 'POST':
        form = FormChangePassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('manager:changePassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = FormChangePassword(request.user)
    dist = {
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
        'testo_count':testo_count,
        'company' : CompanyInformation.objects.get(id = 1)
    }
    dist.update(public)
    return render(request, 'staff/changePassword.html',dist )

# ------------------------------------>
# Logout------------------------------>
# ------------------------------------>
def logOut(request):
    logout(request)
    return redirect('/')

# ------------------------------------->
# Search Blog-------------------------->
# ------------------------------------->

def searchBlog(request):
    name = request.GET['blogS']
    blog = Blog.objects.filter(title__icontains = name)
    dist = {
        'blog':blog
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
        'testo_count':testo_count,
        'company' : CompanyInformation.objects.get(id = 1)
    }
    dist.update(public)
    return render(request, "staff/searchBlog.html", dist)