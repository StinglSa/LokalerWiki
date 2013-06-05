# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Entry'
        db.create_table(u'entries_entry', (
            ('content', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('wikilink', self.gf('django.db.models.fields.CharField')(max_length=30)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'entries', ['Entry'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Entry'
        db.delete_table(u'entries_entry')
    
    
    models = {
        u'entries.entry': {
            'Meta': {'object_name': 'Entry'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'wikilink': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }
    
    complete_apps = ['entries']
