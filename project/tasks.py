import string

from django.utils.crypto import get_random_string
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
from collections import OrderedDict
from django.shortcuts import get_object_or_404


from celery import shared_task
from celery.decorators import task


@shared_task
def create_user_task():
	print("creating user")
	return 15

@task(name="delete_one_article")
def delete_one_article(pk):
	articles = Article.objects.all()
	article = get_object_or_404(articles, video_uuid=pk)
	print(article)
	article.delete()
	return "Article Deleted"

@task(name="tasks.get_article_pk")
def get_article_pk(pk):
	print("get--------------------------")
	"""find video uuid based on pk"""
	vector = SearchVector('_0seconds_55seconds', '_55seconds_110seconds', '_110seconds_165seconds','_165seconds_220seconds','_220seconds_275seconds', '_275seconds_330seconds','_330seconds_385seconds','_385seconds_440seconds','_440seconds_495seconds','_495seconds_550seconds','_550seconds_605seconds','_605seconds_660seconds','_660seconds_715seconds','_715seconds_770seconds','_770seconds_825seconds','_825seconds_880seconds','_880seconds_935seconds')
	query = SearchQuery(pk)
	ranked_results = Transcription.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank').values_list('video_uuid', flat=True)
	print(ranked_results)
	ranked_array = []
	for key in ranked_results:
		articles = Article.objects.all()
		article = get_object_or_404(articles, video_uuid=key)
		serializer = ArticleSerializer(article, many=False)
		ranked_array.append(serializer.data)
	return ranked_array



