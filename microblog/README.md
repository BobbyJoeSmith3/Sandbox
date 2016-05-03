**CONFIGURATION**
Many Flask extensions require some amount of configuration, so we are going to setup a configuration file inside our root microblog folder so that it is easily accessible if it needs to be edited

```Python
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
```

**LOGIN** Users will login using OpenID. OpenIDs have the benefit that the authentication is done by the provider of the OpenID, so we don't have to validate passwords, making our site more secure to our users.
