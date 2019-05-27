# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

class Article(models.Model):
	video_uuid = models.CharField(max_length=255, null=True, blank=True)
	title = models.CharField(max_length=255, null=True, blank=True)
	site_url =  models.URLField(default=False)
	image_url =  models.URLField(default=False)

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
	class Meta:
		unique_together = ('article', 'video_uuid')

	def __str__(self):
		return '%d: %s' % (self.video_uuid)


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



