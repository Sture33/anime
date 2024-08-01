from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from main.api.v1 import views

urlpatterns = [
    path('', views.AnimeListView.as_view(), name='anime'),
    path('hello/', views.HelloWorldView.as_view(), name='hello-world'),
    path('anime/<int:id>/', views.AnimeMediaListView.as_view(), name='anime_series'),
    path('anime_create/', views.AnimeCreateView.as_view(), name='anime_create'),
    path('anime_media_create/', views.AnimeMediaCreateView.as_view(), name='anime_media_create'),
    path('voice_acting_create/', views.VoiceActingCreateView.as_view(), name='voice_acting_create'),
    path('comment_create/', views.VoiceActingCreateView.as_view(), name='comment_create'),
    path('anime_update/<slug:slug>/', views.HelloWorldView.as_view(), name='anime_update'),
    path('anime_media_update/<slug:slug>/', views.HelloWorldView.as_view(), name='anime_media_update'),
    path('voice_acting_update/<slug:slug>/', views.HelloWorldView.as_view(), name='voice_acting_update'),
    path('comment_update/<int:id>/', views.HelloWorldView.as_view(), name='comment_update'),

    path('accounts/', include('accounts.api.v1.urls')),
]
