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
min-height:1500px;

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
	background:url('bimg/d1.jpg');	
	background-size:100% 100%;
	background-attachment:fixed;
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
	margin-left:45%;
	font-family:Blackadder ITC;
}
.ban1txt
{
	font-size:30px;
	font-family:Algerian;
	color:white;
	margin-left:35%;
}
.contact
{
 min-height:400px;
 background:white;
 width:1320px;
}
.con
{
 min-height:330px;
 width:400px;
}
.c
{
 background:orange;
 min-height:250px;
 font-size:20px;
 color:white;
 word-wrap:4px;
}
.c i
{
 font-size:25px;
 color:white;
}
.a
{
  text-align:justify;
  word-spacing:8px
}
.b
{
 text-align:justify
 word-spacing:8px;
}
.couter
{
 min-height:400px;
 width:1350px;
}
.form
{
 min-height:350px;
 width:550px;
}
.gmap
{
 min-height:350px;
 width:700px;
 background:gray; 
}
.txt1
{
 height:50px;
 border-radius:0px;
 box-shadow:2px 2px  4px black;
}
.btn
{
 width:75px;
 height:75px;
 color:black;
 margin-top:10px;
 border-radius:50%;
 box-shadow:3px 3px 4px black;
 background:white;
 font-weight:bold;
 margin-left:100px;
}
.btn1
{
 width:75px;
 height:75px;
 color:white;
 margin-top:10px;
 border-radius:50%;
 box-shadow:3px 3px 4px black;
 background:black;
 font-weight:bold;
 margin-left:100px;
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
			<div class="col-sm-12 contact">
				<div class="col-sm-12 text-center" style="min-height:50px;font-size:45px;margin-left:0px;margin-top:25px;;color:blue;">Contact Us</span>
				<div class="col-sm-12">
				<div class="col-sm-4 con">
				<div class="row">
				<div class="col-sm-2" style="background:white;"></div>
				<div class="col-sm-9 text-center c"><br/>
				<i class="fa fa-map-marker"> Location</i><br/><br/>
							Mahadevan Tola<br/>
						    Chowk Market,<br/>
							fatehpur,(U.P)
				</div>
				<div class="col-sm-1" style="background:white;"></div>
				</div>
				</div>
				
				<div class="col-sm-4 con">
				<div class="row">
				<div class="col-sm-2" style="background:white;"></div>
				<div class="col-sm-9 text-center c"><br/>
				<i class="fa fa-phone"> contact</i><br/><br/>
				           +91,7376890952<br/>
						   +91,7985464382
				</div>
				<div class="col-sm-1" style="background:white;"></div>
				</div>
				
				</div>
				<div class="col-sm-4 con">
				<div class="row">
				<div class="col-sm-2" style="background:white;"></div>
				<div class="col-sm-9 text-center c"><br/>
				<i class="fa fa-envelope"> Email</i><br/><br/>
				         yash20000rastogi@gmail.com<br/>
						 yash2000rastogi@gmail.com
				</div>
				<div class="col-sm-1" style="background:white;"></div>
				</div>
				</div>
				</div>
				</div>
				<div class="col-sm-12 couter">
				<div class="col-sm-6 gmap">
				<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3558.1615098718576!2d80.96419201452032!3d26.89836886718408!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39995785d5f7f1a5%3A0xffa47f1efe103f0d!2sTechpile+Technology+Pvt.+Ltd.!5e0!3m2!1sen!2sin!4v1564402435086!5m2!1sen!2sin" width="650" height="350" frameborder="0" style="border:0" allowfullscreen></iframe>
				</div>
				<div class="col-sm-6 form">
				<div class="h1 text-center" style="font-family:Curlz MT;margin-top:-20px;">Contact Form</div>
				<form action="code/enqcode.py" method="post">
				<input type="text" class="form-control txt1" name="name" placeholder="Full Name" required /><br/>
				<input type="email" class="form-control txt1" name="email" placeholder="Enter your Email.." required /><br/>
				<input type="number" class="form-control txt1" name="mob" placeholder="Contact No." required /></br>
				<textarea class="form-control txt1" name="msg" placeholder="Insert Your Querry Here"></textarea>
				<input type="submit" class="btn" value="Submit"/>
			    <input type="reset" class="btn1" value="Clear"/>
				</form>
				</div>
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
</body>
</html>
''')