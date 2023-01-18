from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Datapenarikan
from databukutabungan.models import Databukutabungan
from .forms import DatapenarikanForm
# Create your views here.

@login_required(login_url='login')
def index(request):
    datapenarikan = Datapenarikan.objects.all()
    context = {
        'datapenarikan' : datapenarikan,
           
    }
    return render(request, 'datapenarikan/index.html', context) 


def createpenarikan(request):
    form = DatapenarikanForm()
    
    databukutabungan = Databukutabungan.objects.all()
    saldoakhir = 0

    if request.method == "POST":
        norekening = request.POST['norekening']
        jumlah = request.POST['jumlah']
     
        databukutabungan = Databukutabungan.objects.get(id=norekening)
        saldoawal = databukutabungan.saldonominal
        saldoakhir = saldoawal - int(jumlah)
        databukutabungan.saldonominal = saldoakhir 
        databukutabungan.save()    
        
     #   databukutabungan.save()

       # saldoemasawal = databukutabungan.saldoemas
       # saldoemas = jumlah / 800000 
       # saldoemasakhir = saldoemasawal + saldoemas
       # databukutabungan.saldoemas = saldoemasakhir 
       # databukutabungan.save()
        

             
        form = DatapenarikanForm(request.POST) 
        
        if form.is_valid():
      #      updatejumlah = form.save(commit=False)
       #     updatejumlah.jumlah = jumlah
       #     updatejumlah.save()
            form.save()
            return redirect('datapenarikan') 
        
       
    context = {
        'form' : form

    } 
    return render(request, 'datapenarikan/create.html', context)  

def updatepenarikan(request, pk):
    penarikan = Datapenarikan.objects.get(id=pk)
    form = DatapenarikanForm(instance=penarikan)
    if request.method == "POST":
        form = DatapenarikanForm(request.POST, instance=penarikan)
        if form.is_valid():
            form.save()
            return redirect('datapenarikan')

    context = {
        'form' : form
    }

    return render(request, 'datapenarikan/update.html', context)

def deletepenarikan(request, pk):
    penarikan = Datapenarikan.objects.get(id=pk)
    if request.method == "POST":
        penarikan.delete()
        return redirect('datapenarikan')
    
    context = {
        'item' : penarikan,
    }
    return render(request, 'datapenarikan/delete.html', context)# Create your views here.


