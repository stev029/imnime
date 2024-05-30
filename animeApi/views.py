import datetime

from rest_framework.generics import *
from rest_framework.response import Response

from animeApi.models import *
from animeApi.serializers import *

class AnimeApiView(ListAPIView):
    serializer_class = AnimeSerializer
    queryset = AnimeModel.objects.all()

class SugestApiView(ListAPIView):
    serializer_class = SugestSerializer
    queryset = AnimeModel.objects.all()

    def get_queryset(self):
        return { "anime": super().get_queryset() }

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

class AnimeWatchView(RetrieveAPIView):
    queryset = StreamModel.objects.all()
    serializer_class = WatchSerializer

class AnimeUpload(ListAPIView):
    queryset = AnimeModel.objects.filter(episode__created_at__gte=datetime.datetime.now() - datetime.timedelta(days=1)).order_by("-created_at")
    serializer_class = AnimeSerializer
