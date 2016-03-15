from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms.validators import ValidationError
from ..models import User


class LoginForm(Form):
    email = StringField('邮箱', validators=[Required(), Length(1,64), Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

class RegistrationForm(Form):
    email = StringField('邮箱', validators=[Required(), Length(1,64), Email()])
    username = StringField('用户名', validators=[Required(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                               '用户名只能包含字母数字点号或下划线')])
    password = PasswordField('密码', validators=[
        Required(), EqualTo('password2', message='密码必须一致')
    ])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在.')
