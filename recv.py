#!/usr/bin/python

import cgi

print  "Content-type:text/html"
print  ""

webdata=cgi.FieldStorage()
# this will recv all http data

user_email=webdata.getvalue('e')

# to get email id given by user
user_password=webdata.getvalue('p')
#

print  "given user email id  is "+user_email
print  "given password is ",user_password

