#!/usr/bin/python3
import os, sys


name = ""
if (os.environ.get("HTTP_COOKIE") != ""):
    name = os.environ.get("HTTP_COOKIE")
    print ("Cache-Control: no-cache\nContent-type: text/html\n\n")

else :
    name = "No name set"
    print ("Cache-Control: no-cache\nContent-type: text/html\n\n")


# print HTML file top
print ("<!DOCTYPE html>")
print ("<html>")
print ("<head>")
print ("<title>Perl Sessions</title>")
print ("</head>")
print ("<body>")

print ("<h1>Python Sessions Page 2</h1>")

print ("<p><b>Name:</b> " + name + "</p>")

print ("<br/><br/>")
print ("<a href=\"/cgi-bin/py-sessions-1.py\">Session Page 1</a><br/>")
print ("<a href=\"/py-cgiform.html\">Py CGI Form</a><br />")
print ("<form style=\"margin-top:30px\" action=\"/cgi-bin/py-destroy-session.py\" method=\"get\">")
print ("<button type=\"submit\">Destroy Session</button>")
print ("</form>")

print ("</body>")
print ("</html>")