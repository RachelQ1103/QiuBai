#!/usr/bin/env python
import os
from app import create_app, db
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User, Role, Permission
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.context_processor
def inject_login_form():
    """Add LoginFrom to base.html"""
    form = LoginForm()
    return dict(login_form=form)

@app.context_processor
def inject_registration_form():
    """Add RegistrationForm to base.html"""
    form = RegistrationForm()
    return dict(registration_form=form)


if __name__ == '__main__':
    manager.run()



