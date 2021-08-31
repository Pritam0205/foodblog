#!C:/Users/user/AppData/Local/Programs/Python/Python38/python
import cgi,cgitb,config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <title>
        Sign Up
    </title>
    <style>
    body{
            background-repeat: no-repeat;
            background-size: cover;
        }
    </style>

</head>


<body>

<nav class="navbar navbar-expand-md bg-custom-2">
  <a class="navbar-brand" href="Home.py">Home</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
  
    <li class="nav-item">
      <a class="nav-link" href="" target="_blank">TIMELINE&nbsp;</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="signup.py">SIGNUP&nbsp;</a>
    </li>
      <li class="nav-item">
        <a class="nav-link" href="login.py" >LOGIN&nbsp;</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="logout.py" >LOGOUT&nbsp;</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="profile.py" >PROFILE&nbsp;</a>
      </li>
          
    
  </div>
</nav>
</div> <br>

    <div class="jumbotron">
               <h1 class="text-center">SIGN UP</h1>
            </div>
    <form method="post" enctype = "multipart/form-data" action="signup_code.py" class="needs-validation" novalidate>
       <center>
       <table cellpadding="7" border="2" id="xyz" style="width: auto; height: auto;">

     
    <tr>
      <td><label id="abc">Name</label></td>
      <td><input type="text" name="name" required placeholder="Enter your name"></td>
    </tr> 


    <tr>
      <td><label id="abc">Email Id</label></td>
      <td><input type="text" name="email" required placeholder="Enter your email"></td>
    </tr>  


    <tr>
      <td><label id="abc">Address</label></td>
      <td><input type="text" name="address" required placeholder="Enter your address"></td>
    </tr>  


    <tr>
      <td><label id="abc">Phone Number</label></td>
      <td><input type="text" name="phone" required placeholder="Enter phone number"></td>
    </tr>  


     <tr>
      <td><label id="abc">Password</label></td>
      <td><input type="password" name="password" required placeholder="Create password"></td>
    </tr> 

    <tr>
      <td><label id="abc">Upload Picture</label></td>
      <td><input type="file" name="image" required placeholder="Upload picture"></td>
    </tr> 
    
     
    </table><br><br>


    
     <div class="Submit">
      <input id="pqr" type="submit" name="ok" value="submit">
     </center></div>
        
    </form>''')

form=cgi.FieldStorage()
if form.getvalue('ok'):
    name=form.getvalue('name')
    email=form.getvalue('email')
    address=form.getvalue('address')
    phone=form.getvalue('phone')
    password=form.getvalue('password')
    try:
        cursor = config.db.cursor()
        src="SELECT email FROM user WHERE email='{}'".format(email)
        cursor.execute(src)
        rec=cursor.fetchall()
        if rec:
            print("You are already joined")
        else:
            sql="INSERT INTO user (name,email,address,phone,password) VALUES ('{}','{}','{}','{}','{}')".format(name,email,address,phone,password)
            cursor.execute(sql)
            config.db.commit()
            config.db.close()
            print('signup successful')
    except Exception as e:
        print(e)
print('''
</body>
</html>''')