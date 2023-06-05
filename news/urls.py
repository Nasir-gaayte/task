from django.urls import path
from .views import (news,
                    newsDetail,
                    update_news,
                    add_news,deleteNews,
                    newsGet,
                    newsCatsGet,
                    newsGetById,
                    newsCatsGetById,
                    )


urlpatterns = [
    path('news/',news,name='news'),
    path('news_detail/<str:pk>/',newsDetail,name='news_detail'),
    path('news_update/<str:pk>/',update_news,name='news_update'),
    path('delete_news/<str:pk>/',deleteNews,name='delete_news'),
    path('add_news/',add_news,name='add_news'),
    
     #________________api url __________________
    
    path('api/news_get/',newsGet),
    path('api/news_category/',newsCatsGet),
    path('api/news_id/<str:pk>/',newsGetById),
    path('api/news_category_id/<str:pk>/',newsCatsGetById),
   
]


