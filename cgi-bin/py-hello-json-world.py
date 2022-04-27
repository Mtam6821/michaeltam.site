#!/usr/bin/python3

import os
from datetime import datetime
import json
print ("Cache-Control: no-cache\nContent-type: text/html\n\n")

my_time = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
my_ip_addr = os.environ.get("REMOTE_ADDR")

my_obj_dict = {
    "time" : my_time,
    "heading" : "Hello, Python",
    "message" : "This page was generated with the Python programming language",
    "IP" : my_ip_addr,
    "title" : "Hello, Python"
}

json_obj = json.dumps(my_obj_dict)
print(json_obj)