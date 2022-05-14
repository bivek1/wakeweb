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
    path('team', views.Team.as_view(), name ="team"),
    path('terms-and-condition', views.Term.as_view(), name ="term"),
    path('Ceo-Message', views.Ceo.as_view(), name ="ceo"),
    path('privacy-and-policy', views.Privacy.as_view(), name ="privacy"),
    path('verifyfirst', views.postwork, name = "work"),
    path('postyourwork/<int:id>', views.PostNow, name = "post"),
    path('login', views.LoginV, name = 'login'),
]