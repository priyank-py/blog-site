from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

GENRE_CHOICES = [
    ('adventure', 'Adventure'),
    ('fiction', 'Fiction'),
    ('non_fiction', 'Non Fiction'),
    ('technology', 'Technology'),
    ('lifestyle', 'Lifestyle'),
]

def upload_image(instance, filename):
    return f'{instance.title}/{filename}'

class Article(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    writer = models.CharField(_("Writer"), max_length=100)
    genre = models.CharField(_("Genre"), max_length=20, choices=GENRE_CHOICES)
    published_on = models.DateTimeField(_("Published on"), auto_now_add=True)
    modified_on = models.DateTimeField(_("Modified on"), auto_now=True)
    title_image = models.ImageField(_("Title Image"), upload_to=upload_image, blank=True, null=True)
    body = HTMLField(_("Content"))
    keywords = TaggableManager(verbose_name='Keywords', blank=True)
    slug = models.SlugField(_("slug"), blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.writer}')
        super(Article, self).save(*args, **kwargs)
    

