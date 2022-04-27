#!/usr/bin/python3

import os
from urllib import parse
import sys

print ("Cache-Control: no-cache\nContent-type: text/html\n\n")


# print HTML file top
print ("<!DOCTYPE html>" +
"<html><head><title>POST Echo</title>" +
"</head><body><h1 align='center'>POST Echo</h1>" +
"<hr>")

print ("<b>Message Body:</b> <br />\n")
print ("<ul>\n")

post_data = sys.stdin.read()
post_list = post_data.split('&')
for kv_pair in post_list:
    split_pair = kv_pair.split('=')
    print ("<li>" + split_pair[0] + ": " + split_pair[1] + "</li>")
print ("</ul>\n")

print("</body></html>")