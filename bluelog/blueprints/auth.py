# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import random

from flask import render_template, flash, redirect, url_for, Blueprint, request
from flask_login import login_user, logout_user, login_required, current_user

from bluelog.forms import LoginForm
from bluelog.models import Admin
from bluelog.utils import redirect_back
from bluelog.emails import send_validation_email

from bluelog.extensions import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        if form.submit.data:
            username = form.username.data
            password = form.password.data
            remember = form.remember.data
            captcha = form.captcha.data
            admin = Admin.query.first()
            if admin:
                if username == admin.username and admin.validate_password(password) and captcha == admin.captcha:
                    login_user(admin, remember)
                    flash('Welcome back.', 'info')
                    # 生成新的无效验证码
                    newCaptcha = ''.join(
                    random.sample('zyxwvutsrqponmlkjihgfedcba1234567890!@#$%&*', random.randint(7, 8)))
                    admin.captcha = newCaptcha
                    db.session.commit()
                    redirect_back()
                    return redirect_back()
                flash('Invalid username or password.', 'warning')
            else:
                flash('No account.', 'warning')
            # 生成新的无效验证码
            newCaptcha = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890!@#$%&*', random.randint(7, 8)))
            admin.captcha = newCaptcha
            db.session.commit()
        elif form.getCap.data:
            username = form.username.data
            admin = Admin.query.first()
            if username == admin.username:
                newCaptcha = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890!@#$%&*', random.randint(7, 8)))
                admin.captcha = newCaptcha
                db.session.commit()
                send_validation_email(newCaptcha)
                flash('Validation email has been sent to Your MailBox', 'info')
            else:
                flash('No account.', 'warning')
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect_back()
