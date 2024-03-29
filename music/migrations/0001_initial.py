# Generated by Django 2.2.6 on 2019-10-06 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('music_name', models.CharField(max_length=250)),
                ('music_genre', models.CharField(choices=[('P', 'Pop_Music'), ('E', 'Electronic_Dance_Music'), ('R', 'Rap_Music'), ('T', 'Trance_Music'), ('C', 'Classical_Music'), ('M', 'Mettal_Music')], max_length=1)),
                ('music_logo', models.ImageField(upload_to='')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_music', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
