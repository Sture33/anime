# Generated by Django 5.0.3 on 2024-06-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_app', '0006_remove_animemedia_voice_acting_delete_voiceacting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
