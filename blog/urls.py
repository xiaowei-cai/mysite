# ---------------- #
# coding=utf-8     #
# Author:cxw       #
# Date:2017.xx.xx  #
# ---------------- #
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_title, name='blog_title'),
    url(r'^(?P<article_id>\d)/$', views.blog_article, name='blog_detail')
]
