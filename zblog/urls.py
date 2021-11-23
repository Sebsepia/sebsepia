from django.urls import path, include
from . import views
from .views import HomeRedirectView


urlpatterns = [
    path((''), HomeRedirectView.as_view(), name='redirect-to-blog'),
    path('blog', views.home_view, name="home"),
    path('blog/<str:slug>', views.detail_view, name='details'),
    path('info', views.info_view, name='info'),
    path('linktree', views.linktree, name='linktree'),
    path('nsfw', views.nsfw_view, name='nsfw'),
    path('portfolio/<str:slug>/', views.portfolio, name='portfolio'),
    path('sketchbook', views.sketchbook, name='sketchbook'),
    path('tag/<str:slug>/', views.tagged, name='tag'),


]
