#!C:\Python27\python
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
f=cgi.FieldStorage()
name=f.getvalue('name')
email=f.getvalue('email')
mob=f.getvalue('mob')
msg=f.getvalue('msg')
con=MySQLdb.connect("127.0.0.1","root","","bakeology",3306)
cur=con.cursor()
q="insert into tblcontact(name,email,mobno,msg,enqdate) values('"+str(name)+"','"+str(email)+"','"+str(mob)+"','"+str(msg)+"',curdate())"
cur.execute(q);  
print "<script>alert('Data Saved Successfully.');window.location.href='project/ContactUs.py';</script>";
