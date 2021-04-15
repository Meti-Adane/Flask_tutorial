from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
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
    
class LoginForm(FlaskForm):
    
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField("Login")