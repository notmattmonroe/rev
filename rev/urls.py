from django.conf.urls import include, url
from django.views.generic import TemplateView, RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/blog/')),
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    #(r'^search/', include('haystack.urls')),
    url(r'^blog/', include('rev.blog.urls')),
    #url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^projects/', include('rev.project.urls')),
    url(r'^reviews/', include('rev.review.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
#from django.conf.urls import include, url
#from django.contrib import admin

#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#]
