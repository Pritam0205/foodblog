#!C:/Users/user/AppData/Local/Programs/Python/Python38/python
import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
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
        Log In
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
               <h1 class="text-center">LOG IN</h1>
            </div>
    <form method="post" action="login_code.py" class="needs-validation" novalidate>
       <center>
       <table cellpadding="7" border="2" id="xyz" style="width: auto; height: auto;">
        <tr>
            <td>Email-Id</td>
            <td><input type="email" name="email"></td>
        </tr>
        <tr>
            <td>Password</td>
            <td><input type="password" name="password"></td>
        </tr>
        <tr>
            <td colspan="2" align="center">
                <input type="submit" name="ok" value="Login">
            </td>
        </tr>
    </table>
</form>''')
if form.getvalue('msg'):
    print(form.getvalue('msg'))
print('''</body>
</html>''')
