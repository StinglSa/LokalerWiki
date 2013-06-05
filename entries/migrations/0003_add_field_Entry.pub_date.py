# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Entry.pub_date'
        db.add_column(u'entries_entry', 'pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2013, 5, 13)), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'Entry.pub_date'
        db.delete_column(u'entries_entry', 'pub_date')
    
    
    models = {
        u'entries.entry': {
            'Meta': {'object_name': 'Entry'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'wikilink': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }
    
    complete_apps = ['entries']
