# Generated by Django 3.2 on 2022-06-28 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_song_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
    ]
