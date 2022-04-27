#!/usr/bin/python3
import os

print ("Cache-Control: no-cache\nContent-type: text/html\n\n")


# print HTML file top
print ("<!DOCTYPE html>" +
"<html><head><title>Environment Variables</title>" +
"</head><body><h1 align='center'>Environment Variables</h1>" +
"<hr>")

for env_var_name in os.environ:
    print(env_var_name + ": " + os.environ.get(env_var_name) + "<br>")



