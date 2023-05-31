from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

from core.filter import ContactFilter

from django.views.generic import DetailView

from . models import Contactmodel, Citymodel, Categorymodel, PromoModel
from . forms import AddForm, CategoryForm, CityForm, PromoForm


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ContactSerializer, CategorySerializer,CitySerializer
@login_required
def addpromo(request):
    if request.method=="POST":
        data = request.POST
        logo = request.FILES.get('logo')
        PromoModel.objects.get_or_create(
            imo = logo,
            desc = data['desc']
        )
    return render(request,"core/add_promo.html",{
        
    })    

@login_required
def promodel(request, id):
    pro_del = PromoModel.objects.get(pk= id)
    if request:
        pro_del.delete()
        return redirect('home')


# Create your views here.
@login_required
def delete_re(request, id):
    ca = Categorymodel.objects.get(pk = id)
    if request: 
        ca.delete()
        return redirect('home')
    
@login_required  
def delete_re2(request, id):
    ci = Citymodel.objects.get(pk = id)
    if request: 
        ci.delete()
        return redirect('home')    
     
    
    

@login_required
def change(request):
    cats = Categorymodel.objects.all()
    citys = Citymodel.objects.all()
    return render(request,"core/change.html",{
        'cats':cats,
        'citys':citys,
    })

@login_required
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
@login_required    
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
    # if request.method=="POST":
    #     s_naem= request.POST['name']
   
    #     searched = Contactmodel.objects.filter(name__contains=s_naem)
    
    cont_filter = ContactFilter(request.GET, queryset =Contactmodel.objects.all())
    
 
            
    return render(request,'core/search.html',{
        'form':cont_filter.form,   
        'searched':cont_filter.qs,
        # 'categores':categores,
        })


def home(request):
   
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        mes = request.POST.get('message')
        
        print(name,mes,email)
        send_mail(
            "Welcome"+name,
            'we well contact you soon -- mar dhaw ayaa lagula soo xirrirayaa mahadsanid'+"\n"+ mes,
            email,
            ['doon1wac101@gmail.com'],
            )
        # return HttpResponse('your mail has send !')
        return redirect('home')
    
    
    if request : 
       cont_filter= ContactFilter(request.GET, queryset =Contactmodel.objects.all())
       
    
    
    # if category == None :
    #     conts =  Contactmodel.objects.all().order_by('-id') 
    # elif city:       
    #     conts = Contactmodel.objects.filter(category__name=category)
    #     print(conts)
    # else:
    #     messages.error(request,f"no city have this name on the website")    
           
    promos = PromoModel.objects.all()    
    conts = Contactmodel.objects.all()
    citys = Citymodel.objects.all()
    return render(request,'core/home.html',{
        'conts':conts,
        'citys':citys,
        'promos':promos,
        'form':cont_filter.form,   
        'searched':cont_filter.qs,
        
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
@login_required
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


@login_required
def update_req(request, id):
    conts = Contactmodel.objects.get(pk=id)
    if request.method == "POST":
        form = AddForm(request.POST,request.FILES, instance=conts, )
        if form.is_valid():
            form.save()
        return redirect ('home')
    form=AddForm(instance=conts)       
    return render(request,'core/update.html',{
        
        'form':form,
        
        })
    
@login_required    
def delete_req(request, id):
    conts = Contactmodel.objects.get(pk=id)
    if request:
        conts.delete()
        return redirect('home')
    
        
#__________________________________________api__________________________________________


#___________contact api____________________


@api_view(['GET'])
def contactGet(request):
    data = Contactmodel.objects.all()
    serializer = ContactSerializer(data, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def contactGetById(request, pk):
    data = Contactmodel.objects.get(id= pk)
    serializer = ContactSerializer(data, many=False)
    return Response(serializer.data)

#_______________city____________________

@api_view(['GET'])
def cityGet(request):
    data = Citymodel.objects.all()
    serializer = CitySerializer(data, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def cityGetById(request, pk):
    data = Citymodel.objects.get(id= pk)
    serializer = CitySerializer(data, many=False)
    return Response(serializer.data)



#_______________category____________________

@api_view(['GET'])
def categoryGet(request):
    data = Categorymodel.objects.all()
    serializer = CategorySerializer(data, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def categoryGetById(request, pk):
    data = Categorymodel.objects.get(id= pk)
    serializer = CategorySerializer(data, many=False)
    return Response(serializer.data)