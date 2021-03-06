#!/usr/bin/python3

import sys, os

post_data = sys.stdin.read()
post_list = post_data.split(';')
name = ""

if (post_list[0] != "" and post_list[0] != "destroyed"):
    print("Set-Cookie: " + post_list[0] + "\nCache-Control: no-cache\nContent-type: text/html\n\n")
    name = (post_list[0]).split('=')[1]

elif (os.environ.get("HTTP_COOKIE") != ""):
    cookies_string = os.environ.get("HTTP_COOKIE")
    cookies_list = cookies_string.split(';')
    name = (cookies_list[0]).split('=')[1]
    if (name == "destroyed"):
        name = "No name set"
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

print ("<h1>Python Sessions Page 1</h1>")



print ("<p><b>Name:</b> " + name + "</p>")
print ("<br/><br/>")
print ("<a href=\"/cgi-bin/py-sessions-2.py\">Session Page 2</a><br/>")
print ("<a href=\"/py-cgiform.html\">Py CGI Form</a><br />")
print ("<form style=\"margin-top:30px\" action=\"/cgi-bin/py-destroy-session.py\" method=\"get\">")
print ("<button type=\"submit\">Destroy Session</button>")
print ("</form>")

print ("</body>")
print ("</html>")