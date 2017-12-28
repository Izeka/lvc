#!/usr/bin/python

import urllib
url = "http://10.65.217.1/login.html" 
username = "rmartinez" 
password = "fingolfin"
login_data = urllib.urlencode({'username': username, 'password' : password, 'submit':'sendin'})
op = urllib.urlopen(url, login_data).read()
print op
