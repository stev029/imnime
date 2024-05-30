import os.path
import pathlib
import uuid

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import FileExtensionValidator

from hitcount.models import HitCount, HitCountMixin
from video_encoding.fields import VideoField
from video_encoding.models import Format


def dir_path(instance, filename):
    _, ext = os.path.splitext(instance.media.name)
    return "anime_%s/%s/%s" % (instance.get_foldername, ext.replace(".", ""), filename)

class StatusModel(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

class GenreModel(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

class StreamModel(models.Model):
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    duration = models.FloatField(editable=False, null=True)

    file = VideoField(upload_to="mov/", width_field='width', height_field='height',
                     duration_field='duration')

    format_set = GenericRelation(Format)

    def __str__(self):
        return self.file.name

    def delete(self, *args, **kwargs):
        pathlib.Path(self.media.path).unlink(missing_ok=True)

    @property
    def get_foldername(self):
        return self.episode_anime.anime.id

class EpisodeAnimeModel(models.Model):
    title = models.CharField(max_length=255)
    episode = models.IntegerField(null=False, blank=False)
    stream = models.ForeignKey(StreamModel, on_delete=models.CASCADE, related_name="episode_anime", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AnimeModel(models.Model, HitCountMixin):
    title = models.CharField(null=False, blank=False, max_length=255)
    synopsis = models.TextField(null=False, blank=False)
    _type = models.CharField(max_length=255)
    season = models.CharField(max_length=255)
    publish = models.DateTimeField(null=False, blank=True)
    region = models.CharField(max_length=255)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')
    status = models.ForeignKey(StatusModel, on_delete=models.CASCADE, related_name="anime")
    genre = models.ForeignKey(GenreModel, on_delete=models.CASCADE, related_name="anime", blank=True, null=True)
    episode = models.ManyToManyField(EpisodeAnimeModel, related_name="anime", blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ImageModel(models.Model):
    media = models.ImageField(upload_to=dir_path)
    anime = models.ForeignKey(AnimeModel, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.media.name
    
    @property
    def get_foldername(self):
        return self.anime.id

