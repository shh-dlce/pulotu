# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Response.page'
        db.delete_column('responses', 'page')


    def backwards(self, orm):
        # Adding field 'Response.page'
        db.add_column('responses', 'page',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
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
            'coder': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'culture': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'fact': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Language']", 'symmetrical': 'False', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
        },
        u'core.language': {
            'Meta': {'ordering': "['language']", 'unique_together': "(('isocode', 'language'),)", 'object_name': 'Language', 'db_table': "'languages'"},
            'abvdcode': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'classification': ('django.db.models.fields.TextField', [], {}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isocode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3', 'db_index': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'core.section': {
            'Meta': {'ordering': "['id']", 'object_name': 'Section', 'db_table': "'sections'"},
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '1000'}),
            'year': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'})
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
        u'survey.optionquestion': {
            'Meta': {'object_name': 'OptionQuestion', 'db_table': "'questions_option'", '_ormbases': [u'survey.Question']},
            'options': ('django.db.models.fields.TextField', [], {}),
            u'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['survey.Question']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'survey.optionresponse': {
            'Meta': {'object_name': 'OptionResponse', 'db_table': "'responses_options'", '_ormbases': [u'survey.Response']},
            'response': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            u'response_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['survey.Response']", 'unique': 'True', 'primary_key': 'True'}),
            'response_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'survey.question': {
            'Meta': {'object_name': 'Question', 'db_table': "'questions'"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_survey.question_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'question': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'response_type': ('django.db.models.fields.CharField', [], {'default': "'Int'", 'max_length': '6'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Section']"})
        },
        u'survey.response': {
            'Meta': {'unique_together': "(('question', 'culture'),)", 'object_name': 'Response', 'db_table': "'responses'"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'codersnotes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'culture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Culture']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'missing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_survey.response_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.Question']"}),
            'source': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sources_info'", 'symmetrical': 'False', 'to': u"orm['core.Source']"}),
            'uncertainty': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'survey.textresponse': {
            'Meta': {'object_name': 'TextResponse', 'db_table': "'responses_texts'", '_ormbases': [u'survey.Response']},
            'response': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'response_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['survey.Response']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['survey']