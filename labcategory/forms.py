from .models import Labcategory
from django import forms
import datetime

class LabcategoryForm(forms.ModelForm):
    ## change the widget of the date field.
#    dob = forms.DateField(
#        label='What is your birth date?', 
        # change the range of the years from 1980 to currentYear - 5
#        widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year-5))
#    )
    
    def __init__(self, *args, **kwargs):
        super(LabcategoryForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Labcategory
        fields = ('spous', 'nick_name', 'name', 'hardware', 'software', 'licensed', 'both', 'open_souce', 'developed', 'capacity', 'status') 
        
