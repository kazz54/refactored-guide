from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
from .models import User
#from PIL import Image
#from django.core.files import File



#class HorizRadioRenderer(forms.RadioSelect.renderer):
#    """ this overrides widget method to put radio buttons horizontally
#        instead of vertically.
#    """
#    def render(self):
#            """Outputs radios"""
#            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


from django.utils.safestring import mark_safe

#class HorizontalRadioRenderer(forms.RadioSelect.renderer):
#  def render(self):
#    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))





class RegistrationForm(forms.ModelForm):
    institution_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Institution Name',
                                                               'class': 'form-control',
                                                               }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))                                                           
    password1 = forms.CharField(max_length=50,
                                required=True,
                                label="Password",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                label="Confirm Password",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
                                                                  
                                                                  
#    is_mvp = forms.CharField(label="Are you a US Citizen?",
#                                 widget=forms.RadioSelect(attrs=HorizRadioRenderer,
#                                 widget=forms.RadioSelect(attrs={'id': 'value'}))
#                                 widget=
#                                 choices=(('yes','YES'),('no','NO'))), required=True)  
                                                                                             
#    is_mvp = forms.ChoiceField(choices=APPROVAL_CHOICES,
#                 initial=0,
#                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
#                                 )
#    is_mvp = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'star'}), choices=(('False', 'x'), ('True', 'y'),))
    class Meta:
        model = User
        fields = ('institution_name', 'email', 'password1', 'password2', 'quetion', 'is_svp', 'is_spo', 'is_rev', 'qtwo', 'is_mvp', 'is_dpn')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
        
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('institution_name','email', 'password', 'is_staff', 'is_superuser', 'is_mvp')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ('institution_name', 'email', 'password', 'is_active', 'is_superuser', 'is_mvp')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
        
        


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-2 mb-0'),
                Column('title', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('phone_number', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
#            'title',
#            'address_2',
            Row(
                Column('institution_name', css_class='form-group col-md-2 mb-0'),
                Column('section', css_class='form-group col-md-4 mb-0'),
                Column('region', css_class='form-group col-md-4 mb-0'),
                Column('institution_address', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            
            'sector_your_instution_belongs',
            'other_institution_belong',
            'category_of_institution',
            'mandate_of_institution',
            'other_mandate_of_institution',
#            Column('', css_class='form-group col-md-6 mb-0'),
            Submit('submit', 'Proceed')
        )
    class Meta:
        model = User
        
        
        
        fields = ('institution_name', 'name', 'title', 'email', 'phone_number', 'institution_address', 'section', 'region', 'sector_your_instution_belongs', 'other_institution_belong', 'category_of_institution', 'mandate_of_institution', 'other_mandate_of_institution')
        
        

       





#class ProfileForm(forms.ModelForm):
#
#    class Meta:
#        model = Profile
#        fields = ('country_of_rigin', 'country', 'physical_address_while_in_tanzania')        
        
#class UpdateProfileForm(forms.ModelForm):
#    passportimg = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
#    other_names = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
#
#    class Meta:
#        model = User
#        fields = ['passportimg', 'other_names']






#class PhotoForm(forms.ModelForm):
#    x = forms.FloatField(widget=forms.HiddenInput())
#    y = forms.FloatField(widget=forms.HiddenInput())
#    width = forms.FloatField(widget=forms.HiddenInput())
#    height = forms.FloatField(widget=forms.HiddenInput())
#
#    class Meta:
#        model = User
#        fields = ('passportimg', 'x', 'y', 'width', 'height', )
#        widgets = {
#            'passportimg': forms.FileInput(attrs={
#                'accept': 'image/*'  # this is not an actual validation! don't rely on that!
#            })
#        }
#
#    def save(self):
#        user = super(PhotoForm, self).save()
#
#        x = self.cleaned_data.get('x')
#        y = self.cleaned_data.get('y')
#        w = self.cleaned_data.get('width')
#        h = self.cleaned_data.get('height')
#
#        image = Image.open(user.passportimg)
#        cropped_image = image.crop((x, y, w+x, h+y))
#        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
#        resized_image.save(user.passportimg.path)
#
#        return user



        
           
    
                 


#STATES = (
#    ('', 'Choose...'),
#    ('MG', 'Minas Gerais'),
#    ('SP', 'Sao Paulo'),
#    ('RJ', 'Rio de Janeiro')
#)

#class AddressForm(forms.Form):
#    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
#    password = forms.CharField(widget=forms.PasswordInput())
#    address_1 = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
#    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
#    city = forms.CharField()
#    state = forms.ChoiceField(choices=STATES)
#    zip_code = forms.CharField(label='Zip')
#    check_me_out = forms.BooleanField(required=False)


#class CrispyAddressForm(AddressForm):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.helper = FormHelper()
#        self.helper.layout = Layout(
#            Row(
#                Column('email', css_class='form-group col-md-6 mb-0'),
#                Column('password', css_class='form-group col-md-6 mb-0'),
#                css_class='form-row'
#            ),
#            'address_1',
#            'address_2',
#            Row(
#                Column('city', css_class='form-group col-md-6 mb-0'),
#                Column('state', css_class='form-group col-md-4 mb-0'),
#                Column('zip_code', css_class='form-group col-md-2 mb-0'),
#                css_class='form-row'
#            ),
#            'check_me_out',
#            Submit('submit', 'Sign in')
#        )


#class CustomCheckbox(Field):
#    template = 'custom_checkbox.html'
        