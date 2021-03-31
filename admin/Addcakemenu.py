#!C:\Python27\python
print('Content-Type:text/html\n\n')
print ("""
<html>
<head>
<link href="iconTech.png" rel="icon"/>
<meta name="viewport" content="width=device-width,intial-scale=1.0"/>
<link href="../css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link href="../css/bootstrap-theme.min.css" rel="stylesheet" type="text/css"/>
<link rel="stylesheet" href="../css/font-awesome.min.css" type="text/css"/>
<script src="../js/jquery.js"></script>
<script src="../js/bootstrap.min.js"></script>
<style>
.outer
{
min-height:100px;
}
.top
{
 min-height:50px;
 background:gray;
}
.logo
{
 height:50px;
 width:240px;
 margin:5px 5px;
 background:white;
 font-size:30px;
 font-family:Algerian;
 border:5px double green;
}
.menu
{
 height:50px;
 width:1000px;
 background:gray;
 z-index:10;
}
#menu
{
 background:none;
 border:none;
 box-shadow:none;
 padding:1% 0%;
 margin:0px;
 font-size:15px;
}
#menu ul li a
{
 color:white;
 text-shadow:none;
 font-weight:bold;
 font-size:12px;
}
#menu ul li:hover
{
 background:transparent; 
}
.head
{
 height:100px;
 background:url('../bimg/d1.jpg');
 background-attachment:fixed;
 background-size:100% 100%;
}
.head1
{
 height:100px;
 background-color:rgba(0,0,0,.4);
 color:white;
 font-size:20px;
 padding:2% 0%;
}
.addcake
{
min-height:550px;
margin-left:25%;
background:rgba(0,0,0,.3);
margin-top:20px;
margin-bottom:20px;
}

.footer
{
 min-height:50px;
 padding:1% 0%;
 text-align:center;
 color:white;
 font-size:20px;
 background:black;
}
</style>
</head>
<body>
<div class="col-sm-12 outer">
			<div class="row">
				<div class="col-sm-12 top">
				<div class="row">
					<div class="col-sm-3 logo">Bake<span style="color:orange;">-o-</span>logy</div>
					<div class="col-sm-9 menu">					<nav class="navbar navbar-default" id="menu">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only clpbtn">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
    </div>
<!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1" >
      <ul class="nav navbar-nav navbar-right">
        <li><a href="index.py">Dashboard</a></li>
        <li><a href="Addmenu.py">Add Menu</a></li>
		<li><a href="Addservices.py">Add Services</a></li>
		<li><a href="Addimages.py">Add Images</a></li>
		<li><a href="OrderManagement.py">Order Management</a></li>
		<li><a href="ContactManagement.py">Contact Management</a></li>
		<li><a href="Changepassword.py">Change Password</a></li>
		<li><a href="LogOut.py">LogOut</a></li>
		</li>
        
		      </ul>
			  
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
    					
		        </div></div></div>
				<div class="col-sm-12 main">
				<div class="row">
				<div class="col-sm-12 head">
				<div class="row">
				<div class="col-sm-12 head1">
				<div class="text-center"><span class="fa fa-cutlery "></span> Add Cake Menu </div>
				</div>
				</div></div>
				</div></div>
				<div class="col-sm-6 addcake">
				<div class="h2 text-center">Add Cakes Menu</div>
				<form action="../code/cakecode.py" enctype="multipart/form-data" method="post">
				<div class="h4">Cake Name</div>
				<input type="text" placeholder="Input Your Cake Name" name="cake" class="form-control">
				<div class="h4">Cake Size</div>
				<input type="text" placeholder="Input Your Cake size" name="size" class="form-control">
                <div class="h4">Cake Weight</div>
				<input type="text" placeholder="Input Your Cake Flavour" name="flavour" class="form-control">
                 <div class="h4">Price</div>
				 <input type="text" placeholder="Input Your Cake Weight" name="weight" class="form-control">
                 <div class="h4">Cake Flavour</div>
				<input type="text" placeholder="Input Your Cake Price" name="price" class="form-control">	
                  <div class="h4">Cake Image</div>
				<input type="file" placeholder="Import Your Cake image" name="pic" class="form-control"><br/>
                <input type="submit" class="form-control" value="Add">
				</div>
				<div class="col-sm-12 footer">
				<div class="col-sm-6">&copy;copyright:<a target="_blank" href="https://www.techpile.in">Techpile Technology.pvt.Ltd.</a>
				</div>
				
				<div class="col-sm-6">	
                Developed By:-Yash Rastogi</div>
				</div>
				
			</div>
			</div>


</body>
</html>

""")