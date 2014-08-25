# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tarea.color_prioridad'
        db.add_column(u'tareas_tarea', 'color_prioridad',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Tarea.color_prioridad'
        db.delete_column(u'tareas_tarea', 'color_prioridad')


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
        u'comentarios.comentario': {
            'Meta': {'object_name': 'Comentario'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuarios.Usuario']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tareas.tarea': {
            'Meta': {'ordering': "['-numero_prioridad']", 'object_name': 'Tarea'},
            'asignada': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Asignada'", 'to': u"orm['usuarios.Usuario']"}),
            'color_prioridad': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'comentarios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['comentarios.Comentario']", 'symmetrical': 'False'}),
            'creada': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Creada'", 'to': u"orm['usuarios.Usuario']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_prioridad': ('django.db.models.fields.SmallIntegerField', [], {}),
            'prioridad': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'usuarios.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'es_directivo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'es_programador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'es_usuario': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['tareas']