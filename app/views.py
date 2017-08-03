# -*- coding: utf-8 -*-
# @Date    : 2017-06-14 14:52:34
# @Author  : 郑斌 (rjguanwen001@163.com)

import os
from flask import render_template, flash, redirect, session, url_for, request, g, abort
from flask_login import login_user, logout_user, current_user, login_required

from app import app, db, lm
from .forms import LoginForm
from .models import User



@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        user_id = form.username.data
        user = User.query.get(user_id)
        if not user:
            flash('没有该用户，请检查！')
            return render_template('login.html', 
                           title='Sign In',
                           form=form)
        # 先简单的把密码设置为'b'
        # user.password = 'b'
        password = form.password.data
        # if user.verify_password(password):
        print("=====>> password=%s" % password)
        if password != user.password:
            flash('密码错误，请重新输入！')
            return render_template('login.html', 
                           title='Sign In',
                           form=form)
        print("=====>> login_user - begin")
        login_user(user, remember=form.remember_me.data)
        print("=====>> login_user - end")
        next = request.args.get('next')
        if not next_is_valid(next):
            return abort(400)
        else:
            # flash('Login requested for OpenID="%s", remember_me=%s' %
            #       (form.openid.data, str(form.remember_me.data)))
            return redirect(next or url_for('index'))
    return render_template('login.html', 
                           title='Sign In',
                           form=form)


# 检验next
def next_is_valid(next):
    if next:
        return True
    return False


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    # 造一些文章
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                            user=user,
                            posts=posts)

