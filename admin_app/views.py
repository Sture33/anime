from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from admin_app.forms import AnimeForm, AnimeMediaForm
from anime_app.models import Anime, AnimeMedia


class AnimeCreateView(CreateView):
    model = Anime
    form_class = AnimeForm
    template_name = 'temps_for_admin/create/anime.html'
    success_url = reverse_lazy('anime_list')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect('yana')
        return super().dispatch(request, *args, **kwargs)


class AnimeMediaCreateView(CreateView):
    model = AnimeMedia
    form_class = AnimeMediaForm
    template_name = 'temps_for_admin/create/anime_media.html'
    success_url = reverse_lazy('anime_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        anime_slug = form.instance.anime.slug
        self.success_url = reverse_lazy('anime_detail', kwargs={'anm_slug': anime_slug})
        return response

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect('yana')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.success_url


class AnimeUpdateView(UpdateView):
    model = Anime
    form_class = AnimeForm
    template_name = 'temps_for_admin/update/anime.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('anime_detail')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect('yana')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('anime_detail', kwargs={'slug': self.object.slug})


class AnimeMediaUpdateView(UpdateView):
    model = AnimeMedia
    form_class = AnimeMediaForm
    template_name = 'temps_for_admin/update/anime_media.html'
    slug_field = 'slug'
    slug_url_kwarg = 'anm_slug'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect('yana')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('anime_media_detail', kwargs={'anm_slug': self.object.slug})


def anime_delete(request, slug):
    anime = Anime.objects.get(slug=slug)
    anime.delete()
    return redirect('anime_list')


def anime_media_delete(request, anm_slug):
    anime_media = AnimeMedia.objects.get(slug=anm_slug)
    anime_media.delete()
    return redirect('anime_list')
