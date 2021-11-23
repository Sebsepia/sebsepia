from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils.text import slugify
from django.utils.html import mark_safe
from taggit.managers import TaggableManager
import markdown

from colorfield.fields import ColorField



class BlogImage(models.Model):
    b_img = models.ImageField('Blog Image', null=True, blank=True, upload_to="img/b")
    b_img_alt = models.CharField(max_length=255, blank=True, null=True)
    b_img_description = models.CharField(max_length=255, blank=True, null=True)
    b_img_paragraph = models.TextField(blank=True, null=True)
    postimg = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.b_img.name

    def save(self, **kwargs):
        self.b_img_date = datetime.now()
        super(BlogImage, self).save()

class PanoImage(models.Model):
    p_img = models.ImageField("Panorama Image", null=True, blank=True, upload_to="img/p")
    p_img_description = models.CharField(max_length=255, blank=True, null=True)
    p_img_paragraph = models.TextField(blank=True, null=True)
    postpanoimg = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.p_img.name

class Post(models.Model):
    post_date = models.DateField(auto_now_add=False,blank=True, null = True)
    slug = models.SlugField(unique=True, max_length=100,blank=True, null = True)
    tags = TaggableManager(blank=True)
    title = models.CharField(max_length=100, unique=True)
    title_tag = models.CharField(max_length=100, blank=True, null = True)
    portfolio_category = models.ForeignKey('PortfolioCategory', on_delete=models.SET_NULL, blank=True, null=True)
    sketchbook_category = models.ForeignKey('SketchbookCategory', on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):


        if not self.post_date:
            self.post_date = datetime.now()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse('home.html', args=(str(self.id)) )
        return reverse('home')

class PortfolioCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Portfolio Category'
        verbose_name_plural = 'Portfolio Categories'

    def __str__(self):
        return self.category_name

class SketchbookCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    cover_img = models.ImageField('Blog Image', null=True, blank=True, upload_to="img/sketchbookCover")
    class Meta:
        verbose_name = 'Sketchbook Category'
        verbose_name_plural = 'Sketchbook Categories'

    def __str__(self):
        return self.category_name
