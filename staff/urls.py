from django.urls import path
from .import views
app_name = "staff"

urlpatterns = [
    path('blog', views.AddBlog.as_view(), name="addBlog"),
    path('<int:id>/delete', views.deleteBlog, name="deleteBlog"),
    path('<pk>/update', views.UpdateBlog.as_view(), name="updateBlog"),
    path('category', views.AddCategory.as_view(), name="addCategory"),
    path('<int:id>/deleteCategory', views.deleteCategory, name="deleteCategory"),
    path('<pk>/updateCategory', views.UpdateCategory.as_view(), name="updateCategory"),
    path('Subcategory', views.AddSubCategory.as_view(), name="addSubCategory"),
    path('<int:id>/deleteSubCategory', views.deleteSubCategory, name="deleteSubCategory"),
    path('<pk>/updateSubCategory', views.UpdateSubCategory.as_view(), name="updateSubCategory"),
    path('<pk>/profile', views.Profile.as_view(), name="profile"),
    path('changePassword', views.changePassword, name = "changePassword"),
    path('logout', views.logOut, name="logout"),
    path('search', views.searchBlog, name = 'searchBlog'),
]