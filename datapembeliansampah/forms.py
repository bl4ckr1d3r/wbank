from django.forms import ModelForm, TextInput, Select
from .models import Datapembeliansampah  


class DatapembeliansampahForm(ModelForm):
    class Meta:
        model = Datapembeliansampah
        fields = '__all__'
        
        widgets = {
            #'' : Select(attrs={'class' : 'form-control'}),
            'kdpembeliansampah' : TextInput(attrs={'class' : 'form-control'}),
            'norekening' : Select(attrs={'class' : 'form-control'}),
            'jenissampah' : Select(attrs={'class' : 'form-control'}),
            'berat' : TextInput(attrs={'class' : 'form-control'}),
            'jumlah' : TextInput(attrs={'class' : 'form-control', 'class' : 'd-none'}),
            
        } 
    def __init__(self, *args, **kwargs):
        super(DatapembeliansampahForm, self).__init__(*args, **kwargs)
        self.fields['jumlah'].required = False