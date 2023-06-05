from django.shortcuts import render, redirect
from . models import NewsModel,NewsCategoryModel
from . forms import NewsFrom, NewsCategoryFrom
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import NewsCateSerializer, NewsSerializer

@api_view(['GET'])
def newsGet(request):
    data = NewsModel.objects.all()
    serializer = NewsSerializer(data,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def newsCatsGet(request):
    data = NewsCategoryModel.objects.all()
    serializer = NewsCateSerializer(data,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def newsGetById(request, pk):
    data = NewsModel.objects.get(id=pk)
    serializer = NewsSerializer(data,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def newsCatsGetById(request, pk):
    data = NewsCategoryModel.objects.get(id=pk)
    serializer = NewsCateSerializer(data,many=False)
    return Response(serializer.data)


#------------------------------------------------------
def news(request):
    cats= NewsCategoryModel.objects.all()
    news = NewsModel.objects.all()
    return render(request,'news/news.html',{
        'cats':cats,
        'news':news,
    })
def newsDetail(request, pk):
    cat= NewsCategoryModel.objects.get(id=pk)
    new = NewsModel.objects.get(id=pk)
    return render(request,'news/news_details.html',{
        'cat':cat,
        'new':new,
    })
    
@login_required    
def update_news(request, pk):
    new = NewsModel.objects.get(id=pk)
    if request.method == "POST":
        form = NewsFrom(request.POST, request.FILES, instance=new)
        if form.is_valid():
            form.save()
            return redirect('news')
    form =NewsFrom(instance=new)  
    return render (request,'news/update_news.html',{
        'form':form,
    })          

@login_required
def add_news(request):
    if request.method == "POST":
        data = request.POST
        imgs = request.FILES.get('imgUrl')
        NewsModel.objects.create(
            category = NewsCategoryModel.objects.get(id= data['category']),
            imgUrl = imgs,
            newsTitel=data['newsTitel'],
            by = data['by'],
            body = data['body'],  
        )
        return redirect('news')  
    news = NewsModel.objects.all()
    return render(request,'news/add_news.html',{
        'c':NewsCategoryModel.objects.all(),
        'news':news,
    })  
        

        
def deleteNews(request,pk):
    news= NewsModel.objects.get(id=pk)
    news.delete()
    return redirect('news')
            