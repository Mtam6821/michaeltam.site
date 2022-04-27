#!/usr/bin/python3
import os
from datetime import datetime

print ("Cache-Control: no-cache\nContent-type: text/html\n\n")
print ("<html>")
print ("<head>")
print ("<title>Hello, Python!</title>")
print ("</head>")
print ("<body>")

print("<h1>Hello, Python!</h1>")
print("<p>This page was generated with the Python programming langauge</p>")

print("<p>Current Time: " + datetime.now().strftime("%a %b %d %H:%M:%S %Y") + "</p>")

print("<p>Your IP Address: " + os.environ.get("REMOTE_ADDR")  + "</p>")

print ("</body>")
print ("</html>")