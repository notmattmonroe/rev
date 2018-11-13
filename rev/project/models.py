from django.db import models
import datetime

class ProjectType(models.Model):
    title = models.CharField('Title', max_length=100)
    def __unicode__(self):
        return self.title

class Project(models.Model):
    prepopulated_fields={"slug": ("title",)}
    title = models.CharField('Title', max_length=100)
    slug = models.CharField('slug', max_length=100)
    projecttype = models.ForeignKey(ProjectType)
    date = models.DateTimeField('Date', default=datetime.datetime.now)
    enable_comments = models.BooleanField(default=True)
    body = models.TextField()
    is_public = models.BooleanField();
    version = models.FloatField();
    project_file = models.FileField(upload_to='projects', null=True, blank=True)


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug
        #return "/projects/%s/%s/" % (self.date.strftime("%Y/%b/%d").lower(), self.slug)
        #return "/projects/%i" % self.id
        #return ('project.view.details', [str(self.title)])
    #get_absolute_url = permalink(get_absolute_url)

