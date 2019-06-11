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


""" limit to 50 """
@task(name="get_all_article")
def get_all_article():
	articles = Article.objects.all()[:50]
	serializer = ArticleSerializer(articles, context={'request': None}, many=True)
	return serializer.data

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
	vector = SearchVector('_0seconds_55seconds', '_55seconds_110seconds', '_110seconds_165seconds','_165seconds_220seconds','_220seconds_275seconds', '_275seconds_330seconds','_330seconds_385seconds','_385seconds_440seconds','_440seconds_495seconds','_495seconds_550seconds','_550seconds_605seconds','_605seconds_660seconds','_660seconds_715seconds','_715seconds_770seconds','_770seconds_825seconds','_825seconds_880seconds','_880seconds_935seconds','_935seconds_990seconds','_990seconds_1045seconds','_1045seconds_1100seconds','_1100seconds_1155seconds','_1155seconds_1210seconds','_1210seconds_1265seconds','_1265seconds_1320seconds','_1320seconds_1375seconds','_1375seconds_1430seconds','_1430seconds_1485seconds','_1485seconds_1540seconds','_1540seconds_1595seconds','_1595seconds_1650seconds','_1650seconds_1705seconds','_1705seconds_1760seconds','_1760seconds_1815seconds','_1815seconds_1870seconds','_1870seconds_1925seconds','_1925seconds_1980seconds','_1980seconds_2035seconds','_2035seconds_2090seconds','_2090seconds_2145seconds','_2145seconds_2200seconds','_2200seconds_2255seconds','_2255seconds_2310seconds','_2310seconds_2365seconds','_2365seconds_2420seconds','_2420seconds_2475seconds','_2475seconds_2530seconds','_2530seconds_2585seconds','_2585seconds_2640seconds','_2640seconds_2695seconds','_2695seconds_2750seconds','_2750seconds_2805seconds','_2805seconds_2860seconds','_2860seconds_2915seconds','_2915seconds_2970seconds','_2970seconds_3025seconds','_3025seconds_3080seconds','_3080seconds_3135seconds','_3135seconds_3190seconds','_3190seconds_3245seconds','_3245seconds_3300seconds','_3300seconds_3355seconds','_3355seconds_3410seconds','_3410seconds_3465seconds','_3465seconds_3520seconds','_3520seconds_3575seconds','_3575seconds_3630seconds','_3630seconds_3685seconds','_3685seconds_3740seconds','_3740seconds_3795seconds','_3795seconds_3850seconds','_3850seconds_3905seconds','_3905seconds_3960seconds','_3960seconds_4015seconds','_4015seconds_4070seconds','_4070seconds_4125seconds','_4125seconds_4180seconds','_4180seconds_4235seconds','_4235seconds_4290seconds','_4290seconds_4345seconds','_4345seconds_4400seconds','_4400seconds_4455seconds','_4455seconds_4510seconds','_4510seconds_4565seconds','_4565seconds_4620seconds','_4620seconds_4675seconds','_4675seconds_4730seconds','_4730seconds_4785seconds','_4785seconds_4840seconds','_4840seconds_4895seconds','_4895seconds_4950seconds','_4950seconds_5005seconds')
	query = SearchQuery(pk)
	ranked_results = Transcription.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank').values_list('video_uuid', flat=True)[:50]
	print(ranked_results)
	ranked_array = []
	for key in ranked_results:
		articles = Article.objects.all()
		article = get_object_or_404(articles, video_uuid=key)
		serializer = ArticleSerializer(article, many=False)
		ranked_array.append(serializer.data)
	return ranked_array




