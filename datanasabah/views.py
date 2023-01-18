from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Datanasabah
from .forms import DatanasabahForm
# Create your views here.
@login_required(login_url='login')
def index(request):
    datanasabah = Datanasabah.objects.all()
    context = {
        'datanasabah' : datanasabah,
           
    }
    return render(request, 'datanasabah/index.html', context) 


def createnasabah(request):
    form = DatanasabahForm()

    if request.method == "POST":
        form = DatanasabahForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('datanasabah') 
        
       
    context = {
        'form' : form

    } 
    return render(request, 'datanasabah/create.html', context)  

def updatenasabah(request, pk):
    nasabah = Datanasabah.objects.get(id=pk)
    form = DatanasabahForm(instance=nasabah)
    if request.method == "POST":
        form = DatanasabahForm(request.POST, instance=nasabah)
        if form.is_valid():
            form.save()
            return redirect('datanasabah')

    context = {
        'form' : form
    }

    return render(request, 'datanasabah/update.html', context)

def deletenasabah(request, pk):
    nasabah = Datanasabah.objects.get(id=pk)
    if request.method == "POST":
        nasabah.delete()
        return redirect('datanasabah')
    
    context = {
        'item' : nasabah,
    }
    return render(request, 'datanasabah/delete.html', context)