from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, RedirectView
from .models import Post, BlogImage, FreeImage
from django.utils.text import slugify
from datetime import datetime, date

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown

def home_view(request):
    posts = Post.objects.exclude(tags__name="nsfw").order_by('-id')
    #posts = Post.objects.order_by('-id')
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {
    'page_obj': page_obj,
    'posts': posts,
    }
    return render(request, 'home.html', context)

class HomeRedirectView(RedirectView):
    pattern_name = 'redirect-to-blog'
    def get_redirect_url(self, *args, **kwargs):
        return '/blog'

def detail_view(request, slug):
    md = markdown.Markdown()
    post = get_object_or_404(Post, slug=slug)
#    postcontent = md.convert(post.talkshit)
    context = {
        'post':post,
#        'postcontent':postcontent,
    }
    return render(request, 'details.html', context)

def info_view(request):
    context = {}
    return render(request, 'info.html', context)

def contact_view(request):
    context = {}
    return render(request, 'contact.html', context)

def tagged(request, slug):
    posts = Post.objects.filter(tags__name__in=[slug]).order_by('-id')
    freeimgs = FreeImage.objects.all()
    context = {
        'posts':posts,
        'freeimgs' :freeimgs,
    }
    return render(request, 'tag.html', context)

def portfolio(request):
    portfolio_catalog = ('test', )
    posts = Post.objects.filter(tags__name__in=portfolio_catalog)
    freeimgs = FreeImage.objects.all()
    context = {
        'posts':posts,
        'freeimgs' :freeimgs,
        'portfolio_catalog': portfolio_catalog,
    }
    return render(request, 'portfolio.html', context)

def nsfw_view(request):
    posts = Post.objects.filter(tags__name="nsfw").order_by('-id')
    freeimgs = FreeImage.objects.all()
    context = {
    'posts':posts,
    'freeimgs' :freeimgs,
    }
    return render(request, 'nsfw.html', context)
