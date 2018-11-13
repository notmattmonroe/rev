from django.conf.urls import  url
from .views import *

urlpatterns =[ 
      #url(r'^$', IndexView.as_view(), name='index'),
      #url(r'^(?P<slug>[-\w\d]+)/$',  PostDetailView.as_view(),name='post',),
              url(r'^$',
                                 PostArchiveIndex.as_view(),
                                 name='blog_post_archive_index'),
                             url(r'^(?P<year>\d{4})/$',
                                 PostArchiveYear.as_view(),
                                 name='blog_post_archive_year'),
                             url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
                                 PostArchiveMonth.as_view(),
                                 name='blog_post_archive_month'),
                             url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
                                 PostArchiveDay.as_view(),
                                 name='blog_post_archive_day'),
                             url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[\w\-]+)/$',
                                 PostDetail.as_view(),
                                 name='blog_post_detail'),
]
