# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

SECTION_LIST = [
    ("Physical Environment", 'physical-environment'),
    ("Indigenous State", 'indigenous-state'),
    ("Supernatural Practices", 'supernatural-practices'),
    ("Social Environment", 'social-environment'),
    ("Economic Environment", 'economic-environment'),
    ('Religious Institutional Structure', 'religious-institutional-structure'),
    ("Current State of Culture", 'current-state'),
]

SECTION_NOTES = {
    'indigenous-state': 
    """
    General Coding Guide For Indigenous State
    The indigenous state coding sheet should ideally describe the culture as it was immediately prior to contact with Western (i.e. European and European-derived) culture.  For the purposes of this database, only contact involving cultural exchange should be considered. A one-off visit from a European explorer would not constitute contact for our purposes, but regular visits from and / or trade with Europeans would. Contact with other outside cultures need not be considered except for questions 49 and 50. 
    
    Absent or Missing Data
    
    It is not always clear whether a cultural feature should be coded as “absent” or  “missing data”. Ethnographers are more likely to talk about the features of a culture that are present, rather than systematically list the features that are absent. For this reason, if there is a fair amount of information related to a feature but no mention of the feature itself, the feature should be coded as “absent” rather than “missing data”. 
    If information regarding the feature is incomplete or ambiguous, use your discretion in deciding whether the item should be coded “absent” or “missing data”. If you have limited confidence in your decision, please mark the item with an asterisk and state the reason for your uncertainty in the “coder’s notes” section. 
    
    """,
    'social-environment': 
    """
    NOTE: For the purpose of this database, a local community is a group in which people have face-to-face contact on a daily basis, e.g. village, homestead, farm. A society is a group consisting of people who share the same culture, and often consists of many communities. 
    """,
}



class Migration(DataMigration):

    def forwards(self, orm):
        editor = orm['auth.user'].objects.all()[0]
        Section = orm['core.Section']
        for sec in SECTION_LIST:
            s = Section.objects.create(
                section=sec[0],
                slug=sec[1],
                notes=SECTION_NOTES.get(sec[1], ""),
                editor=editor,
            )
            s.save()


    def backwards(self, orm):
        "Write your backwards methods here."

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
        u'core.language': {
            'Meta': {'ordering': "['language']", 'unique_together': "(('isocode', 'language'),)", 'object_name': 'Language', 'db_table': "'languages'"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'classification': ('django.db.models.fields.TextField', [], {}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isocode': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_index': 'True'}),
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
            'Meta': {'ordering': "['author', 'year']", 'object_name': 'Source', 'db_table': "'sources'", 'index_together': "[['author', 'year']]"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'bibtex': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'}),
            'year': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
    symmetrical = True
