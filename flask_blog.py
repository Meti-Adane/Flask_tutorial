from flask import Flask, render_template, url_for, redirect, flash
from forms import RegisterationForm, LoginForm;
app = Flask(__name__)
app.config['SECRET_KEY'] = 'f38562b513d05c4a9e68ba32d2f7ca69'
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
def m():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('hello'))
    if form.is_submitted() and not form.validate_on_submit():
        flash(f'Invalid input', 'danger')
    return render_template('signup.html', title="Register", form = form)
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="login", form = form)
 
if __name__ == '__main__':
    app.run(debug=True)