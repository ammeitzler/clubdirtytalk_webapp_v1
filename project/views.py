from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from project.serializers import *
from .models import *
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from oauth2_provider.views.generic import ProtectedResourceView

from .tasks import *


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

    """ return video articles/foo/ """
    @method_decorator(cache_page(60))
    def retrieve(self, request, pk=None):
        res = get_article_pk.delay(pk)
        task_res = res.get()
        task_res_length = len(task_res)
        j_res = []
        for i in range(task_res_length):
            print(task_res[i]["title"])
            title = task_res[i]["title"]
            site_url = task_res[i]["site_url"]
            image_url = task_res[i]["image_url"]
            rating = task_res[i]["rating"]
            j_res.append({"title":title,"site_url":site_url, "image_url":image_url, "rating":rating})
        return JsonResponse(j_res, safe=False)

    def destroy(self, request, pk=None):
        res = delete_one_article.delay(pk)
        print(res)
        task_res = res.get()
        return HttpResponse(task_res)
    
    def list(self, request):
        res = get_all_article.delay(pk)
        task_res = res.get()
        
        # x = Article.objects.filter(title__icontains='First Ever').values_list()
        # found_video_uuid = Transcription.objects.annotate(search=SearchVector('_0seconds_55seconds', '_55seconds_110seconds', '_110seconds_165seconds','_165seconds_220seconds','_220seconds_275seconds', '_275seconds_330seconds','_330seconds_385seconds','_385seconds_440seconds','_440seconds_495seconds','_495seconds_550seconds','_550seconds_605seconds','_605seconds_660seconds','_660seconds_715seconds','_715seconds_770seconds','_770seconds_825seconds','_825seconds_880seconds','_880seconds_935seconds'),).filter(search='loose and limber').values_list('video_uuid', flat=True)
        # vector = SearchVector('_0seconds_55seconds', '_55seconds_110seconds', '_110seconds_165seconds','_165seconds_220seconds','_220seconds_275seconds', '_275seconds_330seconds','_330seconds_385seconds','_385seconds_440seconds','_440seconds_495seconds','_495seconds_550seconds','_550seconds_605seconds','_605seconds_660seconds','_660seconds_715seconds','_715seconds_770seconds','_770seconds_825seconds','_825seconds_880seconds','_880seconds_935seconds')
        # query = SearchQuery('malicious juice')
        # ranked_results = Transcription.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank').values_list('video_uuid', flat=True)

        # print(ranked_results)
        # print(x)
        # print(found_video_uuid)
        return Response(task_res)
        










