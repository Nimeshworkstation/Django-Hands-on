# Generated by Django 3.2.12 on 2022-04-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('roll', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=70)),
                ('marks', models.IntegerField()),
                ('pass_date', models.DateField()),
            ],
        ),
    ]
