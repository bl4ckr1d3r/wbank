from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Databukutabungan
from .forms import DatabukutabunganForm
# Create your views here.
@login_required(login_url='login')
def index(request):
    databukutabungan = Databukutabungan.objects.all()
    context = {
        'databukutabungan' : databukutabungan,
           
    }
    return render(request, 'databukutabungan/index.html', context) 


def createbukutabungan(request):
    form = DatabukutabunganForm()

    if request.method == "POST":
        form = DatabukutabunganForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('databukutabungan') 
        
       
    context = {
        'form' : form

    } 
    return render(request, 'databukutabungan/create.html', context)  

def updatebukutabungan(request, pk):
    bukutabungan = Databukutabungan.objects.get(id=pk)
    form = DatabukutabunganForm(instance=bukutabungan)
    if request.method == "POST":
        form = DatabukutabunganForm(request.POST, instance=bukutabungan)
        if form.is_valid():
            form.save()
            return redirect('databukutabungan')

    context = {
        'form' : form
    }

    return render(request, 'databukutabungan/update.html', context)

def deletebukutabungan(request, pk):
    bukutabungan = Databukutabungan.objects.get(id=pk)
    if request.method == "POST":
        bukutabungan.delete()
        return redirect('databukutabungan')
    
    context = {
        'item' : bukutabungan,
    }
    return render(request, 'databukutabungan/delete.html', context)