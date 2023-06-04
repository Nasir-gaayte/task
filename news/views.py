from django.shortcuts import render, redirect
from . models import NewsModel,NewsCategoryModel
from . forms import NewsFrom, NewsCategoryFrom




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
