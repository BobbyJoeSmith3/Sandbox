'''
The views are the handlers that respond to requests from web browsers or other clients. In Flask handlers are written as Python functions. Each view function is mapped to one or more request URLs.
'''
#import render_template method invoking jinja2 templating engine
from flask import render_template
from app import app

'''
The two route decorators above the function create the mappings from URLs '/' and '/index' to the function returning Hello, World!
'''
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
