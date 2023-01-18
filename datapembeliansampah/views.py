from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Datapembeliansampah
from datasampah.models import Datasampah
from databukutabungan.models import Databukutabungan
from .forms import DatapembeliansampahForm
# Create your views here.
@login_required(login_url='login')
def index(request):
    datapembeliansampah = Datapembeliansampah.objects.all()
    context = {
        'datapembeliansampah' : datapembeliansampah,
           
    }
    return render(request, 'datapembeliansampah/index.html', context) 


def createpembeliansampah(request):
    form = DatapembeliansampahForm()
    datasampah = Datasampah.objects.all()
    databukutabungan = Databukutabungan.objects.all()
    saldoakhir = 0

    if request.method == "POST":
        norekening = request.POST['norekening']
        jenissampah = request.POST['jenissampah']
        berat = request.POST['berat']
        datasampah = Datasampah.objects.get(id=jenissampah)
        hargabeli = datasampah.hargabeli
        
        jumlah = int(berat) * hargabeli
        databukutabungan = Databukutabungan.objects.get(id=norekening)
        saldoawal = databukutabungan.saldonominal
        saldoakhir = saldoakhir + jumlah
        databukutabungan.saldonominal = saldoakhir
        
        databukutabungan.save()

       # saldoemasawal = databukutabungan.saldoemas
       # saldoemas = jumlah / 800000 
       # saldoemasakhir = saldoemasawal + saldoemas
       # databukutabungan.saldoemas = saldoemasakhir 
       # databukutabungan.save()
        

             
        form = DatapembeliansampahForm(request.POST) 
        
        if form.is_valid():
            updatejumlah = form.save(commit=False)
            updatejumlah.jumlah = jumlah
            updatejumlah.save()
            #form.save()
            return redirect('datapembeliansampah') 
        
       
    context = {
        'form' : form

    } 
    return render(request, 'datapembeliansampah/create.html', context)  

def updatepembeliansampah(request, pk):
    pembeliansampah = Datapembeliansampah.objects.get(id=pk)
    form = DatapembeliansampahForm(instance=pembeliansampah)
    if request.method == "POST":
        form = DatapembeliansampahForm(request.POST, instance=pembeliansampah)
        if form.is_valid():
            form.save()
            return redirect('datapembeliansampah')

    context = {
        'form' : form
    }

    return render(request, 'datapembeliansampah/update.html', context)

def deletepembeliansampah(request, pk):
    pembeliansampah = Datapembeliansampah.objects.get(id=pk)
    if request.method == "POST":
        pembeliansampah.delete()
        return redirect('datapembeliansampah')
    
    context = {
        'item' : pembeliansampah,
    }
    return render(request, 'datapembeliansampah/delete.html', context)# Create your views here.


