#!C:\Python27\python
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
a=cgi.FieldStorage()
con=MySQLdb.connect("127.0.0.1","root","","bakeology",3306)
cur=con.cursor()
userid=a.getvalue('email')
password=a.getvalue('pswd')
q="select * from tblalogin where userid='"+str(userid)+"' and password='"+str(password)+"'"
print q
cur.execute(q);  
res=cur.fetchall()
if res:
	print "<script>window.location.href='../admin/index.py';</script>";
else:
	print "<script>alert('username and Password is invalid !! try again !!...');window.location.href='../login.py';</script>";