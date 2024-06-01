from django.urls import path

from .views import *

urlpatterns = [
    path('', NewsAPIView.as_view(), name='news_api'),
    path('create/', NewsAPICreate.as_view(), name='news_create_api'),
    path('<int:pk>/', NewsAPIRetrieve.as_view(), name='news_retrieve_api'),
    path('update/<int:pk>/', NewsAPIUpdate.as_view(), name='news_update_api'),
    path('destroy/<int:pk>/', NewsAPIDestroy.as_view(), name='news_destroy_api'),
]
