"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.urls import include, path
from django.conf.urls import url, include
from rest_framework import routers
from project import views
from project.views import *


router = routers.DefaultRouter()
# router.register(r'groups', views.GroupViewSet)
router.register(r'article', views.ArticleViewSet, base_name='article')
router.register(r'album', views.AlbumViewSet, base_name='album')


urlpatterns = [
    url('', include(router.urls)),
    url('album/', views.AlbumViewSet.as_view({'get': 'list'})),
    url(r'^artcle/(?P<search_text>[\w|\W]+)/$', views.ArticleViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'delete': 'destroy',
}), name='article-detail'),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

