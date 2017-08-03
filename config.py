# -*- coding: utf-8 -*-
# @Date    : 2017-05-23 14:44:53
# @Author  : 郑斌 (rjguanwen001@163.com)

import os


WTF_CSRF_ENABLED = True
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

OPENID_PROVIDERS = [
	{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
	{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
	{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'}]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
