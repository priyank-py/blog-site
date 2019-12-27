# Generated by Django 2.2.8 on 2019-12-27 11:50

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Keywords'),
        ),
    ]