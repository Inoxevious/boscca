from sacco.models import City
from django import forms
import datetime

class CityForm(forms.ModelForm):
    ## change the widget of the date field.
    # name = forms.DateField(
    #     label='City', 
    #     # change the range of the years from 1980 to currentYear - 5
    #     widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year-5))
    # )
    
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = City
        fields = 'country','name', 'official_language', 'state'