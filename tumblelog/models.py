# -*- coding: utf-8 -*-
import datetime
from flask import url_for
from tumblelog import db


class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name=u"Комментарий", required=True)
    author = db.StringField(verbose_name=u"Имя", max_length=255, required=True)

class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    tag = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('post', kwargs={"tag": self.tag})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'tag'],
        'ordering': ['-created_at']
    }


