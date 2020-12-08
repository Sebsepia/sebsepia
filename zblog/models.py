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


class FreeImage(models.Model):
    f_img = models.ImageField(null=True, blank=True, upload_to="img/f")
    f_img_alt = models.CharField(max_length=100, blank=True, null=True)
    posi_X = models.IntegerField(default=800)
    posi_Y = models.IntegerField(default=0)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.f_img.name


class BlogImage(models.Model):
    b_img_date = models.DateField(auto_now_add=False,blank=True, null = True)
    b_img = models.ImageField("Blog Image", null=True, blank=True, upload_to="img/b")
    postimg = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.b_img.name

    def save(self, **kwargs):
        self.b_img_date = datetime.now()
        super(BlogImage, self).save()



class Post(models.Model):
    bg_color = ColorField(default='#FFFFFF')
    bg_color_a = models.BooleanField(default=True)
    bg_overlay_color = ColorField(default='#FFFFFF00')
    bg_overlay_check = models.BooleanField(blank=True, null = True)
    post_date = models.DateField(auto_now_add=False,blank=True, null = True)
    slug = models.SlugField(unique=True, max_length=100,blank=True, null = True)
    talkshit = models.TextField(blank=True, null = True)
    talkshit_md = models.TextField(blank=True, null = True)
    text_color = ColorField(default='#000000')
    tags = TaggableManager(blank=True)
    title = models.CharField(max_length=100, unique=True)
    title_tag = models.CharField(max_length=100, blank=True, null = True)

    def get_talkshit_as_markdown(self):
        return mark_safe(markdown(self.talkshit, safe_mode='escape'))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.title_tag = self.title
        #convert markdown to HTML in .talkshit_md while keeping pure markdown text in .talkshit
        md = markdown.Markdown()
        text1 = self.talkshit
        html1 = md.convert(text1)
        html1 = html1.replace("<p>","").replace("</p>","")
        self.talkshit_md = html1

        #ajoute un alpha a la couleur en hexadecimal si checked
        bg_color = self.bg_color
        if self.bg_color_a:
            self.bg_color = bg_color + "00"
        if not self.post_date:
            self.post_date = datetime.now()
        #check le checkbox de bg_overlay
        if not self.bg_overlay_check:
            self.bg_overlay_color= "#00000000"
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse('home.html', args=(str(self.id)) )
        return reverse('home')
