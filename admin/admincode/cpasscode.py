#!C:\Python27\python
print('Content-Type:text/html\n\n')

import cgi
import MySQLdb
f=cgi.FieldStorage()
opass=f.getvalue('opass')
npass=f.getvalue('npass')
cnpass=f.getvalue('cnpass')
print opass,npass,cnpass
con=MySQLdb.connect("127.0.0.1","root","","bakeology",3306)
cur=con.cursor()
cmd="update tblalogin set password='"+str(npass)+"'where password='"+str(opass)+"'";
cur.execute(cmd)
print "<script>alert('record deleted successfully..');window.location.href='../../login.py';</script>";