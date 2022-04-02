from django.urls import path
from .import views
app_name = "manager"

urlpatterns = [
    path('', views.Dashboard.as_view(), name="dashboard" ),
    path('adminList', views.AddAdmin.as_view(), name="addAdmin"),
    path('<int:id>/deleteAdmin', views.deleteAdmin, name="deleteAdmin"),
    path('<pk>/updateAdmin', views.UpdateAdmin.as_view(), name="updateAdmin"),
    path('product', views.AddProduct.as_view(), name="addProduct"),
    path('<int:id>/deleteproduct', views.deleteProduct, name="deleteProduct"),
    path('<pk>/updateproduct', views.UpdateProduct.as_view(), name="updateProduct"),
    # Url For Client------->
    # --------------------->
    path('client', views.AddClient.as_view(), name="addClient"),
    path('<int:id>/deleteClient', views.deleteClient, name="deleteClient"),
    path('<pk>/updateClient', views.UpdateClient.as_view(), name="updateClient"),

    # Url For Testomonial------->
    # --------------------->
    path('testomonial', views.AddTestomonial.as_view(), name="addTestomonial"),
    path('<int:id>/deleteTestomonial', views.deleteTestomonial, name="deleteTestomonial"),
    path('<pk>/updateTestomonial', views.UpdateTestomonial.as_view(), name="updateTestomonial"),
    # Url For Service------->
    # --------------------->
    path('Service', views.AddService.as_view(), name="addService"),
    path('<int:id>/deleteService', views.deleteService, name="deleteService"),
    path('<pk>/updateService', views.UpdateService.as_view(), name="updateService"),

    # Url for Profile
    path('setting', views.Company, name="company"),
   
]   