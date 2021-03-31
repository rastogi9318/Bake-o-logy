#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi
import MySQLdb
f=cgi.FieldStorage()
name=f.getvalue('name')
mob=f.getvalue('mob')
city=f.getvalue('city')
add=f.getvalue('add')
btype=f.getvalue('btype')
flav=f.getvalue('flav')
size=f.getvalue('size')
col=f.getvalue('col')
quan=f.getvalue('quan')
con=MySQLdb.connect("127.0.0.1","root","","bakeology",3306)
cur=con.cursor()
q="insert into tbl_order(oname,omobno,ocity,oadd,otype,oflavour,osize,ocolor,oquan,odate) values('"+str(name)+"','"+str(mob)+"','"+str(city)+"','"+str(add)+"','"+str(btype)+"','"+str(flav)+"','"+str(size)+"','"+str(col)+"','"+str(quan)+"',curdate())"
cur.execute(q);
print q