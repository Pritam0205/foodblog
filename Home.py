#!C:/Users/user/AppData/Local/Programs/Python/Python38/python
import cgi,cgitb,config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html>
<head>

    <title>
        Khaddo Roshik
       </title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

<link href="khaddoroshik.css" rel="stylesheet">
</head>

    <nav class="navbar navbar-light navbar-expand-md bg-custom-2">
  <a class="navbar-brand" href="#">Home</a>
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
</div> <br>

<div>
  <center>
    <img src="Khaddo Roshik.png" style="width: 25%"; height="250px;">
  </center>
</div> <br>

<marquee width="100%" direction="right" height="60px">
  <b style="font-family: monospace; font-size:xx-large; color: gold ;">WELCOME PETUK</b>
  </marquee> 


<div class="slideshow-container">

<div class="mySlides ">
  <div class="numbertext">1 / 4</div>
  <img src="Slider Pic 1.jpg" style="width:100%">
  <div class="text">Royal Indian Restaurant</div>
</div>

<div class="mySlides ">
  <div class="numbertext">2 / 4</div>
  <img src="Slider Pic 2.jpg" style="width:100%">
  <div class="text">Arsalan</div>
</div>

<div class="mySlides ">
  <div class="numbertext">3 / 4</div>
  <img src="Slider Pic 3.jpg" style="width:100%">
  <div class="text">Oudh 1590</div>
</div>

<div class="mySlides ">
  <div class="numbertext">4 / 4</div>
  <img src="Slider Pic 4.jpg" style="width:100%">
  <div class="text">Cafe Ekante</div>
</div>


</div>
<br>

<div style="text-align:center">
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
</div>

<script>
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 3000); // Change image every 5 seconds
}
</script>


