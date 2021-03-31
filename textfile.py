#!C:\Python27\python
print "Content-Type:text/html\n\n"
print '''
<html>
<head>
</head>
<body>
<form action="code/testcode.py" method="post" enctype="multipart/form-data">
Name
<input type="text" name="name"><br/><br/>
Upload Profile:<input type="file" name="pic"/><br/>
<input type="submit" value="Click to Upload">
</form>
</body>
</html>

'''