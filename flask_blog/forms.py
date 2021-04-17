from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_blog.modles import User


class RegisterationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=4, max=10)
                            ])

    email = StringField("Email", 
                        validators=[
                            DataRequired(), Email()
                        ])
    password = PasswordField('Password', 
                           validators=[
                               DataRequired(), Length(min=4)
                           ])
    confirmPassword = PasswordField('confirm Password', 
                                    validators=[
                                        DataRequired(), EqualTo('password')
                                    ])
    submit = SubmitField("signup")
    
    
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("This username is already taken choose a different one please!")
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("There is already an account with this email please change your email or login to your account")
class LoginForm(FlaskForm):
    
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")