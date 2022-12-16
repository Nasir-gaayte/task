from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update_req,name='update'),
    path('delete/<int:id>/',views.delete_req,name='delete'),
    path('search/',views.search,name='search'),
    path('views/<pk>/',views.DetailI.as_view(),name='views'),
    path('cat/',views.cat,name='cat'),
    path('city/',views.cityes,name='city'),
    path('change/',views.change,name='change'),
    path('del/<int:id>',views.delete_re,name='del'),
    path('del2/<int:id>',views.delete_re2,name='del2'),
    
]

