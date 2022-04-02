
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Product, Service,Client, Testomonial
from homepage.models import CompanyInformation
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# User Create and Update form
class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['email', 'password']:
            self.fields[fieldname].help_text = None
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'

    class Meta:
        model = User
        fields = ('first_name', 
                'last_name',
                'username',
                'email',
                'password',)
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'username':'Username',
            'email':'Email',
            'password':'Password'
        }
   

class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['email',]:
            self.fields[fieldname].help_text = None
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    class Meta:
      
        model = User

        fields = ('first_name', 
                'last_name',
                'username',
                'email',)
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'username':'Username',
            'email':'Email',
        }

# Create and Update Product
class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'

    class Meta:
        model = Product
        fields = ('name', 
                'description',
                'image',
                'link',
                )
        labels = {
            'name':'Name of the Product',
            'description':'Description of Product',
            'image':'Image for Product',
            'link':'Link',
        }
   

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Create and Update Service Model ------------------->
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class ServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'

    class Meta:
        model = Service
        fields = ('name', 
                'description',
                'image',

                )
        labels = {
            'name':'Name of the Service',
            'description':'Description of Service',
            'image':'Image for Service',
    
        }
        widgets = {
            'description':CKEditorUploadingWidget
        }
   

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Create and Update Client Model ------------------->
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'

    class Meta:
        model = Client
        fields = ('name', 
                'description',
                'image',
                'link'
     
                )
        labels = {
            'name':'Name of the Client',
            'description':'Description of Client',
            'image':'Image for Client',
            'link':'Link'
        }
        widgets = {
            'description':CKEditorUploadingWidget
        }
   
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Create and Update Testomonial Model ----------------->
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class TestomonialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestomonialForm, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'

    class Meta:
        model = Testomonial
        fields = ('name', 
                'description',
           
                )
        labels = {
            'name':'Name of the Product',
            'description':'Description of Product',
         
        }
   

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Create and Update CompanyInformation Model -------------------->
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class CompanyInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyInformationForm, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'

    class Meta:
        model = CompanyInformation
        fields = ('name', 
                'short',
                'aims',
                'logo',
                )
        labels = {
            'name':'Name',
            'short':'Short Description of Company',
            'logo':'Company Logo',
            'aims':'Aims',
        }
        widgets = {
            'logo':forms.FileInput(attrs={'required':False})
        }