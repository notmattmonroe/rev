from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'luke.todolist.views.index'),
    )