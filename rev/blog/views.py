import datetime
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views import generic

from .models import Post
from .forms import PostSearchForm

def postsearch(request):
    form = PostSearchForm(request.GET)
    posts = form.search()
    return render_to_response('posts.html', {'posts': posts})

class BasePostView(object):
    date_field = 'publish'
    model = Post
class PostArchiveIndex(BasePostView, generic.ArchiveIndexView):
    paginate_by = 5

    
class PostArchiveYear(BasePostView, generic.YearArchiveView):
    make_object_list = True


class PostArchiveMonth(BasePostView, generic.MonthArchiveView):
    pass


class PostArchiveDay(BasePostView, generic.DayArchiveView):
    pass


class PostDetail(BasePostView, generic.DateDetailView):
    pass