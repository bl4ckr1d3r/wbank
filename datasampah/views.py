from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Datasampah
from .forms import DatasampahForm
# Create your views here.
#@login_required(login_url='login')
def index(request):
    datasampah = Datasampah.objects.all()
    context = {
        'datasampah' : datasampah,
           
    }
    return render(request, 'datasampah/index.html', context) 


def createsampah(request):
    form = DatasampahForm()

    if request.method == "POST":
        hargajual = request.POST['hargajual']
        hargabeli = request.POST['hargabeli']
        
        margin = int(hargajual) - int(hargabeli) 
        
        
        form = DatasampahForm(request.POST) 
        if form.is_valid():
            updatemargin = form.save(commit=False)
            updatemargin.margin= margin
            updatemargin.save()
            
            return redirect('datasampah') 
        
       
    context = {
        'form' : form

    } 
    return render(request, 'datasampah/create.html', context)  

def updatesampah(request, pk):
    sampah = Datasampah.objects.get(id=pk)
    form = DatasampahForm(instance=sampah)
    if request.method == "POST":
        form = DatasampahForm(request.POST, instance=sampah)
        if form.is_valid():
            form.save()
            return redirect('datasampah')

    context = {
        'form' : form
    }

    return render(request, 'datasampah/update.html', context)

def deletesampah(request, pk):
    sampah = Datasampah.objects.get(id=pk)
    if request.method == "POST":
        sampah.delete()
        return redirect('datasampah')
    
    context = {
        'item' : sampah,
    }
    return render(request, 'datasampah/delete.html', context)# Create your views here.


