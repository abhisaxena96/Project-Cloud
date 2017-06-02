#!/usr/bin/python2
import os,cgitb
import commands
import cgi

print "Content-type:text/html"
print ""

cgitb.enable()

x=cgi.FieldStorage()
u=x.getvalue('usr')
e=x.getvalue('email')
m=x.getvalue('mob')
p=x.getvalue('passwd')
p1=x.getvalue('passwd1')
if (p==p1) :
	a=commands.getoutput("sudo cat /var/www/html/users.txt | grep "+u+" | awk '{print$1}'")
	if (a != ""):	
		print "this user already exist"	
	else :
		f=open("/var/www/html/users.txt",'a')
		f.write(u)
		f.write(" : ")
		f.write(e)
		f.write(" : ")
		f.write(m)
		f.write(" : ")
		f.write(p)
		f.write(" : ")
		f.write(p1)
		f.write(" : ")
		f.write("\n")
		f.close()
		os.system("sudo useradd  "+u+"")
		commands.getstatusoutput("sudo echo "+p1+"| sudo passwd "+u+" --stdin ")
		print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.26.128/index.html'/>"
		
else :
	print "wrong user name os password"


