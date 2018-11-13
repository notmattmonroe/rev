# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'chore'
        db.create_table(u'chore', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chorename', self.gf('django.db.models.fields.CharField')(max_length=135, blank=True)),
            ('choredescription', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('chorechart', ['chore'])

        # Adding model 'chore_user'
        db.create_table(u'chore_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('chorename', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chorechart.chore'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('chorechart', ['chore_user'])

        # Adding model 'rule'
        db.create_table(u'rule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rulename', self.gf('django.db.models.fields.CharField')(max_length=135, blank=True)),
            ('ruledescription', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('chorechart', ['rule'])

        # Adding model 'rule_user'
        db.create_table(u'rule_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('rulename', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chorechart.rule'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('chorechart', ['rule_user'])


    def backwards(self, orm):
        # Deleting model 'chore'
        db.delete_table(u'chore')

        # Deleting model 'chore_user'
        db.delete_table(u'chore_user')

        # Deleting model 'rule'
        db.delete_table(u'rule')

        # Deleting model 'rule_user'
        db.delete_table(u'rule_user')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'chorechart.chore': {
            'Meta': {'ordering': "['chorename']", 'object_name': 'chore', 'db_table': "u'chore'"},
            'choredescription': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chorename': ('django.db.models.fields.CharField', [], {'max_length': '135', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'chorechart.chore_user': {
            'Meta': {'ordering': "['username', 'date', 'chorename']", 'object_name': 'chore_user', 'db_table': "u'chore_user'"},
            'chorename': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chorechart.chore']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'chorechart.rule': {
            'Meta': {'ordering': "['rulename']", 'object_name': 'rule', 'db_table': "u'rule'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ruledescription': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rulename': ('django.db.models.fields.CharField', [], {'max_length': '135', 'blank': 'True'})
        },
        'chorechart.rule_user': {
            'Meta': {'ordering': "['rulename', 'date', 'username']", 'object_name': 'rule_user', 'db_table': "u'rule_user'"},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rulename': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chorechart.rule']"}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['chorechart']