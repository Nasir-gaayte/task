from django.shortcuts import render ,redirect
from django.contrib.auth import login
from django.contrib import messages

from django.views.generic import DetailView

from . models import Contactmodel, Citymodel, Categorymodel
from . forms import AddForm, CategoryForm, CityForm

# Create your views here.
def delete_re(request, id):
    ca = Categorymodel.objects.get(pk = id)
    if request: 
        ca.delete()
        return redirect('home')
    
    
def delete_re2(request, id):
    ci = Citymodel.objects.get(pk = id)
    if request: 
        ci.delete()
        return redirect('home')    
     
    
    


def change(request):
    cats = Categorymodel.objects.all()
    citys = Citymodel.objects.all()
    return render(request,"core/change.html",{
        'cats':cats,
        'citys':citys,
    })


def cat(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CategoryForm()    
    return render(request,"core/cat.html",{
        "form":form,
    })    
    
def cityes(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CityForm()    
    return render(request,"core/city.html",{
        "form":form,
    })    


class DetailI(DetailView):
    model = Contactmodel
    # form_class = AddForm
    context_object_name = 'sss'
    template_name= 'core/views.html'



def search(request):
    if request.method == "POST":
        s_naem= request.POST['name']
        # s_category =request.POST['category']
        searched = Contactmodel.objects.filter(name__contains=s_naem)
        # searched = Contactmodel.objects.filter(name__contains=s_category)
    return render(request,'core/search.html',{
        'searched':searched,
        
        })


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
    
    # if category == None :
    #     conts =  Contactmodel.objects.all().order_by('-id') 
    # elif city:       
    #     conts = Contactmodel.objects.filter(category__name=category)
    #     print(conts)
    # else:
    #     messages.error(request,f"no city have this name on the website")    
           
        
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
        image = request.FILES.get('logo')
        locat_imo = request.FILES.get('location_imo')
        category = Categorymodel.objects.get(id= data['category'])
        print(category)
        name= Citymodel.objects.get(id= data['city'])
        print(name)
        
       
          
        Contactmodel.objects.get_or_create (
            auther = username,
            logo = image,
            name  = data['name'],
            category = category,
            city=name ,
            phone1 = data['phone1'],
            email = data['email'],
            location_url = data['location_url'],
            location_imo = locat_imo,
            desc = data['desc'],
            
        
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
    
        
       