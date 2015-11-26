# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        editor = orm['auth.User'].objects.all()[0]
        Section = orm['core.Section']
        
        q = orm.Question.objects.create(
            section=Section.objects.get(slug='physical-environment'),
            number=2,
            question='Estimated Yearly Rainfall (mm)',
            information='If the culture occupies a number of islands with a large difference in rainfall, use an average and provide details in the note section',
            editor=editor
        )
        q.save()

        q = orm.Question.objects.create(
            section=Section.objects.get(slug='physical-environment'),
            number=51,
            question='Distance to Nearest Active Volcano (km) (if within 1000km)',
            information='Please check multiple sources, as not all databases contain all active volcanos',
            editor=editor
        )
        q.save()

        q = orm.Question.objects.create(
            section=Section.objects.get(slug='social-environment'),
            number=51,
            question='Estimate of culture population size at contact',
            information='',
            editor=editor
        )
        q.save()

    
    def backwards(self, orm):
        "Write your backwards methods here."
        orm.Question.objects.delete()
        
        
    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.culture': {
            'Meta': {'ordering': "['culture']", 'object_name': 'Culture', 'db_table': "'cultures'"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'culture': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Language']", 'symmetrical': 'False', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
        },
        u'core.language': {
            'Meta': {'ordering': "['language']", 'unique_together': "(('isocode', 'language'),)", 'object_name': 'Language', 'db_table': "'languages'"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'classification': ('django.db.models.fields.TextField', [], {}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isocode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3', 'db_index': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'core.section': {
            'Meta': {'ordering': "['section']", 'object_name': 'Section', 'db_table': "'sections'"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'core.source': {
            'Meta': {'ordering': "['author', 'year']", 'unique_together': "(['author', 'year'],)", 'object_name': 'Source', 'db_table': "'sources'", 'index_together': "[['author', 'year']]"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'bibtex': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'}),
            'year': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'survey.floatresponse': {
            'Meta': {'object_name': 'FloatResponse', 'db_table': "'responses_floats'", '_ormbases': [u'survey.Response']},
            'response': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'response_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['survey.Response']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'survey.integerresponse': {
            'Meta': {'object_name': 'IntegerResponse', 'db_table': "'responses_integers'", '_ormbases': [u'survey.Response']},
            'response': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'response_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['survey.Response']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'survey.question': {
            'Meta': {'object_name': 'Question', 'db_table': "'questions'"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.TextField', [], {}),
            'number': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Section']"})
        },
        u'survey.response': {
            'Meta': {'object_name': 'Response', 'db_table': "'responses'"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'culture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Culture']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_survey.response_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.Question']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Source']"})
        },
        u'survey.textresponse': {
            'Meta': {'object_name': 'TextResponse', 'db_table': "'responses_texts'", '_ormbases': [u'survey.Response']},
            'response': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'response_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['survey.Response']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['core', 'auth', 'survey']
    symmetrical = True