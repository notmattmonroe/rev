import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views import generic

from .models import *

#def albums_by_artist(request, id):
#    artist = get_object_or_404(Artist, id__iexact=id)
#    return list_detail.object_list(
#        request,
#        queryset = Review.objects.filter(artist=artist),
#        template_name = 'review/albums_by_artist.html',
#        template_object_name = 'review',
#        extra_context = {'artist': artist}
#    )



class ReviewIndexView(generic.ListView):
    template_name = 'review/index.html'
    context_object_name = 'reviewindex'
    queryset = Review.objects.order_by('-date')[:5]


class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'review/detail.html'
    context_object_name  = 'review'

class ArtistList(generic.ListView):
    template_name = 'review/artist_list.html'
    context_object_name = 'artistlist'
    queryset = Artist.objects.all()

class ArtistReviewList(generic.ListView):
    template_name = 'review/albums_by_artist.html'
    context_object_name = 'albumsbyartist'
    def get_queryset(self):
        self.artist = get_object_or_404(Artist, artist=self.args[0])
        return Review.objects.filter(artist=self.artist)
