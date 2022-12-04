from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update_req,name='update'),
    path('delete/<int:id>/',views.delete_req,name='delete'),
    path('search/',views.search,name='search'),
    
]

