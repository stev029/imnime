from django.contrib import admin
from django.db import models

from video_encoding.admin import FormatInline

from animeApi.models import *

# for cls in dir(animeModel):
#     cls = getattr(animeModel, cls)
#     try:
#         if models.Model in cls.__mro__:
#             @admin.register(cls)
#             class StreamAdmin(admin.ModelAdmin):
#                 pass
#     except Exception as e:
#         pass
    # print(models.Model in cls.__mro__)

@admin.register(AnimeModel)
class AnimeAdmin(admin.ModelAdmin):
    pass

@admin.register(EpisodeAnimeModel)
class AnimeAdmin(admin.ModelAdmin):
    pass

@admin.register(ImageModel)
class AnimeAdmin(admin.ModelAdmin):
    pass

@admin.register(GenreModel)
class AnimeAdmin(admin.ModelAdmin):
    pass

@admin.register(StatusModel)
class AnimeAdmin(admin.ModelAdmin):
    pass

@admin.register(StreamModel)
class VideoAdmin(admin.ModelAdmin):
    model = StatusModel
    inlines = (FormatInline,)

    list_dispaly = ('get_filename', 'width', 'height', 'duration', 'file')
    fields = ('width', 'height', 'duration')
    readonly_fields = fields
    fields += ('file',)


