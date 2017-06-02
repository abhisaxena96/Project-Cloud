#!/usr/bin/python2
import commands
import cgi,cgitb

print "Content-type : text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
user=x.getvalue('usr')
password=x.getvalue('passwd')
osname=x.getvalue('name')
osram=x.getvalue('ram')
oscpu=x.getvalue('cpu')
por=x.getvalue('port')
hd1=x.getvalue('hd')

#hd=x.getvalue('hd')

#for radio button
n=x.getvalue('radio')
os=x.getvalue('y')
commands.getoutput("systemctl restart httpd")
commands.getoutput("setenforce 0")
commands.getoutput("itables -F")
a=commands.getoutput("cat /var/www/html/users.txt | grep "+user+ " | awk '{print$1}'")
b=commands.getoutput("cat /var/www/html/users.txt | grep "+password+ " | awk '{print$7}'")

	
#LINUX os--------------------------------------------------------------------
if (os=="1" ) and (a !="") and (b !=""):
	#liveboot------------------------------------------------------------
	if (n=="1"):
		#commands.getoutput("sudo qemu-img create -f qcow2 -b  /var/lib/libvirt/images/rhel7.1.qcow2   /var/lib/libvirt/images/"+osname+".qcow2")
		commands.getoutput("sudo virt-install --name "+osname+" --ram "+osram+" --vcpu "+oscpu+" --cdrom /home/ubuntu14.iso --nodisk  --noautoconsole --graphics=vnc,listen=0.0.0.0,port="+por+",password="+password)
		f1=open('/var/www/html/clienttar/iaasclient.py','w+')
		f1.write("#!/usr/bin/python2 \nimport os\nos.system('vncviewer 192.168.26.128:"+por+"')")
		f1.close()
		commands.getoutput('sudo chmod 777 /var/www/html/clienttar/iaasclient.py')
		commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_iaas.tar /var/www/html/clienttar/iaasclient.py")
		#commands.getoutput("sudo cd /var/www/html/websockify-master")
		pid1=commands.getoutput("sudo netstat -tnlp | grep 7000 | awk '{print $7}' | cut -d'/' -f1")
		commands.getoutput("sudo kill -9 " +pid1)
		commands.getoutput("sudo /var/www/html/websockify-master/./run -D 7000 192.168.26.128:"+por)
		print  "<html>"
		print  "<p><a href='http://192.168.26.128/vnc/vnc.html'>Start</a>OS on browser</p>"
		print  "<p>><a href='http://192.168.26.128/clienttar/"+user+"_iaas.tar' download>Downlode</a> tar for VNC connectivity</p>"
		print	"<p>Go to your vnc viewer and connect using this ip & potrt[192.168.26.128:"+por+"]</p>"
		print  "</html>"

	elif (n=="2"):
		#virt-install --name asd --ram 1024 --vcpu 1  --cdrom  /root/Desktop/iso/rhel7.iso   --disk path=/var/lib/libvirt/images/asd.qcow2,size=9 --noautoconsole --graphics=vnc,listen=0.0.0.0,port=5909,password=1325
		commands.getoutput("sudo virt-install --name "+osname+" --ram "+osram+" --vcpu "+oscpu+"  --cdrom  /home/rhel7.iso   --disk path=/home/images/"+osname+".qcow2,size="+hd1+" --noautoconsole --graphics=vnc,listen=0.0.0.0,port="+por+",password="+password)
		
		f1=open('/var/www/html/clienttar/iaasclient.py','w+')
		f1.write("#!/usr/bin/python2 \nimport os\nos.system('vncviewer 192.168.26.128:"+por+"')")
		f1.close()
		commands.getoutput('sudo chmod 777 /var/www/html/clienttar/iaasclient.py')
		commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_iaas.tar /var/www/html/clienttar/iaasclient.py")
		pid1=commands.getoutput("sudo netstat -tnlp | grep 7000 | awk '{print $7}' | cut -d'/' -f1")
		commands.getoutput("sudo kill -9 " +pid1)
		commands.getoutput("sudo /var/www/html/websockify-master/./run -D 7000 192.168.26.128:"+por)
		print  "<html>"
		print  "<p><a href='http://192.168.26.128/vnc/vnc.html'>Start</a>OS on browser</p>"
		print  "<p>><a href='http://192.168.26.128/clienttar/"+user+"_iaas.tar' download>Downlode</a> tar for VNC connectivity</p>"
		print	"<p>Go to your vnc viewer and connect using this ip & potrt[192.168.26.128:"+por+"]</p>"
		print  "</html>" 
	

		

	


	#snap---------------------------------------------------------------
	elif (n=="3"):
		commands.getoutput("sudo qemu-img create -f qcow2 -b  /var/lib/libvirt/images/"+osname+".qcow2   /var/lib/libvirt/images/"+osname+"_snap.qcow2")
		commands.getoutput("sudo virt-install --name "+osname+" --ram "+osram+" --vcpu "+oscpu+" --disk=/var/lib/libvirt/images/"+osname+"_snap.qcow2 --import --noautoconsole --graphics=vnc,listen=0.0.0.0,port="+por+",password="+password)
		f1=open('/var/www/html/clienttar/iaasclient.py','w+')
		f1.write("#!/usr/bin/python2 \nimport os\nos.system('vncviewer 192.168.26.128:"+por+"')")
		f1.close()
		commands.getoutput('sudo chmod 777 /var/www/html/clienttar/iaasclient.py')
		commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_iaassnap.tar /var/www/html/clienttar/iaasclient.py")
		#commands.getoutput("sudo cd /var/www/html/websockify-master")
		commands.getoutput("sudo /var/www/html/websockify-master/./run -D 7000 192.168.26.128:"+por)
		print  "<html>"
		print  "<p><a href='http://192.168.26.128/vnc/vnc.html'>Start</a>OS on browser</p>"
		print  "<p>><a href='http://192.168.26.128/clienttar/"+user+"_iaassnap.tar' download>Downlode</a> tar for VNC connectivity</p>"
		print	"<p>Go to your vnc viewer and connect using this ip & potrt[192.168.26.128:"+por+"]</p>"
		print  "</html>"

		


#Windows os------------------------------------------------------------------
elif (os=="1" ) and (a !="") and (b !=""):
    pass;

else :
	print "<html>"
	print "Wrong user name or password"
	print "</html>" 










