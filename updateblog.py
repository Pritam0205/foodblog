#!C:/Users/user/AppData/Local/Programs/Python/Python38/python
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">''')
import cgi, cgitb, config
cgitb.enable()
frm=cgi.FieldStorage()
id=frm.getvalue('id')
#print(id)
src="SELECT * FROM blog WHERE id='{}'".format(id)
#print(src)
cursor3=config.db.cursor()
cursor3.execute(src)
rs=cursor3.fetchall()
rec=rs[0]
# print(rec)
# print(rec[0])
# print(rec[1])
# print(rec[2])

print('''
  <head>
        <title>
                update blog
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

        <!--update blog starts-->
        <div class="jumbotron">
            <h1 class="text-center">UPDATE BLOG</h1>
        </div>
        
        <div class="container mt-5"> 
            <div class="jumbotron bg-info">   
            <form  action="updateblog_code.py" enctype = "multipart/form-data" method="post" class="needs-validation" novalidate>
                
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
                    <label for="blog">Date:</label>
                    <textarea type="text" class="form-control" id="blog" placeholder="blog date" name="date" required></textarea>
                    <div class="valid-feedback">Valid.</div>
                    <div class="invalid-feedback">Please fill out this field.</div>
                  </div>

                <div class="form-group">
                  <label for="image">Uplode picture:</label>
                  <input type="file" class="form-control" id="image" placeholder="image" name="image" required>
                  <div class="valid-feedback">Valid.</div>
                  <div class="invalid-feedback">Please fill out this field.</div>
                </div>

                <input type="hidden" name="id" value="%s">
                <button type="submit" class="btn btn-primary">Submit</button>
              </form>'''%(rec[1],rec[0]))

print('''            </div>
            </div>

    
        <!--update blog ends-->

            

    </body>
</html>''')