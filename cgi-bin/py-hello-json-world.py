#!/usr/bin/python
import socket
from datetime import datetime
import json

my_time = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
my_ip_addr = socket.gethostbyaddr(socket.gethostname())

my_obj_dict = {
    "time" : my_time,
    "heading" : "Hello, Python",
    "message" : "This page was generated with the Python programming language",
    "IP" : my_ip_addr,
    "title" : "Hello, Python"
}

json_obj = json.dumps(my_obj_dict)
print(json_obj)