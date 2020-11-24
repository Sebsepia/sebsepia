from django import forms
from .models import Post
from taggit.models import Tag
from taggit.forms import *

class PostForm2(forms.ModelForm):

    class Meta:
        model = Post
        fields = 'title', 'talkshit', 'tags', 'post_date'#, 'bg_r', 'bg_g', 'bg_b', 'bg_color'


class PostForm(forms.ModelForm):

#    title = forms.CharField(label=False,
#        widget = forms.TextInput(attrs={'class': 'titleinput', 'placeholder': 'title' }))
#    title_tag = forms.CharField(label=False, required=False,
#        widget = forms.TextInput(attrs={'placeholder': 'title tag'}))
#    slug = forms.CharField(label=False, required=False,
#        widget = forms.TextInput(attrs={'placeholder': 'title tag'}))

#    blog_image = forms.FileInput()
#    blog_image_alt = forms.CharField(label=False, required=False,
#        widget = forms.TextInput(attrs={'placeholder': 'image alt text'}))

#    tags = TagWidget()

#    talkshit = forms.Textarea()

#    bg_color = forms.CharField(label=False, required=False,
#        widget = forms.TextInput(attrs={'class': 'colorinput', 'placeholder': '128, 128, 128, 255' }))
#    text_color = forms.CharField(label=False,required=False,
#        widget = forms.TextInput(attrs={'class': 'colorinput', 'placeholder': '128, 128, 128, 255' }))
#    libre_image = forms.FileInput()
#    libre_image_alt = forms.CharField(label=False, required=False,
#        widget = forms.TextInput(attrs={'placeholder': 'libre image alt text'}))

#    post_date = forms.DateField(label=False, required=False,
#        widget = forms.TextInput(attrs={'class': 'time', 'placeholder': 'date' }))

    class Meta:
        model = Post
        fields = ('title', 'tags',)
        widgets = {
            'tags': TagWidget(),}
#        exclude = ['title_tag', 'blog_image_alt', 'slug']
