#!C:/Users/user/AppData/Local/Programs/Python/Python38/python
import cgi, cgitb, config, check_cookie
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>
              profile
        </title>

        <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <link rel="stylesheet" href="vender/aos/aos.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  <script src="vender/aos/aos.js"></script>
    </head>

    <body>

        <!-- nav bar stared-->
        <nav class="navbar navbar-expand-md bg-dark">
            <a class="navbar-brand" href="Home.py">Home</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="collapsibleNavbar">
              <ul class="navbar-nav ">
                <li class="nav-item">
                  <a class="nav-link" href="profile.py">My Profile</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link " href="login.py"><button>Login</button></a>
                </li>
                <li class="nav-item">
                  <a class="nav-link " href="signup.py"><button>SignUp</button></a>
                </li>    
              </ul>
            </div>  
          </nav>
            <!--nav bar ends-->
        <!--profile info starts-->
          <div class="container ">
               <div class="jumbotron bg-light">
                <div class="container text-center">
                    <h2>{}</h2>
'''.format(check_cookie.user_data[1]))                               
print(''' <img src="{}" class="rounded-circle" alt="Cinque Terre" width="304" height="236"> 
                  </div>

                </div>
              <hr>

            <a href="createblog.py">  <button type="button" class="btn btn-info btn-block">create blog</button>
            <a>

              <hr>'''.format(check_cookie.user_data[4]))

print('''     <div class="list-group">''')
try:
    src="SELECT * FROM blog WHERE u_id='{}' ORDER BY date DESC".format(check_cookie.user_data[0])
    cursor=config.db.cursor()
    cursor.execute(src)
    rs=cursor.fetchall()
except Exception as e:
    print(e)
if rs:
    for rec in rs:


        print('''                <a href="#" class="list-group-item list-group-item-action">
                    <div class="card" style="width:100%">
                        <img class="card-img-top" src="{}" alt="Card image" style="width:100%; height: 350px;" >
                        <div class="card-body">
                          <h4 class="card-title">{}</h4>
                          <p class="card-text">{}</p>
                          <a href="#" class="btn btn-info mt-2">view post</a>
                          <a href="updateblog.py?id={}" class="btn btn-info mt-2">update post</a>
                          <a href="delete.py?id={}" class="btn btn-info mt-2">delete post</a>
                        </div>
                      </div>
                    
                </a>'''.format(rec[4],rec[1],rec[2],rec[0],rec[0]))
                
                
                
               
print('''             </div>

          </div>



        <!--profile info ends-->

            <!--footer starts-->
            <!-- <div class="jumbotron bg-dark">
                <div class="row">
                    <div class="col-sm-4 text-light">
                        <p>@copyright2021 all rights reserved</p>
                    </div>
                </div>
               </div> -->
   
               <!--footer ends-->

    </body>
</html>''')
