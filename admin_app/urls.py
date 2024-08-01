from django.urls import path

from admin_app.views import AnimeCreateView, AnimeUpdateView, AnimeMediaUpdateView, AnimeMediaCreateView

urlpatterns = [
    path('create/anime/', AnimeCreateView.as_view(), name='anime_create'),
    path('create/anime_media', AnimeMediaCreateView.as_view(), name='anime_media_create'),
    path('update/<slug:slug>/anime', AnimeUpdateView.as_view(), name='anime_update'),
    path('update/<slug:anm_slug>/anime_media', AnimeMediaUpdateView.as_view(), name='anime_media_update'),
    path('delete/<slug:slug>/anime', AnimeUpdateView.as_view(), name='anime_delete'),
    path('delete/<slug:anm_slug>/anime_media', AnimeMediaUpdateView.as_view(), name='anime_media_delete'),
]
