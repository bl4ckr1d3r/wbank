from django.forms import ModelForm, TextInput, Select
from .models import Datasampah  


class DatasampahForm(ModelForm):
    class Meta:
        model = Datasampah
        fields = '__all__'
        
        widgets = {
            'jenissampah' : Select(attrs={'class' : 'form-control'}),
            'hargajual' : TextInput(attrs={'class' : 'form-control'}),
            'hargabeli' : TextInput(attrs={'class' : 'form-control'}),
            'margin' : TextInput(attrs={'class' : 'form-control', 'class' : 'd-none'}),
        } 
    def __init__(self, *args, **kwargs):
        super(DatasampahForm, self).__init__(*args, **kwargs)
        self.fields['margin'].required = False