from django.forms import ModelForm, TextInput
from .models import Datanasabah  


class DatanasabahForm(ModelForm):
    class Meta:
        model = Datanasabah
        fields = '__all__'
        widgets = {
            'nama' : TextInput(attrs={'class' : 'form-control'}),
            'alamat' : TextInput(attrs={'class' : 'form-control'}),
            'nohp' : TextInput(attrs={'class' : 'form-control'}),
            'jumlahanggota' : TextInput(attrs={'class' : 'form-control'}),
        } 
