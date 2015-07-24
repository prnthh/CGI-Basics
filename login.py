#!/usr/bin/python

import cgi, cgitb, os

form = cgi.FieldStorage()

if form.getvalue('username'):
	username = form.getvalue('username')

if form.getvalue('password'):
	password = form.getvalue('password')

########################################################
httpPre = """
<html>
<head><title>Login</title></head>
<body>
</body>
</html>
"""
########################################################
content = """
<a href="logout.py">Log out</a><br><br><br><br>
"""
########################################################


if(username.lower()=="admin" and password.lower()=="password"):
	print ("Set-Cookie: session=696969123")
	print ("Content-type: text/html\r\n\r\n")
	print httpPre % (content)
