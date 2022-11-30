from django.shortcuts import render ,redirect
from django.contrib.auth import login

from . models import Contactmodel
from . forms import AddForm

# Create your views here.



def home(request):
    conts= Contactmodel.objects.all()
    return render(request,'core/home.html',{'conts':conts})



def add(request):
    if request.method == "POST":
        form = AddForm(request.POST, user=request.user)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('home')
    form = AddForm()        
    return render(request,'core/add.html',{'form':form})