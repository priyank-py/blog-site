# Generated by Django 2.2.8 on 2019-12-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20191227_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='slug'),
        ),
    ]
