from flask import render_template, url_for, redirect, flash
from flask_blog.forms import RegisterationForm, LoginForm;
from flask_blog.modles import User, Post
from flask_blog import app, bcrypt, db 
from flask_login import login_user, current_user, logout_user

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
def hello():
    return render_template('home.html', title="Meti",posts=posts)
@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('hello'))
    form = RegisterationForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username= form.username.data, email= form.email.data, password = hashed)
        db.session.add(user)
        db.session.commit()
        flash(f'Account successfully created you can now login into your account', 'success')
        return redirect(url_for('login'))
    # if form.is_submitted() and not form.validate_on_submit():
    #     flash(f'Invalid input', 'danger')
    return render_template('signup.html', title="Register", form = form)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('hello'))
        flash("login failed check your email and password", 'danger')
    return render_template('login.html', title="login", form = form)
 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('hello'))