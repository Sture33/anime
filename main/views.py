from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import TrigramSimilarity
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, DetailView

from anime_app.models import Anime, AnimeMedia, Comments, Rating, Favorites
from main.forms import CommentForm, SearchForm


class AnimeListView(ListView):
    model = Anime
    template_name = 'main/temps/main.html'
    context_object_name = 'anime_list'
    paginate_by = 10


class AnimeDetailView(TemplateView):
    template_name = 'main/temps/anime_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anime_slug = self.kwargs.get('slug')
        anime = Anime.objects.get(slug=anime_slug)

        context['anime'] = anime
        context['anime_medias'] = AnimeMedia.objects.filter(anime=anime)
        context['average_rating'] = anime.get_average_rating()
        return context


class AnimeMediaDetailView(DetailView):
    model = AnimeMedia
    template_name = 'main/temps/anime_media_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'anm_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anime_media = get_object_or_404(AnimeMedia, slug=self.kwargs['anm_slug'])
        context['comments'] = Comments.objects.filter(anime_media=anime_media)
        context['form'] = CommentForm()
        context['total_likes'] = anime_media.get_total_likes()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.anime_media = self.object
            comment.user = request.user
            comment.save()
            return redirect('anime_media_detail', anm_slug=self.object.slug)
        return redirect('anime_media_detail', anm_slug=self.object.slug)


def like_anime_media(request, anm_slug):
    anime_media = get_object_or_404(AnimeMedia, slug=anm_slug)
    if request.user in anime_media.likes.all():
        anime_media.likes.remove(request.user)
    else:
        anime_media.likes.add(request.user)
    return redirect('anime_media_detail', anm_slug=anm_slug)


def rate_anime(request, slug):
    anime = get_object_or_404(Anime, slug=slug)
    if request.method == 'POST':
        rating_value = int(request.POST.get('rating'))
        rating, created = Rating.objects.get_or_create(user=request.user, anime=anime)
        anime.user_is_rating = True
        rating.value = rating_value
        anime.save()
        rating.save()
        return redirect('anime_detail', slug=slug)


def anime_search_2(request):
    form = SearchForm()
    query = None
    results = []
    page = request.GET.get('page', 1)
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Anime.objects.annotate(
                similarity=TrigramSimilarity('title', query),
            ).filter(similarity__gt=0.1).order_by('-similarity')

    paginator = Paginator(results, 10)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    return render(request, 'main/temps/search.html', {
        'form': form,
        'results': results,
        'paginator': paginator,
        'query': query,
    })

@login_required
def add_to_favorites(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    Favorites.objects.create(anime=anime, user=request.user)
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url:
        return redirect(previous_url)
    else:
        return redirect('home')




def yana(request):
    return render(request, 'main/you_are_not_admin.html')
