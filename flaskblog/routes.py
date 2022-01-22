from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
    {
        'author': 'Corey',
        'title': "blog1",
        'content': 'first content',
        'date_posted': 'May 22, 2022',
    },
    {
        'author': 'Jane',
        'title': "blog2",
        'content': 'Second content',
        'date_posted': 'May 22, 2022',
    }

]

@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template("home.html", posts = posts)

@app.route('/about')
def about():  # put application's code here
    return render_template("about.html", title="about")

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data =='password':
            flash('You are have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unscuccessful. please check ', 'danger')
    return render_template('login.html', title='Login', form=form)
