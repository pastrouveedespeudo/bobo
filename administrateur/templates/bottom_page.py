


    <style>
    #containner {
        margin: 0px auto;
        width: 400px;
        height: 400px;
    }
    #videoElement {
        width: 400px;
        height: 400px;
        position:relative;
    }
    #patron{
      margin-left:105px;
      margin-top:100px;
      width: 200px;
      height: 200px;
      border: 2px solid red;
      border-radius:50%;
      position:absolute ;
      z-index:1;
    }
    </style>


  <!-- Portfolio Section -->
  <section id="portfolio">

  
    <div class="container-fluid p-0">
      <div class="row no-gutters">

      
        <div class="col-lg-4 col-sm-6">
        
          <a class="portfolio-box" href="/static/img/portfolio/fullsize/1.jpg">
            <img class="img-fluid" src="/static/img/portfolio/thumbnails/1.jpg" alt="">
            <div class="portfolio-box-caption">
            
              <div class="project-category text-white-50">
                Conerad 26 ans
              </div>
                
              
              <div class="project-name">
                A enfin arréter les pull orange et vert !
              </div>
            </div>
          </a>
        </div>

        
        <div class="col-lg-4 col-sm-6">
        
          <a class="portfolio-box" href="/static/img/portfolio/fullsize/2.jpg">
            <img class="img-fluid" src="/static/img/portfolio/thumbnails/2.jpg" alt="">
            
            <div class="portfolio-box-caption">
              <div class="project-category text-white-50">
                Sarah 24 ans
              </div>
              <div class="project-name">
                Ne fais plus d'achat inutil
              </div>
            </div>
          </a>
        </div>



        
        <div class="col-lg-4 col-sm-6">
          <a class="portfolio-box" href="/static/img/portfolio/fullsize/3.jpg">
            <img class="img-fluid" src="/static/img/portfolio/thumbnails/3.jpg" alt="">
            <div class="portfolio-box-caption">
              <div class="project-category text-white-50">
                Jo 35 ans
              </div>
              <div class="project-name">
                a kiffé le projet
              </div>
            </div>
          </a>
        </div>



        
        <div class="col-lg-4 col-sm-6">
          <a class="portfolio-box" href="/static/img/portfolio/fullsize/4.jpg">
            <img class="img-fluid" src="/static/img/portfolio/thumbnails/4.jpg" alt="">
            <div class="portfolio-box-caption">
              <div class="project-category text-white-50">
                Marion 17 ans
              </div>
              <div class="project-name">
                a adoré le site ! (elle est aujourd'hui manequin)
              </div>
            </div>
          </a>
        </div>



        
        <div class="col-lg-4 col-sm-6">
          <a class="portfolio-box" href="/static/img/portfolio/fullsize/5.jpg">
            <img class="img-fluid" src="/static/img/portfolio/thumbnails/5.jpg" alt="">
            <div class="portfolio-box-caption">
              <div class="project-category text-white-50">
                Rey 22 ans Professionel de Tennis
              </div>
              <div class="project-name">
                Ne fais pas un match sans avoir tester des habits sur My Profil
              </div>
            </div>
          </a>
        </div>

        
        <div class="col-lg-4 col-sm-6">
          <a class="portfolio-box" href="/static/img/portfolio/fullsize/6.jpg">
            <img class="img-fluid" src="/static/img/portfolio/thumbnails/6.jpg" alt="">
            <div class="portfolio-box-caption p-3">
              <div class="project-category text-white-50">
                Ginette 82 ans
              </div>
              <div class="project-name">
                N'a rien compris
              </div>
            </div>
          </a>
        </div>
      </div>

      
    </div>
  </section>














  <!-- Call to Action Section -->
  <section class="page-section bg-dark text-white">
    <div class="container text-center">
      <h2 class="mb-4">Abonne toi sur nos reseaux sociaux !</h2>


                 
           <style>#im10{width:100px; height:100px;margin-left:50px;}</style>
           <img src = "/static/img/portfolio/icone/facebook.png"/ id="im10">

                                
            <style>#im11{width:100px; height:100px;margin-left:100px;}</style>
           <img src = "/static/img/portfolio/icone/twitter.png"/ id="im11">

                  
           <style>#im12{width:200px; height:200px;margin-left:100px;}</style>
           <img src = "/static/img/portfolio/icone/snap.png"/ id="im12">
                    
    </div>
  </section>







  <!-- Contact Section -->
  <section class="page-section" id="contact">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-8 text-center">
          <h2 class="mt-0">Let's Get In Touch!</h2>
          <hr class="divider my-4">
          <p class="text-muted mb-5">Ready to start your next project with us? Give us a call or send us an email and we will get back to you as soon as possible!</p>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-4 ml-auto text-center">
          <i class="fas fa-phone fa-3x mb-3 text-muted"></i>
          <div>+1 (202) 555-0149</div>
        </div>
        <div class="col-lg-4 mr-auto text-center">
          <i class="fas fa-envelope fa-3x mb-3 text-muted"></i>
          <!-- Make sure to change the email address in anchor text AND the link below! -->
          <a class="d-block" href="mailto:contact@yourwebsite.com">contact@yourwebsite.com</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-light py-5">
    <div class="container">
      <div class="small text-center text-muted">Copyright &copy; 2019 - Start Bootstrap</div>
    </div>
  </footer>

  <!-- Bootstrap core JavaScript -->
  <script src="/static/vendor/jquery/jquery.min.js"></script>
  <script src="/static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Plugin JavaScript -->
  <script src="/static/vendor/jquery-easing/jquery.easing.min.js"></script>
  <script src="/static/vendor/magnific-popup/jquery.magnific-popup.min.js"></script>

  <!-- Custom scripts for this template -->
  <script src="/static/js/creative.min.js"></script>

</body>



    <script>
    var video = document.querySelector("#videoElement");
    if (navigator.mediaDevices.getUserMedia) {     
        navigator.mediaDevices.getUserMedia({video: true})
      .then(function(stream) {
        video.srcObject = stream;
      })
      .catch(function(err0r) {
        console.log("Something went wrong!");
      });
    }
    </script>







</html>
