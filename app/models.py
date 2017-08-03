# -*- coding: utf-8 -*-
# @Date    : 2017-05-30 10:45:26
# @Author  : 郑斌 (rjguanwen001@163.com)

from hashlib import md5

from app import db
from app import app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    # @property
 #    def password(self):
 #        raise AttributeError('password is not a readable attribute')
        
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id) # python 2
        except NameError:
            return str(self.id) # python 3

    # The __repr__ method tells Python how to print objects of this class
    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def avatar(self, size):
        return "http://www.gravatar.com/avatar/%s?d=mm&s=%d"  %  (md5(self.email.encode('utf-8')).hexdigest(), size)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
