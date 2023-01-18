from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from databukutabungan.models import Databukutabungan
from datanasabah.models import Datanasabah
from datapembeliansampah.models import Datapembeliansampah
from datapenarikan.models import Datapenarikan
from datasampah.models import Datasampah

# Create your views here.
@login_required(login_url='login')
def index(request):
    databukutabungan = Databukutabungan.objects.all().count()
    datanasabah = Datanasabah.objects.all().count()
    datapembeliansampah = Datapembeliansampah.objects.all().count()
    datapenarikan = Datapenarikan.objects.all().count()
    datasampah = Datasampah.objects.all().count()
    context = {
       
       'title' : 'Dashboard | Bank Sampah We SAVE',
       'databukutabungan': databukutabungan,
       'datanasabah' : datanasabah,
       'datapembeliansampah' : datapembeliansampah,
       'datapenarikan' : datapenarikan,
       'datasampah' : datasampah
           
    }
    return render(request, 'dashboard/index.html', context) 


