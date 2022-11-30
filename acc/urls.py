from django.urls import path
from . import views



urlpatterns = [
    path('regiter/',views.register_req,name='register'),
]
