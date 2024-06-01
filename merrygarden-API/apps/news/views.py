from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from .models import *
from .serializers import *

# Create your views here.
class NewsAPIView(ListAPIView):
    queryset = News.objects.all() # SELECT * FROM 
    serializer_class = NewsSerializer

class NewsAPICreate(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsAPIRetrieve(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

class NewsAPIUpdate(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

class NewsAPIDestroy(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

    