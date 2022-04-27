#!/usr/bin/python
import os
from urllib import parse

print ("Cache-Control: no-cache\n")
print ("Content-type: text/html \n\n")

# print HTML file top
print ("<!DOCTYPE html>" +
"<html><head><title>GET Echo</title>" +
"</head><body><h1 align='center'>GET Echo</h1>" +
"<hr>")

full_query = os.getenv("QUERY_STRING", "")
print ("Query String: " + full_query)

query_dict = dict(parse.parse_qsl(full_query))
for key in list(query_dict):
    print ("<b>" + key + "</b>: " + query_dict[key])

print("</body></html>")

