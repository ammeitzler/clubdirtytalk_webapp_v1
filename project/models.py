# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

class Article(models.Model):
	video_uuid = models.CharField(max_length=255, null=True, blank=True)
	title = models.CharField(max_length=255, null=True, blank=True)
	site_url =  models.URLField(default=False)
	image_url =  models.URLField(default=False)
	duration = models.TimeField(default=False, null=True)
	rating = models.CharField(max_length=255, null=True, blank=True)
	source = models.CharField(max_length=255, null=True, blank=True)
	class Meta:
		unique_together = ('video_uuid','site_url')

class Transcription(models.Model):
	article = models.ForeignKey(Article, related_name='transcripts', on_delete=models.CASCADE)
	video_uuid = models.CharField(max_length=255, null=True, blank=True)
	_0seconds_55seconds = models.TextField(max_length=None, blank=True)
	_55seconds_110seconds = models.TextField(max_length=None, blank=True)
	_110seconds_165seconds = models.TextField(max_length=None, blank=True)
	_165seconds_220seconds = models.TextField(max_length=None, blank=True)
	_220seconds_275seconds = models.TextField(max_length=None, blank=True)
	_275seconds_330seconds = models.TextField(max_length=None, blank=True)
	_330seconds_385seconds = models.TextField(max_length=None, blank=True)
	_385seconds_440seconds = models.TextField(max_length=None, blank=True)
	_440seconds_495seconds = models.TextField(max_length=None, blank=True)
	_495seconds_550seconds = models.TextField(max_length=None, blank=True)
	_550seconds_605seconds = models.TextField(max_length=None, blank=True)
	_605seconds_660seconds = models.TextField(max_length=None, blank=True)
	_660seconds_715seconds = models.TextField(max_length=None, blank=True)
	_715seconds_770seconds = models.TextField(max_length=None, blank=True)
	_770seconds_825seconds = models.TextField(max_length=None, blank=True)
	_825seconds_880seconds = models.TextField(max_length=None, blank=True)
	_880seconds_935seconds = models.TextField(max_length=None, blank=True)
	_935seconds_990seconds = models.TextField(max_length=None, blank=True)
	_990seconds_1045seconds = models.TextField(max_length=None, blank=True)
	_1045seconds_1100seconds = models.TextField(max_length=None, blank=True)
	_1100seconds_1155seconds = models.TextField(max_length=None, blank=True)
	_1155seconds_1210seconds = models.TextField(max_length=None, blank=True)
	_1210seconds_1265seconds = models.TextField(max_length=None, blank=True)
	_1265seconds_1320seconds = models.TextField(max_length=None, blank=True)
	_1320seconds_1375seconds = models.TextField(max_length=None, blank=True)
	_1375seconds_1430seconds = models.TextField(max_length=None, blank=True)
	_1430seconds_1485seconds = models.TextField(max_length=None, blank=True)
	_1485seconds_1540seconds = models.TextField(max_length=None, blank=True)
	_1540seconds_1595seconds = models.TextField(max_length=None, blank=True)
	_1595seconds_1650seconds = models.TextField(max_length=None, blank=True)
	_1650seconds_1705seconds = models.TextField(max_length=None, blank=True)
	_1705seconds_1760seconds = models.TextField(max_length=None, blank=True)
	_1760seconds_1815seconds = models.TextField(max_length=None, blank=True)
	_1815seconds_1870seconds = models.TextField(max_length=None, blank=True)
	_1870seconds_1925seconds = models.TextField(max_length=None, blank=True)
	_1925seconds_1980seconds = models.TextField(max_length=None, blank=True)
	_1980seconds_2035seconds = models.TextField(max_length=None, blank=True)
	_2035seconds_2090seconds = models.TextField(max_length=None, blank=True)
	_2090seconds_2145seconds = models.TextField(max_length=None, blank=True)
	_2145seconds_2200seconds = models.TextField(max_length=None, blank=True)
	_2200seconds_2255seconds = models.TextField(max_length=None, blank=True)
	_2255seconds_2310seconds = models.TextField(max_length=None, blank=True)
	_2310seconds_2365seconds = models.TextField(max_length=None, blank=True)
	_2365seconds_2420seconds = models.TextField(max_length=None, blank=True)
	_2420seconds_2475seconds = models.TextField(max_length=None, blank=True)
	_2475seconds_2530seconds = models.TextField(max_length=None, blank=True)
	_2530seconds_2585seconds = models.TextField(max_length=None, blank=True)
	_2585seconds_2640seconds = models.TextField(max_length=None, blank=True)
	_2640seconds_2695seconds = models.TextField(max_length=None, blank=True)
	_2695seconds_2750seconds = models.TextField(max_length=None, blank=True)
	_2750seconds_2805seconds = models.TextField(max_length=None, blank=True)
	_2805seconds_2860seconds = models.TextField(max_length=None, blank=True)
	_2860seconds_2915seconds = models.TextField(max_length=None, blank=True)
	_2915seconds_2970seconds = models.TextField(max_length=None, blank=True)
	_2970seconds_3025seconds = models.TextField(max_length=None, blank=True)
	_3025seconds_3080seconds = models.TextField(max_length=None, blank=True)
	_3080seconds_3135seconds = models.TextField(max_length=None, blank=True)
	_3135seconds_3190seconds = models.TextField(max_length=None, blank=True)
	_3190seconds_3245seconds = models.TextField(max_length=None, blank=True)
	_3245seconds_3300seconds = models.TextField(max_length=None, blank=True)
	_3300seconds_3355seconds = models.TextField(max_length=None, blank=True)
	_3355seconds_3410seconds = models.TextField(max_length=None, blank=True)
	_3410seconds_3465seconds = models.TextField(max_length=None, blank=True)
	_3465seconds_3520seconds = models.TextField(max_length=None, blank=True)
	_3520seconds_3575seconds = models.TextField(max_length=None, blank=True)
	_3575seconds_3630seconds = models.TextField(max_length=None, blank=True)
	_3630seconds_3685seconds = models.TextField(max_length=None, blank=True)
	_3685seconds_3740seconds = models.TextField(max_length=None, blank=True)
	_3740seconds_3795seconds = models.TextField(max_length=None, blank=True)
	_3795seconds_3850seconds = models.TextField(max_length=None, blank=True)
	_3850seconds_3905seconds = models.TextField(max_length=None, blank=True)
	_3905seconds_3960seconds = models.TextField(max_length=None, blank=True)
	_3960seconds_4015seconds = models.TextField(max_length=None, blank=True)
	_4015seconds_4070seconds = models.TextField(max_length=None, blank=True)
	_4070seconds_4125seconds = models.TextField(max_length=None, blank=True)
	_4125seconds_4180seconds = models.TextField(max_length=None, blank=True)
	_4180seconds_4235seconds = models.TextField(max_length=None, blank=True)
	_4235seconds_4290seconds = models.TextField(max_length=None, blank=True)
	_4290seconds_4345seconds = models.TextField(max_length=None, blank=True)
	_4345seconds_4400seconds = models.TextField(max_length=None, blank=True)
	_4400seconds_4455seconds = models.TextField(max_length=None, blank=True)
	_4455seconds_4510seconds = models.TextField(max_length=None, blank=True)
	_4510seconds_4565seconds = models.TextField(max_length=None, blank=True)
	_4565seconds_4620seconds = models.TextField(max_length=None, blank=True)
	_4620seconds_4675seconds = models.TextField(max_length=None, blank=True)
	_4675seconds_4730seconds = models.TextField(max_length=None, blank=True)
	_4730seconds_4785seconds = models.TextField(max_length=None, blank=True)
	_4785seconds_4840seconds = models.TextField(max_length=None, blank=True)
	_4840seconds_4895seconds = models.TextField(max_length=None, blank=True)
	_4895seconds_4950seconds = models.TextField(max_length=None, blank=True)
	_4950seconds_5005seconds = models.TextField(max_length=None, blank=True)
	class Meta:
		unique_together = ('article', 'video_uuid')

	# def __str__(self):
	# 	return '%d: %s' % (self.video_uuid)


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)




# class Entry(models.Model):
# 	video_uuid = models.CharField(max_length=255, null=True, blank=True)
# 	title = models.CharField(max_length=255, null=True, blank=True)
# 	duration = models.CharField(max_length=255, null=True, blank=True)
# 	rating = models.IntegerField(default=False)
# 	# image_file = models.ImageField(upload_to='images')
# 	site_url =  models.URLField(default=False)
# 	image_url =  models.URLField(default=False)
# 	source = models.CharField(max_length=255, null=True, blank=True)
# 	# transcription_id = models.IntegerField(default=False)
# 	transcriptions = models.ForeignKey(Transcription, on_delete=models.CASCADE, related_name='video_transcription', blank=True)
# 	created_at = models.DateTimeField(auto_now_add=True)
	
# 	def __str__(self):
# 		return self



