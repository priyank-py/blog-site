# Generated by Django 2.2.8 on 2019-12-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20191218_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default='i have to update this', verbose_name='Content'),
            preserve_default=False,
        ),
    ]