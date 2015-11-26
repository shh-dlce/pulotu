# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StatisticalValue'
        db.create_table('statistics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128, db_index=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'statistics', ['StatisticalValue'])


    def backwards(self, orm):
        # Deleting model 'StatisticalValue'
        db.delete_table('statistics')


    models = {
        u'statistics.statisticalvalue': {
            'Meta': {'object_name': 'StatisticalValue', 'db_table': "'statistics'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['statistics']