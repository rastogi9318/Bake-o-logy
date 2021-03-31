#!C:\Python27\python
print('Content-Type:text/html\n\n')
print('''
<html>
	<head>
		<link href="iconTech.png" rel="icon"/>
		<meta name="viewport" content="width=device-width,intial-scale=1.0"/>
		<link href="css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
		<link href="css/bootstrap-theme.min.css" rel="stylesheet" type="text/css"/>
		<link rel="stylesheet" href="css/font-awesome.min.css" type="text/css"/>
		<script src="js/jquery.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<link rel="stylesheet" href="bakeology.css"/>
			<style>
			.outer
{
min-height:800px;

}
.top
{
	min-height:50px;
	background:gray;
	
}
.logo
{
	height:50px;
	width:250px;
	margin:5px 5px;
	background:white;
	font-size:30px;
	font-family:Algerian;
	border:5px double green;
}
.menu
{
	height:50px;
	z-index:10;
}
#menu
{
	background:none;
	border:none;
	box-shadow:none;
	padding:1% 0%;
	margin:0px;
}
#menu ul li a
{
	color:white;
	text-shadow:none;
	font-weight:bold;
	font-size:17px;
}
#menu ul li:hover
{
	background:transparent; 
}
.banner
{
	min-height:600px;
	background:url('bimg/d42.jpg');	
	background-size:100% 100%;
	background-attachment:fixed;
	background-repeat:no-repeat;
}
.banner1
{
	min-height:600px;
	background-color:rgba(0,0,0,.4);
}
.bantxt
{
	min-height:600px;
	font-size:45px;
	color:white;
	margin-left:40%;
	font-family:Blackadder ITC;
}
.ban1txt
{
	font-size:30px;
	font-family:Algerian;
	color:white;
	margin-left:25%;
}
.About
{
min-height:350px;
background:white;
margin-top:30px;
}
.us
{
min-height:350px;
background:white;
}
.About1
{
min-height:350px;
background:white;
}
.slider
{
min-height:350px;
background:white;
border:5px double green;
}
.footer
{
min-height:400px;
background:#37474F;
margin-top:60px;
}
.f1
			{
			min-height:100px;
			background:#f4f4f0;
			margin-right:3%;
			margin-top:-40px;
			line-height:100px;
			color:brown;
			font-size:20px;
			}
			.f1 a 
			{
			color:brown;
			text-decoration:none;
			}
			.center
			{
			min-height:50px;
            color:green;
			margin-top:80px;
			}
			.footer
{
 min-height:400px;
 background:#37474F;
 margin-top:40px;
}
.f1
{
 min-height:100px;
 background:#f4f4f0;
 margin-right:3%;
 margin-top:-40px;
 line-height:100px;
 color:brown;
 font-size:20px;
}
.f1 a 
{
 color:brown;
 text-decoration:none;
}
.center
{
 min-height:50px;
 color:green
 margin-top:80px;
}
.cfooter
{
 min-height:50px; 
 margin-top:40px;
 color:white;
 font-size:20px;
}
			

			</style>
		</head>
			<body>
			<div class="col-sm-12 outer">
			<div class="row">
				<div class="col-sm-12 top">
				<div class="row">
					<div class="col-sm-3 logo">Bake<span style="color:orange;">-o-</span>logy</div>
					<div class="col-sm-9 menu">
					<nav class="navbar navbar-default" id="menu">
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
        <li><a href="bakeology.py"><i class="fa fa-home"></i> Home</a></li>
        <li><a href="AboutUs.py">About Us</a></li>
		<li><a href="ContactUs.py">Contact Us</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Menus <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Cakes</a></li>
            <li><a href="#">Pasty</a></li>
            <li><a href="#">Ice Creams</a></li>
			<li><a href="#">Drinks</a></li>
          </ul>
        </li>
		<li><a href="service.py">Services</a></li>
		
         
		<li><a href="#">Gallery</a></li>
		<li><a href="#">Order Now</a></li>
		<li><a href="#">Admin LogIn</a></li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
					</div>
		        </div>
				</div>
			<div class="col-sm-12 banner">
			<div class="row">
				<div class="col-sm-12 banner1"><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
				<span class="bantxt">Delecious</span><br/>
				<span class="ban1txt">What You Need---We Have It </span>
				</div>
			</div>
			</div>
			<div class="col-sm-12 About">				
					<div class="col-sm-1"></div>
					<div class="col-sm-10 Us">
						<div class="col-sm-6 About1"><center>
						<span style="font-size:50px;font-family:Curlz MT;">About Us</span></center>
						<span style="font-size:20px;text-align:justify;word-spacing:8px;">Hii,I am Yash Rastogi..I make this<br/><span class="b">site for the peoples who want to
							  purchase cakes,<br/><span class="a">pastry,drinks and many more items those<br/><span class="b"> available to 
							  bakery store.<br/>
							  <span class="a">Here people simply order there items online<br/><span class="b"> to nearest shop in their locality<br/>
								<span class="a">The people who have their bakery<br/>
								<span class="b">they add their shop in this site<br/>
							 <span style="margin-left:70px;font-family:Algerian; font-size:30px;">WE kNOW YOUR TASTE....</span>
								<span style="margin-left:180px;font-family:Algerian;">-----Thanking You!!!!!!!!!!!</span>
						
						</span>
						
						</div>
						<div class="col-sm-6 slider">
						<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
    <li data-target="#carousel-example-generic" data-slide-to="1"></li>
    <li data-target="#carousel-example-generic" data-slide-to="2"></li>
	<li data-target="#carousel-example-generic" data-slide-to="3"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="bimg/d4.jpg" alt="...">
      <div class="carousel-caption">
	  ...
      </div>
    </div>
    <div class="item">
      <img src="bimg/d5.jpg" alt="...">
      <div class="carousel-caption">
        ...
      </div>
    </div>
	<div class="item">
      <img src="bimg/d6.jpg" alt="...">
      <div class="carousel-caption">
        ...
      </div>
	  <br>
	  </div>
	  <div class="item">
      <img src="bimg/d7.jpg" alt="...">
      <div class="carousel-caption">
      ...
      </div>
	  </div>
	 
  </div>

  <!-- Controls -->
  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
						</div>
						<div class="col-sm-4"></div>
					</div>
				</div>
				<div class="col-sm-12 footer">
				<div class="col-sm-1"></div>
				<div class="col-sm-3  f1">
				<span style="margin-right:239px"><a href="#">FAQ</a></span>
				<a href="#"><span class="fa fa-chevron-right"></span></a>
				</div>
				<div class="col-sm-3 f1">
				<span style="margin-right:210px;"><a href="ContactUs.py">Contact</a></span>
				<a href="Contactus.py"><span class="fa fa-chevron-right"></span></a>
				</div>
				<div class="col-sm-3 f1">
				<span style="margin-right:177px;"><a href="#">Our Stores</a></span>
				<a href="#"><span class="fa fa-share"></span></a>
				
				</div>
				<div class="col-sm-1"></div>
				<div class="col-sm-12 text-center center">
				<span style="color:white;font-size:18px;">Follow Us On:-</span><br/><br/>
				<span class="fa fa-facebook" style="color:green;border:4px solid green; font-size:25px;padding:10px;"></span>
				<span class="fa fa-twitter" style="color:green;border:4px solid green; font-size:25px;padding:10px;"></span>
				<span class="fa fa-instagram" style="color:green;border:4px solid green; font-size:25px;padding:10px;"></span>
				<span class="fa fa-youtube" style="color:green;border:4px solid green; font-size:25px;padding:10px;"></span>
				</div>
				<div class="col-sm-12 text-right cfooter">
				<span class="fa fa-phone" style="margin-bottom:10px;">:- 91,7376890952</span><br/>
				<span class="fa fa-envelope">:- yash20000rastogi@gmail</span>
				</div>
				</div>
				</div>
		</div>
		</div>
''')