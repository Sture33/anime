from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from anime_app.models import Comments, Anime, AnimeMedia
from main.api.v1.serializers import AnimeSerializer, AnimeMediaSerializer, CommentsSerializer


class AnimeTitle(ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [IsAuthenticated]


class HelloWorldView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data={"message": "Hello, world!"}, status=200)


class AnimeListView(ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (AllowAny,)


class AnimeMediaListView(ListAPIView):
    serializer_class = AnimeMediaSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        anime_id = self.kwargs['id']
        anime = Anime.objects.get(id=anime_id)
        return AnimeMedia.objects.filter(anime=anime)


class CommentsListView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny,)


class AnimeCreateView(CreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (IsAdminUser,)


class AnimeMediaCreateView(CreateAPIView):
    queryset = AnimeMedia.objects.all()
    serializer_class = AnimeMediaSerializer
    permission_classes = (IsAdminUser,)




class CommentsCreateView(CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)


class AnimeUpdateView(UpdateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (IsAdminUser,)


class VoiceActingUpdateView(UpdateAPIView):
    queryset = VoiceActing.objects.all()
    serializer_class = VoiceActingSerializer
    permission_classes = (IsAdminUser,)


class AnimeMediaUpdateView(UpdateAPIView):
    queryset = AnimeMedia.objects.all()
    serializer_class = AnimeMediaSerializer
    permission_classes = (IsAdminUser,)


class CommentsUpdateView(UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)
