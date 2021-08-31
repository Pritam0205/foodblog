#!C:/Users/user/AppData/Local/Programs/Python/Python38/python
import cgi, cgitb, config
cgitb.enable()
print('''
 <!DOCTYPE html>
<html lang="en">
    <head>
        <title>
               create blog
        </title>

        <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <link rel="stylesheet" href="vender/aos/aos.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  <script src="vender/aos/aos.js"></script>

  <script>
    // Disable form submissions if there are invalid fields
    (function() {
      'use strict';
      window.addEventListener('load', function() {
        // Get the forms we want to add validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
          form.addEventListener('submit', function(event) {
            if (form.checkValidity() === false) {
              event.preventDefault();
              event.stopPropagation();
            }
            form.classList.add('was-validated');
          }, false);
        });
      }, false);
    })();
    </script>
    </head>

    <body>

        <!--create blog starts-->
        <div class="jumbotron">
           <h1 class="text-center">CREATE BLOG</h1>
        </div>
        <div class="container mt-5">   
            <div class="jumbotron bg-info"> 
            <form method="post" enctype = "multipart/form-data" action="createblog_code.py" class="needs-validation" novalidate>
                
                <div class="form-group">
                  <label for="title">Title:</label>
                  <input type="text" class="form-control" id="title" placeholder="blog title" name="title" required>
                  <div class="valid-feedback">Valid.</div>
                  <div class="invalid-feedback">Please fill out this field.</div>
                </div>

                <div class="form-group">
                    <label for="blog">Blog:</label>
                    <textarea type="text" class="form-control" id="blog" placeholder="blog body" name="blog" required></textarea>
                    <div class="valid-feedback">Valid.</div>
                    <div class="invalid-feedback">Please fill out this field.</div>
                  </div>
                  
                <div class="form-group">
                  <label for="image">Uplode picture:</label>
                  <input type="file" class="form-control" id="image" placeholder="image" name="image" required>
                  <div class="valid-feedback">Valid.</div>
                  <div class="invalid-feedback">Please fill out this field.</div>
                </div>
                
                <button type="submit" class="btn btn-primary">Submit</button>
              </form>
            </div>
            </div>

            <!--create blog ends-->

            
    </body>
</html>




''')