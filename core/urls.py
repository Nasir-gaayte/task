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
    path('promo/',views.addpromo,name='promo'),
    path('pro_del/<int:id>',views.promodel,name='pro_del'),
    
    
    
    
    #________________api url __________________
    
    path('api/contact/',views.contactGet),
    path('api/contact/<str:pk>/',views.contactGetById),
    path('api/city/',views.cityGet),
    path('api/city/<str:pk>/',views.cityGetById),
    path('api/category/',views.categoryGet),
    path('api/category/<str:pk>/',views.categoryGetById),
    
]

