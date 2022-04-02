from django.urls import path
from .import views
app_name = "homepage"

urlpatterns = [
    path('', views.Homepage.as_view(), name="homepage" ),
    path('blog/<int:pk>', views.BlogV.as_view(), name="blogV"),
    path('login', views.LoginV, name = 'login'),
]