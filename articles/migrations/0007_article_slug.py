# Generated by Django 2.2.8 on 2019-12-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20191227_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='slug'),
        ),
    ]
