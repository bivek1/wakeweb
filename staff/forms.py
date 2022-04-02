from django import forms
from .models import Blog, SubCategory, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category','sub_category','description')

        labels = {
            'title':'Title of Blog*',
            'category':'Select Category*',
            'sub_category':'Select Sub Category',
            'description':'Description'
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Your Title'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'sub_category':forms.Select(attrs={'class':'form-control mb-2'}),
            'description':CKEditorUploadingWidget
        }


# Category Form

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        labels = {
            'name':'Name of Category*',
          
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category Name'}),
        }

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ('name','category')

        labels = {
            'name':'Name of SubCategory*',
            'category':'Category'
            
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category Name'}),
            'category':forms.Select(attrs={'class':'form-control mb-2'}),
        }


from django.contrib.auth.forms import PasswordChangeForm

class FormChangePassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(FormChangePassword, self).__init__(*args, **kwargs)
        for field in ('old_password', 'new_password1', 'new_password2'):
            self.fields['old_password'].widget.attrs = {'class':'form-control ps-0 form-control-line', 'placeholder':"Old Password"}
            self.fields['new_password1'].widget.attrs = {'class':'form-control ps-0 form-control-line', 'placeholder':"New Password"}
            self.fields['new_password2'].widget.attrs = {'class':'form-control ps-0 form-control-line', 'placeholder':"Re New Password"}