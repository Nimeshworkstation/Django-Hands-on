# Generated by Django 3.2.12 on 2022-04-19 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('page_name', models.CharField(max_length=70)),
                ('page_cat', models.CharField(max_length=70)),
                ('page_publish', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('panna', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.page')),
                ('likes', models.IntegerField()),
            ],
            bases=('myapp.page',),
        ),
    ]
