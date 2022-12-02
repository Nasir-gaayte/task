from django.shortcuts import render ,redirect
from django.contrib.auth import login

from . models import Contactmodel, Citymodel, Categorymodel
from . forms import AddForm

# Create your views here.



def home(request):
    conts= Contactmodel.objects.all()
    category = request.GET.get('name')
    city = request.GET.get('name')
    if category or city == None:
        catt = Categorymodel.objects.all().order_by('-id') or Citymodel.objects.all()

    else:
        catt = Categorymodel.objects.filter(category__name='name') or Citymodel.objects.filter(city__name='name')   
        print(category)
    categores= Categorymodel.objects.all()
    citys = Citymodel.objects.all()
    return render(request,'core/home.html',{
        'catt':catt,
        'conts':conts,
        'categores':categores,
        'citys':citys,
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
