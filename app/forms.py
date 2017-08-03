# -*- coding: utf-8 -*-
# @Date    : 2017-05-23 14:48:49
# @Author  : 郑斌 (rjguanwen001@163.com)

from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    """登录页的Form"""
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember me', default=False)
