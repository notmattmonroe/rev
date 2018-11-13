from django.db import models
from django.contrib.auth.models import User

class chore(models.Model):
    chorename = models.CharField(max_length=135, blank=True)
    choredescription = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return u'%s' % (self.chorename)
    class Meta:
        db_table = u'chore'
        ordering = ['chorename']

class chore_user(models.Model):
    username = models.ForeignKey(User)
    chorename = models.ForeignKey(chore) 
    date = models.DateTimeField()	
    class Meta:
        db_table = u'chore_user'
        ordering = ['username','date', 'chorename']


class rule(models.Model):
    rulename = models.CharField(max_length=135, blank=True)
    ruledescription = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return u'%s' % (self.name)
    class Meta:
        db_table = u'rule'
        ordering = ['rulename']

class rule_user(models.Model):
    username= models.ForeignKey(User)
    rulename= models.ForeignKey(rule)
    date = models.DateTimeField()

    class Meta:
        db_table = u'rule_user'
        ordering = ['rulename','date','username']
