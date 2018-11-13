from django.conf.urls import  url
from .views import *


urlpatterns = [ 
      url(r'^$', ReviewIndexView.as_view(), name='reviewindex'),
      url(r'^artists/$', ArtistList.as_view()),
      url(r'^artist/(?P<artist>[\w.@+-]+)/$', ArtistReviewList.as_view(), name='albumsbyartist'),
      #url(r'^artist/(\d+)/$', ArtistReviewList.as_view()),
      #url(r'^artist/(\d+)/$', albums_by_artist),
      url(r'^(?P<slug>[-\w\d]+)/$',  ReviewDetailView.as_view(),
              name='review',)
]
