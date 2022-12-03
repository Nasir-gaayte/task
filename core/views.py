from django.shortcuts import render ,redirect
from django.contrib.auth import login
from django.contrib import messages

from . models import Contactmodel, Citymodel, Categorymodel
from . forms import AddForm

# Create your views here.



def home(request):
    
    
    city = request.GET.get('city')
    print(city)
    if city == None :
        conts =  Contactmodel.objects.all().order_by('-id') 
    elif city:       
        conts = Contactmodel.objects.filter(city__name=city)
        print(conts)
    else:
        messages.error(request,f"no city have this name on the website")
        
           
        
    categores= Categorymodel.objects.all()
    citys = Citymodel.objects.all()
    return render(request,'core/home.html',{
        # 'catt':catt,
        'conts':conts,
        'categores':categores,
        'citys':citys,
        'messages':messages,
        })



# def add(request):
#     if request.method == "POST":
#         form = AddForm(request.POST, user=request.user)
#         if form.is_valid():
#             user=form.save()
#             login(request, user)
#             return redirect('home')
#     form = AddForm()        
#     return render(request,'core/add.html',{'form':form})

def add(request):
    cats =Categorymodel.objects.all()
    citss = Citymodel.objects.all()
    if request.method=="POST":
        data = request.POST
        username = request.user
        category = Categorymodel.objects.get(id= data['category'])
        print(category)
        name= Citymodel.objects.get(id= data['city'])
        print(name)
        
       
          
        Contactmodel.objects.get_or_create (
            auther = username,
            name  = data['name'],
            category = category,
            city=name ,
            phone1 = data['phone1'],
            phone2 = data['phone2'],
        
        )  
        return redirect ('home')        
    return render(request,'core/add.html',{
        
        'cats':cats,
        'citss':citss,
        
        })



def update_req(request, id):
    conts = Contactmodel.objects.get(pk=id)
    if request.method == "POST":
        form = AddForm(request.POST, instance=conts)
        if form.is_valid():
            form.save()
        return redirect ('home')
    form=AddForm(instance=conts)       
    return render(request,'core/update.html',{
        
        'form':form,
        
        })
    
    
def delete_req(request, id):
    conts = Contactmodel.objects.get(pk=id)
    if request:
        conts.delete()
        return redirect('home')
    
        
       