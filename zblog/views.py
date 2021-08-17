from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, RedirectView
from .models import Post, PortfolioCategory
from django.utils.text import slugify
from datetime import datetime, date

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown

def home_view(request):
    posts = Post.objects.exclude(tags__name="nsfw").order_by('-post_date', '-id')
    #posts = Post.objects.order_by('-id')
    paginator = Paginator(posts, 5)
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
    return render(request, 'details.html', context,)

def info_view(request):
    context = {}
    return render(request, 'info.html', context)

def contact_view(request):
    context = {}
    return render(request, 'contact.html', context)

def tagged(request, slug):
    exclude = ('nsfw', )
    posts = Post.objects.filter(tags__name__in=[slug]).exclude(tags__name__in=exclude).order_by('-id')
    context = {
        'posts':posts,
    }
    return render(request, 'tag.html', context)

def portfolio(request):
    categories = PortfolioCategory.objects.all().order_by('category_name')
    posts = Post.objects.exclude(tags__name="nsfw").order_by('-post_date', '-id')


    context = {
    'categories': categories,
    'posts': posts,
    }
    return render(request, 'portfolio.html', context)

def portfoliocat(request, slug):
    exclude = ('nsfw', )
    allcategories = PortfolioCategory.objects.all().order_by('category_name')
    categories = PortfolioCategory.objects.filter(category_name__in=[slug]).exclude(category_name__in=exclude).order_by('-id')
    context = {
        'categories':categories,
        'allcategories':allcategories,
    }
    return render(request, 'portfoliocat.html', context)

def shop(request):
    shop_catalog = ('objet', )
    posts = Post.objects.filter(tags__name__in=shop_catalog)
    context = {
        'posts':posts,
        'shop_catalog': shop_catalog,
    }
    return render(request, 'shop.html', context)

def nsfw_view(request):
    posts = Post.objects.filter(tags__name="nsfw").order_by('-id')
    context = {
    'posts':posts,
    }
    return render(request, 'nsfw.html', context)
