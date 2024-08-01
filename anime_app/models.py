from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from taggit.managers import TaggableManager


# Create your models here.

# class Genre(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name


class Anime(models.Model):
    class Status(models.TextChoices):
        ongoing = "OG", "Ongoing"
        already_out = 'AO', 'Already Out'

    title = models.CharField(max_length=255)
    org_title = models.CharField(max_length=255)
    description = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')
    genres = TaggableManager()
    created_year = models.PositiveIntegerField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.already_out)
    user_is_rating = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    class Meta:
        ordering = ('-created_year',)
        indexes = [
            models.Index(fields=['-created_year'])
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings:
            return sum(rating.value for rating in ratings) / len(ratings)
        return 0


class AnimeMedia(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    series = models.PositiveIntegerField()
    name_of_series = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')
    add_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='anime_media_likes', blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f'{self.series, self.anime}', allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)

    def get_total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.anime.title


class Comments(models.Model):
    anime_media = models.ForeignKey(AnimeMedia, on_delete=models.CASCADE)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_updated = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)
        indexes = [models.Index(fields=['created_at'])]

    def __str__(self):
        return f"{self.user} - {self.anime_media}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.FloatField(default=0)
    anime = models.ForeignKey(Anime, related_name='ratings', on_delete=models.CASCADE)


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
