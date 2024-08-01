# Generated by Django 5.0.3 on 2024-05-22 09:39

import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('org_title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('published_year', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('OG', 'Ongoing'), ('AO', 'Already Out')], default='AO', max_length=2)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('genres', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-published_year',),
            },
        ),
        migrations.CreateModel(
            name='AnimeMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.PositiveIntegerField()),
                ('name_of_series', models.CharField(max_length=255)),
                ('video', models.FileField(upload_to='videos/')),
                ('add_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime_app.anime')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.BooleanField(default=False)),
                ('anime_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime_app.animemedia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='VoiceActing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('anime', models.ManyToManyField(to='anime_app.anime')),
            ],
        ),
        migrations.AddField(
            model_name='animemedia',
            name='voice_acting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime_app.voiceacting'),
        ),
        migrations.AddIndex(
            model_name='anime',
            index=models.Index(fields=['-published_year'], name='anime_app_a_publish_eb5a36_idx'),
        ),
        migrations.AddIndex(
            model_name='comments',
            index=models.Index(fields=['created_at'], name='anime_app_c_created_a809ba_idx'),
        ),
    ]
