from django.urls import path, include
from . import views
from zblog.views import Home, Details, Tagged

urlpatterns = [
    path('tag/<str:slug>/', views.tagged, name='post_by_tag'),
    path('', Home.as_view(), name='home'),
    path('nsfw', views.nsfw_view, name='nsfw'),
    path('contact', views.contact_view, name='contact'),
    path('info', views.info_view, name='info'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('<slug:slug>/', Details.as_view(), name='details'),
#    path('tag/<slug:slug>', Tagged.as_view(), name='tags')
#    path('', views.home_view, name="home"),
#    path('<str:slug>', views.detail_view, name='details'),


]
