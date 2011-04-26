#!/usr/bin/python26
import sys
import os
import json
import urllib
import urlparse



def index():
    html = """
    <html>
    <head><title>JSON server usage</title>
    <style type='text/css'>
        body {
            font-family: "Verdana", "Arial", "Sans";
            color: #333;
            font-size: 14px;
            background: #fff;
        }
    </style>
    </head>
    <body>
    <h2>Jenkins JSON Server</h2>
    <h3>Usage:</h3>
    <p>
    <strong>/jenkins_jobs</strong><br />
    Returns a JSON list of all jenkins jobs
    </p>
    </body>
    </html>
    """

    return html



## Get all service hostnames
#   @param req [object] The request object
#   @retval [json] A list of all servers in the current environment
def jobs(req):

    req.content_type = "application/json"
    info = req.form


    try:
       username = info['username']
    except KeyError:
       raise KeyError('cannot find username key in query string')

    try:
       password = info['password']
    except KeyError:
       raise KeyError('cannot find password key in query string')

    try:
       ciHost = info['ciHost']
    except KeyError:
       raise KeyError('cannot find ciHost key in query string')

    #fp = urllib.urlopen("http://rntbuild:rntbuild$$@centos-55-64-vm7.local:8080/api/json")
    ciUrl = "http://" + username + ":" + password + "@" + ciHost + "/api/json" 
    fp = urllib.urlopen(ciUrl)

    objs=json.load(fp)
    jobs=objs["jobs"]

    jsonData = ""
    jsonData += "[\n"
    for j in jobs:
       jsonData += "{name:" + "\"" + j["name"] + "\",value:" + "\"" + j["name"] + "\"},"
    jsonData += "]"

    return jsonData
