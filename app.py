from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import uuid

from forms.login import *
from forms.register import *



app = Flask(__name__)
app.config['SECRET_KEY'] = "Thisissupposedtobehidden!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/praful/Desktop/News/database.db'
Bootstrap(app)


db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view  = 'login'

from models.user import *

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return '<h1>Home Page Visible to everyone</h1>'

@app.route('/login', methods=['GET',"POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print('Yes!')
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
        return '<h1>Invalid Email or Password</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET',"POST"])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(email=form.email.data, password=hashed_password, public_id = str(uuid.uuid4()))
        db.session.add(new_user)
        db.session.commit()
        return '<h1>New User has been created</h1>'
    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return '<h1>dashboard PAge Visible to only logged in Users</h1>'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
