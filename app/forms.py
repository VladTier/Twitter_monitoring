from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(),
                                Length(min=4, max=20)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(message=None),
                    Length(min=6, max=30)]
    )
    first_name = StringField(
        'First Name', validators=[DataRequired(),
                                  Length(min=4, max=30)]
    )
    last_name = StringField(
        'Last Name', validators=[DataRequired(),
                                 Length(min=4, max=30)]
    )
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


class WordsForm(FlaskForm):
    words = StringField('Words', validators=[DataRequired()])




