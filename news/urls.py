from django.urls import path
from .views import news, newsDetail, update_news


urlpatterns = [
    path('news/',news,name='news'),
    path('news_detail/<str:pk>/',newsDetail,name='news_detail'),
    path('news_update/<str:pk>/',update_news,name='news_update'),
   
]


