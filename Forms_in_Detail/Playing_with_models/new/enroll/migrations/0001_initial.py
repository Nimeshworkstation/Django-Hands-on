# Generated by Django 3.2.12 on 2022-03-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=70)),
                ('studemail', models.EmailField(max_length=70)),
                ('stupass', models.CharField(max_length=70)),
            ],
        ),
    ]
