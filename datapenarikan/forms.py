from django.forms import ModelForm, TextInput, Select
from .models import Datapenarikan  


class DatapenarikanForm(ModelForm):
    class Meta:
        model = Datapenarikan
        fields = '__all__'
        
        widgets = {
            #'' : Select(attrs={'class' : 'form-control'}),
            'norekening' : Select(attrs={'class' : 'form-control'}),
            'jumlah' : TextInput(attrs={'class' : 'form-control'}),
            'keterangan' : TextInput(attrs={'class' : 'form-control'}),
            
            
        } 
    def __init__(self, *args, **kwargs):
        super(DatapenarikanForm, self).__init__(*args, **kwargs)
        self.fields['keterangan'].required = False