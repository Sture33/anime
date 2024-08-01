from django import forms
from taggit.forms import TagWidget
from taggit.models import Tag

from anime_app.models import Anime, AnimeMedia, Comments


class SearchForm(forms.Form):
    query = forms.CharField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['body']

        widgets = {'body': forms.Textarea()}
