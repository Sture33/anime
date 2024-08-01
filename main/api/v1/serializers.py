from rest_framework import serializers

from anime_app.models import Anime, AnimeMedia, Comments


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'


class AnimeMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeMedia
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
