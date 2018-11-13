from django.conf.urls import  url
from .views import *

urlpatterns = [ 
      url(r'^$', ProjectIndexView.as_view(), name='projectindex'),
      url(r'^(?P<slug>[-\w\d]+)/$',  ProjectDetailView.as_view(),
              name='project',),
]
