#! /home/developer/.local/share/virtualenvs/Flask_Corey_Schafer_Project-ZtozJHVn
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0c7fbac76e940a6a79929df62124332edafb9e0717ca3691f31aa0256cbb'

posts = [
    {
        'title': 'I am a disco dancer',
        'author': 'Mithun',
        'content': 'I am a dancer and I can dance magically',
        'date_posted': 'July 7, 2019'
    },
    {
        'title': 'Expert Web Developer',
        'author': 'Shreyash',
        'content': 'I am a professional freelance web-developer with lots of experience',
        'date_posted': 'July 10, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title="Root")


@app.route('/about')
def about():
    return render_template('about.html', title="Shreyash")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)



@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':    
            flash(f'You have been logged in successfully. Welcome {form.email.data}!', category='success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check your username and password', 'danger')
    return render_template('login.html', title="login", form=form)




if __name__ == '__main__':
    app.run(debug=True)



