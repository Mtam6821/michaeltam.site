#!/usr/bin/python3

print("Set-Cookie: destroyed\nCache-Control: no-cache\nContent-type: text/html\n\n")


print ("<html>")
print ("<head>")
print ("<title>Python Session Destroyed</title>")
print ("</head>")
print ("<body>")
print ("<h1>Session Destroyed</h1>")
print ("<a href=\"/py-cgiform.html\">Back to the Python CGI Form</a><br />")
print ("<a href=\"/cgi-bin/py-sessions-1.py\">Back to Page 1</a><br />")
print ("<a href=\"/cgi-bin/py-sessions-2.py\">Back to Page 2</a>")
print ("</body>")
print ("</html>")
