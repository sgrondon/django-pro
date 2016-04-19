from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = [

        url(r'^$', views.PostList.as_view(), name='post_list'),
        url(r'^post/new/$', views.PostCreate.as_view(),  name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'),
        url(r'^post/(?P<pk>[0-9]+)/edit$', views.PostEdit.as_view(), name='post_edit'),
 		url(r'^post/(?P<pk>[0-9]+)/delete$', views.PostDelete.as_view(), name='post_delete'),
 		url(r'^comment/(?P<pk>[0-9]+)/like$', views.comment_like, name='comment_like'),
 		url(r'^comment/(?P<pk>[0-9]+)/dislike$', views.comment_dislike, name='comment_dislike'),
 ]