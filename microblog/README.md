**CONFIGURATION**
Many Flask extensions require some amount of configuration, so we are going to setup a configuration file inside our root microblog folder so that it is easily accessible if it needs to be edited

```Python
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
  {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
  {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
  {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
  {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
  {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]
```

**LOGIN** Users will login using OpenID. OpenIDs have the benefit that the authentication is done by the provider of the OpenID, so we don't have to validate passwords, making our site more secure to our users.

A number of major service providers on the internet support OpenID authentication for their members. To make it easier for users to login to our site with one  of these commonly available OpenIDs, we will add links to a short list of them by defining a list in config.py

**Database**
For this application we are using a SQLite database, since it conveniently stores our database in a single file and doesn't require us to start a database server.

Using Flask-SQLAlchemy extension, which is an Object Relational Manager (ORM), to speak to our database for us.

In addition, we make use of SQLAlchemy-migrate to keep track of database updates to make database migrations easier.
