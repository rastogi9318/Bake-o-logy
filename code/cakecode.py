#!C:\Python27\python
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb,os
import cgitb
cgitb.enable()
f=cgi.FieldStorage()
cake=f.getvalue('cake')
size=f.getvalue('size')
flavour=f.getvalue('flavour')
weight=f.getvalue('weight')
price=f.getvalue('price')
pic=f['pic']
fn=os.path.basename(pic.filename)
open('../database_img/database_menu/database_cake/'+fn,'wb').write(pic.file.read())
print "success"
con=MySQLdb.connect("127.0.0.1","root","","bakeology",3306)
cur=con.cursor()
q="insert into tbl_cake(cname,csize,cflavour,cweight,cprice,cpic,cdate) values('"+str(cake)+"','"+str(size)+"','"+str(flavour)+"','"+str(weight)+"','"+str(price)+"','"+str(fn)+"',curdate())"
cur.execute(q);
