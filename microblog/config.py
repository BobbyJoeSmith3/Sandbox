#Activates cross-site request forgery prevention
WTF_CSRF_ENABLED = True
#Create cryptographic token to validate form when CSRF is enabled
SECRET_KEY = 'you-will-never-guess'

#Defines list of OpenID providers
OPENID_PROVIDERS = [
  {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
  {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
  {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
  {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
  {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]
