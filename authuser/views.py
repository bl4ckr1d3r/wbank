from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def loginUser(request):
    
    context = {
        'title' : 'Login | Bank Sampah We SAVE ',
    } 

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)

            return redirect('dashboard') 
        else :
            messages.error(request, 'Wrong username or password')
            

    return render(request, 'authuser/loginregister.html', context) 

def logoutUser(request):
    logout(request)
    return redirect('login') 