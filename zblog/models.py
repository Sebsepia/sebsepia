from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils.text import slugify
from django.utils.html import mark_safe
from taggit.managers import TaggableManager
#import uuid
import markdown

from colorfield.fields import ColorField



class BlogImage(models.Model):
    b_img = models.ImageField('Blog Image', null=True, blank=True, upload_to="img/b")
    postimg = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.b_img.name

    def save(self, **kwargs):
        self.b_img_date = datetime.now()
        super(BlogImage, self).save()

class PanoImage(models.Model):
    p_img = models.ImageField("Panorama Image", null=True, blank=True, upload_to="img/p")
    postpanoimg = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.p_img.name

class Post(models.Model):
    post_date = models.DateField(auto_now_add=False,blank=True, null = True)
    slug = models.SlugField(unique=True, max_length=100,blank=True, null = True)
    talkshit = models.TextField(blank=True, null = True)
    talkshit_md = models.TextField(blank=True, null = True)


    tags = TaggableManager(blank=True)
    title = models.CharField(max_length=100, unique=True)
    title_tag = models.CharField(max_length=100, blank=True, null = True)
    portfolio_category = models.ForeignKey('PortfolioCategory', on_delete=models.SET_NULL, blank=True, null=True)
    sketchbook_category = models.ForeignKey('SketchbookCategory', on_delete=models.SET_NULL, blank=True, null=True)

    def get_talkshit_as_markdown(self):
        return mark_safe(markdown(self.talkshit, safe_mode='escape'))

    def save(self, *args, **kwargs):
        media_path = "/media/img/b/"
        pano_path = "/media/img/p/"
        self.slug = slugify(self.title)
        self.title_tag = self.title
        #convert markdown to HTML in .talkshit_md while keeping pure markdown text in .talkshit
        md = markdown.Markdown()
        text1 = self.talkshit
        text1 = text1.replace("<panorama>", "<div class='pano-image'></div>")
        text1 = text1.replace("](..", "]("+media_path)
        html1 = md.convert(text1)
        self.talkshit_md = html1

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
    #ok mais wtf!!!!
    class Meta:
        verbose_name = 'Sketchbook Category'
        verbose_name_plural = 'Sketchbook Categories'

    def __str__(self):
        return self.category_name
