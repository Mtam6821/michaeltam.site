#!/usr/bin/python3
import os, sys
from urllib import parse

print ("Cache-Control: no-cache\nContent-type: text/html\n\n")


# print HTML file top
print ("<!DOCTYPE html>" +
"<html><head><title>General Echo</title>" +
"</head><body><h1 align='center'>General Echo</h1>" +
"<hr>")

print ("<p><b>HTTP Protocol:</b> " + os.getenv("SERVER_PROTOCOL") + "</p>")
print ("<p><b>HTTP Method:</b> " + os.getenv("REQUEST_METHOD") + "</p>")
print ("<p><b>Query String:</b> " + os.getenv("QUERY_STRING") + "</p>")

print ("<b>Message Body:</b> <br />")
print ("<ul>\n")

post_data = sys.stdin.read()
post_list = post_data.split('&')
for kv_pair in post_list:
    split_pair = kv_pair.split('=')
    print ("<li>" + split_pair[0] + ": " + split_pair[1] + "</li>")
print ("</ul>\n")

print("</body></html>")
