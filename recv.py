#!/usr/bin/python

import cgi

print  "Content-type:text/html"
print  ""

webdata=cgi.FieldStorage()
# this will recv all http data

user=webdata.getvalue('u')

# to get email id given by user
password=webdata.getvalue('p')
#
if  user == 'root' and password == 'redhat' :

	print  "access granted for all cloud services"
	
else :
	print  "Authentication failure"
	print  "<a href='http://192.168.10.103/index.html'>"
	print  "<img src='http://192.168.10.103/try.jpg'>"
	print  "</a>"	
	

