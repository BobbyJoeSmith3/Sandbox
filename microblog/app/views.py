'''
The views are the handlers that respond to requests from web browsers or other clients. In Flask handlers are written as Python functions. Each view function is mapped to one or more request URLs.
'''
#import render_template method invoking jinja2 templating engine
from flask import render_template, flash, redirect
from app import app
#import LoginForm() class in forms.py
from .forms import LoginForm


'''==============================================
          INDEX
=============================================='''
#The two route decorators above the function create the mappings from URLs '/' and '/index' to the function returning Hello, World!

@app.route('/')
@app.route('/index')
def index():
  user = {'nickname': 'Miguel'} #fake user
  #fake array of posts
  posts = [
    {
      'author': {'nickname': 'John'},
      'body': 'Beautiful day in Portland!'
    },
    {
      'author': {'nickname': 'Susan'},
      'body': 'The Avengers movie was so cool!'
    }
  ]
  return render_template('index.html',
                          user=user,
                          posts=posts)


'''==============================================
          LOGIN
=============================================='''
#Import LoginForm class (done above), instantiate an object from it, and send it down to the template
#Methods argument tells Flask that this view function accepts GET and POST requests. Without this, the view will only accept GET requests.
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  return render_template('login.html',
                          title='Sign In',
                          form=form)
