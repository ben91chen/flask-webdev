from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Web World"

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
    return f"Hello, {username}"

@app.route('/user/<name>/<age>')
def two_variable(name,age):
    return f"Hello, your name is <em>{name}</em> and you are <b>{age}</b> years old."

@app.route('/squared/<int:num>')
def number(num):
    return str(num**2)
