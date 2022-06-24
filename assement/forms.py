from django import forms
from django.conf import settings
#from django.forms.widgets import DateInput
from .models import Assesment


    
    



#class ApplicationForm(forms.ModelForm):
    #research_title = forms.CharField(required=True)
    #research_introduction = forms.CharField(required=True)
    #research_broad_objectives = forms.CharField(required=True)
    #research_specific_objectives = forms.CharField(required=True)
    #purpose_of_research = forms.ChoiceField(required=True)
#    research_start_date = forms.DateField(required=True)
#    location_of_Study = forms.CharField(required=True)
#    class Meta:
#        model = Assesment
#        
#        fields = ('sector_your_instution_belongs', 'category_of_institution', 'mandate_of_institution', 'Category_of_technologies') 
#        widgets = {'location_typed': forms.HiddenInput()}
#        forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}))
#        widgets = {
#           'research_start_date': DateInput(attrs={'type': 'date'})                       
 #       }
 #       widgets = {
 #          'research_end_date': DateInput(attrs={'type': 'date'})                       
#        }
#        self.fields['research_end_date'].widget.attrs.update(
#            {
#                'placeholder': 'YYYY-MM-DD ',
#            }
#        )         
#    research_start_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
#    research_end_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        
#       forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}))
        

     
    
    
#class ProductForm(ModelForm):
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Assesment
        fields = ('sector_your_instution_belongs', 'other_institution_belong', 'category_of_institution', 'mandate_of_institution', 'other_mandate_of_institution', 'Category_of_technologies', 'other_category_of_tech') 

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['other_institution_belong'].widget.attrs\
            .update({
                'id': 'myCustomId',
                'placeholder': 'Name',
                'class': 'input-calss_name'
            })
            
            
#    def __init__(self, *args, **kwargs):
#        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['other_mandate_of_institution'].widget.attrs\
            .update({
                'id': 'myCustomIdone',
                'placeholder': 'Name',
                'class': 'input-calss_name'
            })        
            
            
            
        self.fields['other_category_of_tech'].widget.attrs\
            .update({
                'id': 'myCustomIdtwo',
                'placeholder': 'Name',
                'class': 'input-calss_name'
            })            