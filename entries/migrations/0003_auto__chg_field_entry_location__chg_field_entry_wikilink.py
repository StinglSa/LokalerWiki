# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'Entry.location'
        db.alter_column(u'entries_entry', 'location', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True))

        # Changing field 'Entry.wikilink'
        db.alter_column(u'entries_entry', 'wikilink', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True))
    
    
    def backwards(self, orm):
        
        # Changing field 'Entry.location'
        db.alter_column(u'entries_entry', 'location', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Entry.wikilink'
        db.alter_column(u'entries_entry', 'wikilink', self.gf('django.db.models.fields.CharField')(max_length=30))
    
    
    models = {
        u'entries.entry': {
            'Meta': {'object_name': 'Entry'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'wikilink': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }
    
    complete_apps = ['entries']
