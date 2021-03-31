#!C:\Python27\python
print('Content-Type:text/html\n\n')

import cgi
import MySQLdb
f=cgi.FieldStorage()
id=f.getvalue('msg')
con=MySQLdb.connect("127.0.0.1","root","","bakeology",3306)
cur=con.cursor()
cmd="delete from tblcontact where eid='"+str(id)+"'";
cur.execute(cmd)
print "<script>alert('Record Deleted Successfully...');window.location.href='../ContactManagement.py';</script>";