# -*- coding: utf-8 -*-
# @Date    : 2017-05-30 11:30:40
# @Author  : 郑斌 (rjguanwen001@163.com)

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version:' + str(v))
