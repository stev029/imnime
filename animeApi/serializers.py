from rest_framework import serializers

from animeApi.models import *
from utils.timetostr import ToStr

class AnimeSerializerMixin(serializers.ModelSerializer):
    class Meta:
        model = AnimeModel
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ["media"]

class AnimeSerializer(AnimeSerializerMixin):
    noe = serializers.SerializerMethodField(read_only=True)
    status = serializers.StringRelatedField()
    published = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="anime-watch", lookup_field="id")
    images = ImageSerializer(many=True)
    
    class Meta:
        model = AnimeModel
        fields = ["id", "title", "published", "_type", "noe", "status", "images", "url"]

    def get_noe(self, obj):
        return obj.episode.count()

    def get_published(self, obj):
        return ToStr(obj.publish)

class SugestSerializer(serializers.Serializer):
    anime = AnimeSerializer(many=True)
    length = serializers.SerializerMethodField(read_only=True)

    class Meta:
        fields = "__all__"

    def get_length(self, obj):
        return AnimeModel.objects.count()

class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamModel
        fields = ["file", "height", "width", "duration"]

class WatchSerializer(AnimeSerializer)
