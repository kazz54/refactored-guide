from django import forms
from .models import TechRev
#from django.forms.widgets import DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field





#class TechForm(forms.ModelForm):
#    first_name= forms.CharField(max_length=100)
#    last_name= forms.CharField(max_length=100)
#    email= forms.EmailField()
#    age= forms.IntegerField()
#    favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
#     = Choices('', '', '', '')
#    Category_of_technologies = forms.CharField(label='Which categories of technologies does your institution use?', widget=forms.RadioSelect(choices=CATEGORY_OF_TECHNOLOGIES))
#    other_category_of_tech = forms.CharField(max_length=500)
class TechForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
#            Row(
#                Column('email', css_class='form-group col-md-6 mb-0'),
#                Column('password', css_class='form-group col-md-6 mb-0'),
#                css_class='form-row'
#            ),
#            'ethical_considerations',
#            'address_2',
            Row(
                Column('category_of_technologies', css_class='form-group col-md-6 mb-0'),
#                Column('expiration_date', css_class='form-group col-md-4 mb-0'),
#                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
#            'ethical_cert',
#        
#            Submit('submit', 'Submit',css_id = 'desired_id')
        )
    class Meta:
        model = TechRev
        
        
        
        fields = ('category_of_technologies',)
        
#        widgets = {
#            'expiration_date': DateInput(attrs={'type': 'date'})
            
#        } 

       



    











from django import forms








    