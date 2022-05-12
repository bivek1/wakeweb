from django.urls import path
from .import views
app_name = "homepage"

urlpatterns = [
    path('', views.Homepage.as_view(), name="homepage" ),
    path('blog/<int:id>', views.BlogV, name="blogV"),
    path('service', views.ServiceView.as_view(), name = "service"),
    path('serviceDetails/<int:id>', views.ServiceDetail, name="serviceDetails"),
    path('product', views.AllProduct.as_view(), name = "product"),
    path('productsDetails/<int:id>', views.productDetail, name="productDetails"),
    path('contactus', views.Contactus.as_view(), name="contact"),
    path('blogs', views.ShowingBlog.as_view(), name ="ShowingBlog"),
    path('login', views.LoginV, name = 'login'),
]