from flask import render_template
from app.auth.forms import LoginForm
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.context_processor
def inject_login_form():
    form = LoginForm()
    return dict(login_form=form)