<body background="https://images.unsplash.com/photo-1589041127168-9b1915731dc3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80">


    <div class="container">

        <div class="card-columns">  
            <div class="card text-center">
                <img class="card-img-top" src="https://i.ytimg.com/vi/uyDVLNGeopI/maxresdefault.jpg" alt="Card image" style="width:100%"; height="220px;">
                <div class="card-body">
                  <h4 class="card-title">Arsalan</h4>
                  <a href="https://arsalanrestaurants.com/" class="btn btn-link">Checkout</a>
                </div>
              </div>

              
              <div class="card text-center">
                <img class="card-img-top" src="https://qph.fs.quoracdn.net/main-qimg-f7f250042a9210edb4d3de79ed2611db.webp" alt="Card image" style="width:100%"; height="220px;">
                <div class="card-body">
                  <h4 class="card-title">Oudh 1590</h4>
                 <p class="card-text"><a href="https://www.oudh1590.com/></a></p></a>
                  <a href="Video 3.mp4" class="btn btn-link">Checkout</a>
                </div>
              </div>

              <div class="card text-center">
                <img class="card-img-top" src="https://media-cdn.tripadvisor.com/media/photo-s/0f/54/0a/ed/royal-indian-restaurant.jpg" alt="Card image" style="width:100%"; height="220px;">
                <div class="card-body">
                  <h4 class="card-title">Royal Indian Restaurant</h4>
                 <p class="card-text"><a href="https://g.co/kgs/Tyw9zh"></a></p></a>
                  <a href="Video 3.mp4" class="btn btn-link">Checkout</a>
                </div>
              </div>

              <div class="card text-center">
                <img class="card-img-top" src="https://upload.wikimedia.org/wikipedia/commons/8/89/Indian_Coffee_House%2C_Kolkata_%286334188949%29.jpg" alt="Card image" style="width:100%"; height="220px;">
                <div class="card-body">
                  <h4 class="card-title">Indian Coffee House</h4>
                  <a href="https://www.zomato.com/kolkata/indian-coffee-house-college-street" class="btn btn-link">Checkout</a>
                </div>
              </div>

            <div class="card text-center">
              <img class="card-img-top" src="data:image/png;base64,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" alt="Card image" style="width:100%"; height="220px;">
              <div class="card-body">
                <h4 class="card-title">Aminia</h4>
                <a href="https://www.aminia.co.in/" class="btn btn-link">Checkout</a>
              </div>
            </div>

            <div class="card text-center">
              <img class="card-img-top" src="https://b.zmtcdn.com/data/pictures/7/17983797/4e8f2c0d2062b9d651b6314ded4e30c7.jpg?fit=around|750:500&crop=750:500;*,*" alt="Card image" style="width:100%"; height="220px;">
              <div class="card-body">
                <h4 class="card-title">Dada Boudi</h4>
               <p class="card-text"><a href="https://g.co/kgs/j5TwAJ"></a></p></a>
                <a href="Video 3.mp4" class="btn btn-link">Checkout</a>
              </div>
            </div>

            <div class="card text-center">
              <img class="card-img-top" src="https://content.jdmagicbox.com/comp/kolkata/c6/033pxx33.xx33.160419072334.n8c6/catalogue/tandoor-house-ballygunge-kolkata-home-delivery-restaurants-104uix1.jpg" alt="Card image" style="width:100%"; height="220px;">
              <div class="card-body">
                <h4 class="card-title">Tandoor House</h4>
               <p class="card-text"><a href="https://g.co/kgs/pVXZzg"></a></p></a>
                <a href="Video 3.mp4" class="btn btn-link">Checkout</a>
              </div>
            </div>

            <div class="card text-center">
              <img class="card-img-top" src="https://i2.wp.com/moha-mushkil.com/wp-content/uploads/2018/04/IMG_1608.jpg?fit=1024%2C768&ssl=1" alt="Card image" style="width:100%"; height="220px;">
              <div class="card-body">
                <h4 class="card-title">Golbari</h4>
               <p class="card-text"><a href="https://g.co/kgs/WoqTnV"></a></p></a>
                <a href="Video 3.mp4" class="btn btn-link">Checkout</a>
              </div>
            </div>

            <div class="card text-center">
              <img class="card-img-top" src="https://media-cdn.tripadvisor.com/media/photo-s/0f/2c/b1/cb/menu-card.jpg" alt="Card image" style="width:100%"; height="220px;">
              <div class="card-body">
                <h4 class="card-title">Tung Nam</h4>
                <a href="https://www.zomato.com/kolkata/tung-nam-bara-bazar" class="btn btn-link">Checkout</a>
              </div>
            </div>

            <div class="card text-center">
              <img class="card-img-top" src="data:image/jpeg;base64,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" alt="Card image" style="width:100%"; height="220px;">
              <div class="card-body">
                <h4 class="card-title">Mitra Cafe</h4>
               <p class="card-text"><a href="https://g.co/kgs/z9P493"></a></p></a>
                <a href="Video 3.mp4" class="btn btn-link">Checkout</a>
              </div>
            </div>


            <div class="card text-center">
              <img class="card-img-top" src="https://media-cdn.tripadvisor.com/media/photo-s/17/fe/4b/4d/the-logo.jpg" alt="Card image" style="width:100%"; height="220px;">
              <div class="card-body">
                <h4 class="card-title">Cafe Ekante</h4>
               <p class="card-text"><a href="https://www.google.com/search?q=pedri&rlz=1C1CHBF_enIN870IN870&sxsrf=ALeKk03IFwzgIyFzJi1iJ_ETL3WvTX1Zrw%3A1627914568801&ei=SAEIYf6zMITXz7sPuYC0uAc&gs_ssp=eJzj4tVP1zc0zDA1rcooq8owYPRiLUhNKcoEAEunBt8&oq=Pedri&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCC4QsQMQQxCTAjIHCAAQsQMQQzIECAAQQzIFCAAQgAQyBQgAEIAEMgUILhCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgjECc6BAguEEM6CgguELEDEIMBEEM6CAgAEIAEELEDOgsIABCABBCxAxCDAToECAAQA0oFCDgSATFKBAhBGABQxvcQWLmMEWD7mxFoAXAAeACAAe0CiAHuDpIBBTItNS4ymAEAoAEBwAEB&sclient=gws-wiz"></a></p></a>
                <a href="Video 3.mp4" class="btn btn-link">Checkout</a>
              </div>
            </div>

            <div class="card text-center">
              <img class="card-img-top" src="https://www.theindianwire.com/wp-content/uploads/2021/03/barbeque-nation.jpg" alt="Card image" style="width:100%"; height="220px;">
              <div class="card-body">
                <h4 class="card-title">Barbeque Nation</h4>
               <p class="card-text"><a href="https://g.co/kgs/sx9p1Y"></a></p></a>
                <a href="Video 3.mp4" class="btn btn-link">Checkout</a>
              </div>
            </div> 

            

        </div>
    </div> <br>
 
    <footer>

  <div class="jubotron text-light bg-body">
      <div class="row">

    
          <div class="col-sm-6">
              <p> @copyright2021</p>

          </div>
          <div class="col-sm-6">
              contact us::

              <ul>
                  <li>phone - 9002817879</li>
                  <li>mail - pritamkar0205@gmail.com</li>
                  <li>designed by pritam</li>
              </ul>

          </div>
      </div>
  </div>
</footer>

            
</body>
</html>''')