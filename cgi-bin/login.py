#!/usr/bin/python2
import os,cgitb
import commands
import cgi
print "Content-type: text/html"
cgitb.enable()
x=cgi.FieldStorage()
u=x.getvalue('usr')
p=x.getvalue('passwd')

a=commands.getoutput("cat /var/www/html/users.txt |grep "+u+ " | awk '{print$1}'")
b=commands.getoutput("cat /var/www/html/users.txt |grep "+p+ " | awk '{print$1}'")

if (a != "") and (b !=""):
		print "location:http://192.168.26.128/home.html?q=sucess"
		print ""
	
else:
	print "location:http://192.168.26.128/index.html?q=sucess"
	print " "
	
	
