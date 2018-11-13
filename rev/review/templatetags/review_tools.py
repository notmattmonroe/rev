from django import template
from django.db import connection, transaction
from rev.review.models import Artist, Review

register = template.Library()

@register.inclusion_tag('review/artist_list.html')
def artist_list():
#    artists = Artist.objects.all()
#    return {'artists': artists}
    reviews = Review.objects.all()
    return {'reviews': reviews}
