#!C:\Python27\python
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb,os
import cgitb
cgitb.enable()
f=cgi.FieldStorage()
name=f.getvalue('name')
pic=f['pic']
fn=os.path.basename(pic.filename)
open('../fileUpload/'+fn,'wb').write(pic.file.read())
print "success"
