# -*- coding: utf-8 -*-
# @Date    : 2017-05-30 10:52:43
# @Author  : 郑斌 (rjguanwen001@163.com)

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path


db.create_all()

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
	api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
	api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
	api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, 
						api.version(SQLALCHEMY_MIGRATE_REPO))