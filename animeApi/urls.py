from django.urls import path

import animeApi.views as animeViews

urlpatterns = [
    path("sugest/", animeViews.SugestApiView.as_view(), name="sugest"),
    path("watch/<id>/", animeViews.AnimeWatchView.as_view(), name="anime-watch"),
    path("upload/", animeViews.AnimeUpload.as_view(), name="anime-upload"),
    path("", animeViews.AnimeApiView.as_view(), name="anime-list"),
]
