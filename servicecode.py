#!C:\Python27\python
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb,os
import cgitb
cgitb.enable()
f=cgi.FieldStorage()
type=f.getvalue('type')
title=f.getvalue('title')
desc=f.getvalue('desc')
pic=f['pic']
con=MySQLdb.connect("127.0.0.1","root","","bakeology",3306)
cur=con.cursor()
fn=os.path.basename(pic.filename)
open('../database_img/database_service/'+fn,'wb').write(pic.file.read())
print "success"
q="insert into tbl_service(stype,stitle,sdesc,spic,sdate) values('"+str(type)+"','"+str(title)+"','"+str(desc)+"','"+str(fn)+"',curdate())"
cur.execute(q)

