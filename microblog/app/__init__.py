#Creates the application object (of class Flask) and then imports the views module.
from flask import Flask

app = Flask(__name__)
#Tell Flask to read config file
app.config.from_object('config')

#import of views added at the end of the script to avoid circular reference, since views module needs to import the app variable defined above
from app import views
