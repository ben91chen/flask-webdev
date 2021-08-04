from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "keep it secret, keep it safe"
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

basedir = os.path.abspath(os.path.dirname(__file__))

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return f"<Role {self.name}>"


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __repr__(self):
        return f"<User {self.username}>"

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

@app.route('/about')
def about_us():
    return '<p>My name is Ben, I want to be a flask developer.</p>'

@app.route('/favfood')
def favfood():
    return "<h3>My favorite food is...</h3> <li><em>pizza</em></li> <li><strong>chinese food</strong></li><li>fried chicken</li>"

@app.route('/link')
def links():
    return '''<a href="http://localhost:5000/about">Visit My About Page</a>
    <br>
    <a href="http://localhost:5000/favfood">Visit My Fav Food Page</a>'''

@app.route('/user/<username>')
def user(username):
    return render_template('user.html',username=username)

@app.route('/user/<name>/<age>')
def two_variable(name,age):
    return f"Hello, your name is <em>{name}</em> and you are <b>{age}</b> years old."

@app.route('/squared/<int:num>')
def number(num):
    return str(num**2)

@app.route('/derived')
def derived():
    return render_template('derived.html')