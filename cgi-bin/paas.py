#!/usr/bin/python2
import commands
import cgi,cgitb,random
print "Content-type : text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
user=x.getvalue('usr')
password=x.getvalue('passwd')
p=x.getvalue('p')

a=commands.getoutput("cat /var/www/html/users.txt | grep "+user+ " | awk '{print$1}'")
b=commands.getoutput("cat /var/www/html/users.txt | grep "+password+ " | awk '{print$7}'")
port=random.randint(6000,7000)	
if ((p=="1") & (a!="") & (b !="")):
		
	 	id=commands.getoutput("sudo docker run -itd -p "+ str(port) +":4200  -d  ankur")
		commands.getoutput("sudo docker exec -t "+id[1]+"  service shellinaboxd restart")
		print "<html>"
        	print "<a href='http://192.168.26.128:"+str(port)+":4200' target='_blank'> Container \n</a>"
        	print "access containers using ID=python password=python\n"
        	print "</html>"
else:
	print "<html>"
	print "<p>User name or password are incorrect !</p>"
	print "<html>"
