from django.shortcuts import render

# Create your views here.


def register_req(request):
    return render(request,'acc/register.html')