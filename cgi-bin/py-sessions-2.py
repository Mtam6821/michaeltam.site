#!/usr/bin/python
import requests
session = requests.session()

print ("Cache-Control: no-cache\n")
print ("Content-type: text/html \n\n")

# print HTML file top
print ("<!DOCTYPE html>")
print ("<html>")
print ("<head>")
print ("<title>Perl Sessions</title>")
print ("</head>")
print ("<body>")

print ("<h1>Python Sessions Page 1</h1>")

if (session.cookies.get("username") != ""):
	print("<p><b>Name:</b> " + session.cookies.get("username"))
else:
	print ("<p><b>Name:</b> You do not have a name set</p>")
print ("<br/><br/>")
print ("<a href=\"/cgi-bin/py-sessions-2.py\">Session Page 2</a><br/>")
print ("<a href=\"/py-cgiform.html\">Py CGI Form</a><br />")
print ("<form style=\"margin-top:30px\" action=\"/cgi-bin/py-destroy-session.pl\" method=\"get\">")
print ("<button type=\"submit\">Destroy Session</button>")
print ("</form>")

print ("</body>")
print ("</html>")