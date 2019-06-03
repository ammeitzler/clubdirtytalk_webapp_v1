from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class TranscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcription
        fields = ('video_uuid', '_0seconds_55seconds', '_55seconds_110seconds', '_110seconds_165seconds','_165seconds_220seconds','_220seconds_275seconds', '_275seconds_330seconds','_330seconds_385seconds','_385seconds_440seconds','_440seconds_495seconds','_495seconds_550seconds','_550seconds_605seconds','_605seconds_660seconds','_660seconds_715seconds','_715seconds_770seconds','_770seconds_825seconds','_825seconds_880seconds','_880seconds_935seconds')

class ArticleSerializer(serializers.ModelSerializer):
    transcripts = TranscriptionSerializer(many=True)
    class Meta:
        model = Article
        fields = ('video_uuid','title', 'site_url','image_url', 'duration', 'rating', 'source', 'transcripts')
        lookup_field = 'search_text'
        extra_kwargs = {
            'url': {'lookup_field': 'search_text'},
        }

    def create(self, validated_data):
        transcription_data = validated_data.pop('transcripts')
        article = Article.objects.create(**validated_data)
        for transcript_data in transcription_data:
            Transcription.objects.create(article=article, **transcript_data)
        return article





""" track and album are for testing """
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('order', 'title', 'duration')

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album


