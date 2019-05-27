from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from project.serializers import *
from .models import *
from django.http import JsonResponse

from .tasks import create_user_task


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    def list(self, request):
        print("here abc")
        x = create_user_task.delay()
        print(x)
        return Response("hi")

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def list(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, context={'request': None}, many=True)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, context={'request': None}, many=True)
        return Response(serializer.data)
        










