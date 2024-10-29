from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .forms import Regform
from django.http import HttpResponse



from django.shortcuts import render, redirect
from .forms import Regform  # Adjust this import based on your project structure




# Create your views here.

# def message(request):
#     return HttpResponse('Successfully registered')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('Rform')  # Replace with the actual URL name or path

        else:
            messages.error(request, 'Invalid details.')
            return redirect('login')  # Replace with the actual URL name or path

    else:
        return render(request, "login.html")






'''def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Form submitted successfully.')

            return redirect('message')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,"login.html")'''

def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('login')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            print("user created")
        else:
            print("password not matched")
            return redirect('registration')
        return redirect('/')

    else:

        return render(request,'registration.html')








# def Rform(request):
#     if request.method=="POST":
#         form=Regform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('message')
#     else:
#         form=Regform()
#     return render(request,'Rform.html')



def message(request):
    return render(request,'message.html')

def Rform(request):
    if request.method == "POST":
        form = Regform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('message')
    else:
        form = Regform()
    return render(request, 'Rform.html', {'form': form})












def branches(request):
    return render(request, 'branches.html')

def logout(request):
    return render(request, 'index.html')
def index(request):
    return render(request, 'index.html')
def dropdown(request):
    return render(request, 'dropdown.html')
def home(request):
    return render(request, 'index.html')




