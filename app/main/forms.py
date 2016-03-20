from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from flask_wtf.file import FileField, FileAllowed
from flask.ext.uploads import UploadSet, IMAGES
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask.ext.pagedown.fields import PageDownField
from ..models import Role, User

images = UploadSet('images', IMAGES)

class EditProfileForm(Form):
    name = StringField('名字', validators=[Length(0,64)])
    location = StringField('居住地', validators=[Length(0,64)])
    about_me = TextAreaField('自我描述')
    submit = SubmitField('提交')

class EditProfileAdminForm(Form):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    username = StringField('用户名', validators=[
        Required(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名必须为字母数字点号或下划线.')
    ])
    confirmed = BooleanField('确认')
    role = SelectField('角色', coerce=int)
    name = StringField('名字', validators=[Length(0, 64)])
    location = StringField('地址', validators=[Length(0, 64)])
    about_me = TextAreaField('自我描述')
    submit = SubmitField('提交')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')

class PostForm(Form):
    body = PageDownField('分享一件新鲜事...', validators=[Required()])
    photo = FileField('上传图片', validators=[FileAllowed(images, '仅限图片')])
    submit = SubmitField('投递')

class CommentForm(Form):
    body = PageDownField('添加评论...', validators=[Required()])
    submit = SubmitField('评论')

