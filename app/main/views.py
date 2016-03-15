from flask import render_template, flash, url_for, request, redirect
from flask.ext.login import login_user

from app.models import User
from manage import app
from app.auth.forms import LoginForm
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    # print("test1")
    # form = LoginForm()
    # print(form.errors)
    # if form.is_submitted():
    #     print("submitted")
    # if form.validate():
    #     print("valid")
    # print(form.errors)
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user is not None and user.verify_password(form.password.data):
    #         login_user(user, form.remember_me.data)
    #         return redirect(request.args.get('next') or url_for('main.index'))
    #     flash('用户名或密码不正确.')
    return render_template('index.html')


@main.context_processor
def inject_login_form():
    form = LoginForm()
    return dict(login_form=form)