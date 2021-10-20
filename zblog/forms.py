from django import forms
from .models import Post
from taggit.models import Tag
from taggit.forms import *

class PostForm2(forms.ModelForm):

    class Meta:
        model = Post
        fields = 'title', 'talkshit', 'tags', 'post_date'#, 'bg_r', 'bg_g', 'bg_b', 'bg_color'



    class Meta:
        model = Post
        fields = ('title', 'tags',)
        widgets = {
            'tags': TagWidget(),}
#        exclude = ['title_tag', 'blog_image_alt', 'slug']
