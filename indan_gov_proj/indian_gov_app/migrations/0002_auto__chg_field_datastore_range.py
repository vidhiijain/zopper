# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'DataStore.range'
        db.alter_column(u'indian_gov_app_datastore', 'range', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'DataStore.range'
        db.alter_column(u'indian_gov_app_datastore', 'range', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

    models = {
        u'indian_gov_app.csvdata': {
            'Meta': {'object_name': 'CsvData'},
            'file': ('indian_gov_app.helpers.MyFileField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'indian_gov_app.datastore': {
            'Meta': {'object_name': 'DataStore'},
            'device_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'field_of_view': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'magnification': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'range': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['indian_gov_app']