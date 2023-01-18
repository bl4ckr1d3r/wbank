from django.forms import ModelForm, TextInput, Select
from .models import Databukutabungan  


class DatabukutabunganForm(ModelForm):
    class Meta:
        model = Databukutabungan
        fields = '__all__'
        
        widgets = {
            'nama' : Select(attrs={'class' : 'form-control'}),
            'noidentitas' : TextInput(attrs={'class' : 'form-control'}),
            'norekening' : TextInput(attrs={'class' : 'form-control'}),
            'cabang' : TextInput(attrs={'class' : 'form-control'}),
            'saldonominal' : TextInput(attrs={'class' : 'form-control'}),
            'saldoemas' : TextInput(attrs={'class' : 'form-control'}),
        } 
    def __init__(self, *args, **kwargs):
        super(DatabukutabunganForm, self).__init__(*args, **kwargs)
        self.fields['saldonominal'].required = False
        self.fields['saldoemas'].required = False