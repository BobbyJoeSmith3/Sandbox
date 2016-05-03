'''
The views are the handlers that respond to requests from web browsers or other clients. In Flask handlers are written as Python functions. Each view function is mapped to one or more request URLs.
'''
#import render_template method
from flask import render_template
from app import app

'''
The two route decorators above the function create the mappings from URLs '/' and '/index' to the function returning Hello, World!
'''
@app.route('/')
@app.route('/index')
def index():
  user = {'nickname': 'Miguel'} #fake user
  return render_template('index.html',
                          title='Home',
                          user=user)
