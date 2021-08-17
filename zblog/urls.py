from django.urls import path, include
from . import views
from .views import HomeRedirectView

urlpatterns = [
    path((''), HomeRedirectView.as_view(), name='redirect-to-blog'),
    path('blog', views.home_view, name="home"),
    path('blog/<str:slug>', views.detail_view, name='details'),
    path('tag/<str:slug>/', views.tagged, name='tag'),
    path('nsfw', views.nsfw_view, name='nsfw'),
    path('info', views.info_view, name='info'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/<str:slug>/', views.portfoliocat, name='portfoliocat'),
    path('shop', views.shop, name='shop'),
]
urlpatterns = [
    path('', include('zblog.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
