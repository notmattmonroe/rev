from django.db import models
import datetime

class ReviewType(models.Model):
    title = models.CharField(max_length=100)
    def __unicode__(self):
        return self.title

class RatingKey(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(
		'Attach Image',
		upload_to='postimgs',
		blank=True)
    value = models.IntegerField()
    def __unicode__(self):
        return self.title

class Artist(models.Model):
    artist = models.CharField('Artist Name', max_length=200)
    
    def __unicode__(self):
        return self.artist

class Review(models.Model):
    title = models.CharField('Title', max_length=100)
    artist = models.ForeignKey(Artist)
    slug = models.CharField('slug', max_length=100)
    date = models.DateTimeField('Date', default=datetime.datetime.now)
    enable_comments = models.BooleanField(default=True)
    image = models.ImageField(
		'Attach Image',
		upload_to='postimgs',
		blank=True)
    reviewtype = models.ForeignKey(ReviewType)
    body = models.TextField()
    is_public = models.BooleanField(default=True)
    rating = models.IntegerField(default=3)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        #return "%s/%s/" % (self.date.strftime("%Y/%b/%d").lower(), self.slug)
        return self.slug

        
