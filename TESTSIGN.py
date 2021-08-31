#!C:/Users/user/AppData/Local/Programs/Python/Python38/python
import cgi,cgitb,config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  <title>Login and Signup form</title>
  <link href="https://fonts.googleapis.com/css?family=PT+Sans:400,500,700" rel="stylesheet"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
<link rel="stylesheet" href="./TEST.css">

</head>
<body>

    <nav class="navbar navbar-light navbar-expand-md bg-custom-2">
  <a class="navbar-brand" href="Home.py">Home</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
  
    <li class="nav-item">
      <a class="nav-link" href="">TIMELINE&nbsp;</a>
    </li>
      <li class="nav-item">
        <a class="nav-link" href="TESTSIGN.py" >LOGIN&nbsp;</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="logout.py" >LOGOUT&nbsp;</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="profile.py" >PROFILE&nbsp;</a>
      </li>
          
    
  </div>
</nav>
</div>

<section class="user-authentication">
  <div class="user_options-container">
    <div class="user_options-text">
      <div class="user_options-unregistered">
        <h2 class="user_unregistered-title">Don't have an account?</h2>
        <button class="user_unregistered-signup" id="signup-button">Sign up</button>
      </div>

      <div class="user_options-registered">
        <h2 class="user_registered-title">Have an account?</h2>
        <button class="user_registered-login" id="login-button">Login</button>
      </div>
    </div>
    
    <div class="user_options-forms" id="user_options-forms">
      <div class="user_forms-login">
        <h2 class="forms_title">Login</h2>
        <form method="post" action="login_code.py" class="forms_form">
          <fieldset class="forms_fieldset">
            <div class="forms_field">
              <input type="text" name="email" placeholder="Email" class="forms_field-input" required />
            </div>
            <div class="forms_field">
              <input type="password" name="password" placeholder="Password" class="forms_field-input" required />
            </div>
          </fieldset>
          <div class="forms_buttons">
            <button type="submit" class="forms_buttons-action">Login</button>
						<a class="forms_buttons-mb-button" id="signup-button-mb">Sign up</a>
          </div>
        </form>
      </div>
      <div class="user_forms-signup">
        <h2 class="forms_title">Sign Up</h2>
        <form method="post" enctype = "multipart/form-data" action="signup_code.py" class="forms_form">
          <fieldset class="forms_fieldset forms_field_sign">
            <div class="forms_field ">
              <input type="text" name="name" placeholder="Username" class="forms_field-input" required />
            </div>
            <div class="forms_field">
              <input type="text" name="email" placeholder="Email" class="forms_field-input" required />
            </div>
            <div class="forms_field">
              <input type="text" name="address" placeholder="Address" class="forms_field-input" required />
            </div>
            <div class="forms_field">
              <input type="text" name="phone" placeholder="Phone Number" class="forms_field-input" required />
            </div>
            <div class="forms_field">
              <input type="password" name="password" placeholder="Create Password" class="forms_field-input" required />
            </div>
            <div class="forms_field">
              <input type="file" name="image" placeholder="Upload Picture" class="forms_field-input" required />
            </div>
          </fieldset>
          <div class="forms_buttons">
            <button type="submit" class="forms_buttons-action">Sign up</button>
						<a class="forms_buttons-mb-button" id="login-button-mb">Login</a>
          </div>
          
        </form>
      </div>
    </div>
  </div>
</section>''')

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
print('''<script  src="./TEST.js"></script>
</body>
</html>''')
