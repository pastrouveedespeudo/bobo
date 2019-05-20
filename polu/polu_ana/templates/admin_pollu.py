
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Creative - Start Bootstrap Theme</title>

  <!-- Font Awesome Icons -->
  <link href="/static/vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet">
  <link href='https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic' rel='stylesheet' type='text/css'>

  <!-- Plugin CSS -->
  <link href="/static/vendor/magnific-popup/magnific-popup.css" rel="stylesheet">

  <!-- Theme CSS - Includes Bootstrap -->
  <link href="/static/css/creative.min.css" rel="stylesheet">
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.js"></script>

  
</head>




<body id="page-top">

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">

    
    
    <div class="container">
    
      <style> #my{width:50px; height:50px;margin-left:-70px;}</style>
      <img src="/static/img/portfolio2/icone/indian.png" id="my">
      <a class="navbar-brand js-scroll-trigger" href="/polution/polution">My_Polution</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

      <style>#my_prof{height:50px; height:50px;margin-left:-10px;}</style>
      <img src="/static/img/portfolio/icone/my.png" id="my_prof">
      <a class="navbar-brand js-scroll-trigger" href="/">My_Profil</a>
     
      
      <button class="navbar-toggler navbar-toggler-right" type="button"
        data-toggle="collapse" data-target="#navbarResponsive"
        aria-controls="navbarResponsive" aria-expanded="false"
        aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>






      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto my-2 my-lg-0">




          <style>
              #im1{width:50px; height:50px; margin-left:110px;}
              #graph{margin-left:35px; width:200px;}
          </style>
          
          <li class="nav-item">
            <a href = "/photo/photo">
              <img src="/static/img/portfolio2/icone/graphe.png" id="im1">
              <center><a class="nav-link js-scroll-trigger" href="/photo/photo" id='graph'>Nos graphiques</a></center>
            </a>
          </li>


          <style>
            #im2{width:50px;height:50px;margin-left:45px;}
            #donnée{width:200px;height:50px;margin-left:-25px;}
          </style>
          
          <li class="nav-item">
           <a href = "/polution/donnée">
            <img src="/static/img/portfolio2/icone/pol.png" id="im2">
            <center><a class="nav-link js-scroll-trigger" href="/polution/donnée" id='donnée'>Nos données pollution</a></center>
            </a>
          </li>


          <style>
              #impredi{width:50px;height:50px; margin-left:55px;}
              #prédiction{width:200px;height:50px; margin-left:-20px;}

          </style>

          <li class="nav-item">
            <a href = "/photo/coupe">
              <img src="/static/img/portfolio/icone/coiffure.png" id="impredi">
              <center><a class="nav-link js-scroll-trigger" href="/photo/coupe" id='prédiction'>Nos predictions</a></center>
            </a>
          </li>


          

          <style>
            #im3{width:50px;height:50px;margin-left:0px;}
            #imim{width:50px;height:50px;margin-left:68px;}
            #toususr{width:200px;height:50px;margin-left:0px;}
          </style>
          
          <li class="nav-item">
           <a href = "/photo/habits">
            <img src="/static/img/portfolio2/icone/pollution.png" id="imim">
            <center><a class="nav-link js-scroll-trigger" href="/polution/info_pollu" id='toususr'>Tous sur la pollution</a></center>
            </a>
          </li>

          <style>
            #im3{width:50px;height:50px;margin-left:25px;}
          </style>
          
          <li class="nav-item">
           <a href = "/photo/habits">
            <img src="/static/img/portfolio2/icone/fight.png" id="im3">
            <a class="nav-link js-scroll-trigger" href="/photo/habits">Comment lutter ?</a>
            </a>
          </li>


          
        </ul>

        
      </div>
    </div>
  </nav>







  <!-- Masthead -->
  <header class="masthead">
    <div class="container h-100">
      <div class="row h-100 align-items-center justify-content-center text-center">
        <div class="col-lg-10 align-self-end">
          <h1 class="text-uppercase text-white font-weight-bold">Pollution</h1>
          <br>
          <style>#h{font:Serif; color:white;}</style>
          <hr class="divider my-4">
        </div>
        <div class="col-lg-8 align-self-baseline">
          <p class="text-white-75 font-weight-light mb-5"></p>
          
  
          
        </div>
      </div>
    </div>
  </header>



  <!-- About Section -->
  <section class="page-section bg-primary" id="about">
    <div class="container">


      <div class="row justify-content-center">
        <div class="col-lg-12 text-center">
          <h2 class="text-white mt-0"></h2>
          



        <div class="row">

          
          <div class="col-sm-4">
          
            <h5>Taux de pollution de particules fines à Lyon</h5><br><br>
            <center><input type='button' value='Voir les données' onclick='donnée_lyon()'></center>
            <center><strong><h5>{{lyon}}</h5></strong></center><br>
            
          </div>
          
          <div class="col-sm-4">
          
              <h5>Taux de pollution de particules fines à Paris</h5><br><br>
              <center><input type='button' value='Voir les données' onclick='donnée_paris()'></center>
              <center><strong><h5>{{paris}}</h5></strong></center><br>
              
          </div>

          <div class="col-sm-4">
          
              <h5>Taux de pollution de particules fines à Marseille</h5><br><br>
              <center><input type='button' value='Voir les données' onclick='donnée_marseille()'></center>
              <center><strong><h5>{{marseille}}</h5></strong></center><br>
              
          </div>


      </div>


       <br><br>

       <div id='info1' style='display:none;'>

          Météo de Lyon :  {{météo_lyon}}<br><br>
          Vent de Lyon  :  {{vent_lyon}} m/s <br><br>
          Température de Lyon  :  {{température_lyon}} degrès <br><br>
          Pression de Lyon  :  {{pression_lyon}} hpa <br><br>
          Saison actuelle : {{saison_actuelle}}<br><br>
          départ à routier à Lyon :  {{départ_routier_lyon}}<br><br>
          heure de pointe à lyon :  {{heure_pointe_lyon}}<br><br>
          c'est jour regulier à lyon :  {{regulier_jour_lyon}}<br><br>
          ce n'est pas une heure de pointe à lyon :  {{non_pointe_lyon}}<br><br>
          Week end :  {{weekend}}<br><br>
          Jour de semaine :  {{jour_semaine}}<br><br>
          Rang de la ville la plus polluée en France  :  {{classement_lyon}} / 20 <br><br>
          Site industrielle les plus polluant de France :  {{pole_lyon}}<br><br>
          Manifestation en ce moment à Lyon :  {{manif_lyon}} <br><br>
          Population active de 15 à 59 ans:  {{socio_lyon}} personnes<br><br>
          Bouchons à Lyon :  {{bouchons_lyon}} Km

        
        <br><br><br><br>
        <div style='float:left;'><i>Donnée fournis par openweathermap :
        <a href="https://openweathermap.org/" style='color:black;'> <i>openweathermap</i>
        </a></i></div><br>

        <div style='float:left;'>
        <i>Classement de 1 a 7 des villes les plus polluée :</i>
        <a href="http://www.linternaute.com/ville/c-ville-pollution-de-l-air"
         style='color:black;'><i>Internaute</a></i></div><br>


        <div style='float:left;'><i>Classement des sites industriels les plus pollués : 
        </i><a href="https://www.greenunivers.com/2009/05/quinze-sites-industriels-plus-pollueurs-de-france-6981/"
        style='color:black;'><i>Grenunivers</a></i></div><br>

        <div style='float:left;'><i>Manifestation à lyon : </i>
        <a href="https://www.onlymoov.com/trafic/" style='color:black;'><i>onlymoov</a></i></div><br>

        <div style='float:left;'><i>Bouchons à lyon : </i>
        <a href="https://www.moncoyote.com/fr/info-trafic-lyon.html"
          style='color:black;'><i>moncoyote</a></i></div><br>

      </div>



      
      <div id='info2' style='display:none;'>
        Météo de Paris :  {{météo_paris}}<br><br>
        Vent de Paris :  {{vent_paris}} m/s<br><br>
        Température de Paris  :  {{température_paris}} degrès <br><br>
        Pression de Paris  :  {{pression_paris}} hpa <br><br>
        Saison actuelle : {{saison_actuelle}}<br><br>
        départ à routier à Paris :  {{départ_routier_paris}}<br><br>
        heure de pointe à Paris :  {{heure_pointe_paris}}<br><br>
        c'est jour regulier à Paris :  {{regulier_jour_paris}}<br><br>
        ce n'est pas une heure de pointe à Paris :  {{non_pointe_paris}}<br><br>
        Week end :  {{weekend}}<br><br>
        Jour de semaine :  {{jour_semaine}}<br><br>
        Rang de la ville la plus polluée en France  :  {{classement_paris}} / 20 <br><br>
        Site industrielle les plus polluant de France :  {{pole_paris}}<br><br>
        Manifestation en ce moment à Paris :  {{manif_paris}} <br><br>
        Population active de 15 à 59 ans:  {{socio_paris}} personnes<br><br>
        Bouchons à Paris :  {{bouchons_paris}} Km

        <br><br><br><br>
        <div style='float:left;'><i>Donnée fournis par openweathermap</i></div><br>

        <div style='float:left;'>
        <i>Classement de 1 a 7 des villes les plus polluée :</i>
        <a href="http://www.linternaute.com/ville/c-ville-pollution-de-l-air"
         style='color:black;'><i>Internaute</a></i></div><br>


        <div style='float:left;'><i>Classement des sites industriels les plus pollués :</i>
        <a href="https://www.greenunivers.com/2009/05/quinze-sites-industriels-plus-pollueurs-de-france-6981/"
          style='color:black;'><i>Grenunivers</a></i></div><br>

        <div style='float:left;'><i>Bouchons à lyon : </i>
        <a href="https://www.moncoyote.com/fr/info-trafic-lyon.html"
          style='color:black;'><i>moncoyote</a></i></div><br>
          
        <div style='float:left;'><i>Manifestation à Patis : </i>
        <a href="https://paris.demosphere.net/manifestations-paris"
        style='color:black;'><i>demosphere</a></i></div><br>


      </div>



      <div id='info3' style='display:none;'>
        Météo de Marseille :  {{météo_marseille}}<br><br>
        Vent de Marseille :  {{vent_marseille}} m/s<br><br>
        Température de marseille  :  {{température_marseille}} degrès <br><br>
        Pression de marseille  :  {{pression_marseille}} hpa <br><br>
        Saison actuelle : {{saison_actuelle}}<br><br>
        départ à routier à marseille :  {{départ_routier_marseille}}<br><br>
        heure de pointe à marseille :  {{heure_pointe_marseille}}<br><br>
        c'est jour regulier à marseille :  {{regulier_jour_marseille}}<br><br>
        ce n'est pas une heure de pointe à marseille :  {{non_pointe_marseille}}<br><br>
        Week end :  {{weekend}}<br><br>
        Jour de semaine :  {{jour_semaine}}<br><br>
        Rang de la ville la plus polluée en France  :  {{classement_marseille}} / 20 <br><br>
        Site industrielle les plus polluant de France :  {{pole_marseille}}<br><br>
        Manifestation en ce moment à marseille :  {{manif_marseille}} <br><br>
        Population active de 15 à 59 ans:  {{socio_marseille}} personnes<br><br>
        Bouchons à marseille :  {{bouchons_marseille}} Km

        
        <br><br><br><br>
        <div style='float:left;'><i>Donnée fournis par openweathermap</i></div>

        <div style='float:left;'>
        <i>Classement de 1 a 7 des villes les plus polluée :</i>
        <a href="http://www.linternaute.com/ville/c-ville-pollution-de-l-air"
         style='color:black;'><i>Internaute</a></i></div><br>


        <div style='float:left;'><i>Classement des sites industriels les plus pollués :</i>
        <a href="https://www.greenunivers.com/2009/05/quinze-sites-industriels-plus-pollueurs-de-france-6981/"
          style='color:black;'><i>Grenunivers</a></i></div><br>

        <div style='float:left;'><i>Bouchons à lyon : </i>
        <a href="https://www.moncoyote.com/fr/info-trafic-lyon.html"
          style='color:black;'><i>moncoyote</a></i></div><br>
          
        <div style='float:left;'><i>Manifestation à Marseille :</i>
        <a href="https://mars-infos.org/spip.php?page=agenda"
          style='color:black;'><i>mars-info</a></i></div><br>


          
        </div>



      <br><br><br><br><br><br>
      <div style='float:left;'><i>Données issuent de <a href='http://www.airlab.solutions/fr'
          style='color:black;'>plumairlab
          </a></i>
      </div>

        
    </div>
  </section>


  
  <script>
    function donnée_lyon(){
      document.getElementById('info2').style.display = 'none';
      document.getElementById('info3').style.display = 'none';
      document.getElementById('info1').style.display = 'block';
      };     

    function donnée_paris(){
      document.getElementById('info1').style.display = 'none';
      document.getElementById('info3').style.display = 'none';
      document.getElementById('info2').style.display = 'block';
     };

    function donnée_marseille(){
      document.getElementById('info1').style.display = 'none';
      document.getElementById('info2').style.display = 'none';
      document.getElementById('info3').style.display = 'block';
    };
      
  </script>



      </div>
    </div>
  </section>







  
 
  <!-- Services Section -->
  <section class="page-section" id="services">
  
    <div class="container">
    
      <h2 class="text-center mt-0">Mes services</h2>
      <hr class="divider my-4">


      
      <div class="row">
        <div class="col-lg-3 col-md-6 text-center">
          <div class="mt-5">
           <style>#im6{width:100px; height:100px;}</style>
           <img src = "/static/img/portfolio2/icone/graphe.png"/ id="im6">
            <h3 class="h4 mb-2">Un recit sans preuve ca sert a rien...</h3>
            <p class="text-muted mb-0">Nos graphiques</p>
          </div>
        </div>



        
        <div class="col-lg-3 col-md-6 text-center">
          <div class="mt-5">
           <style>#im4{width:100px; height:100px;}</style>
           <img src = "/static/img/portfolio2/icone/pol.png"/ id="im4">
            <h3 class="h4 mb-2">Nos données</h3>
            <br>
            <p class="text-muted mb-0">Nos données pollution</p>
          </div>
        </div>

        
        <div class="col-lg-3 col-md-6 text-center">
          <div class="mt-5">
           <style>#im5{width:100px; height:100px;}</style>
           <img src = "/static/img/portfolio/icone/coiffure.png"/ id="im5">
            <h3 class="h4 mb-2">qui... ne marche pas super..</h3>
            <p class="text-muted mb-0">Nos prédictions</p>
          </div>
        </div>

        
        <div class="col-lg-3 col-md-6 text-center">
          <div class="mt-5">
           <style>#im7{width:100px; height:100px;}</style>
           <img src = "/static/img/portfolio2/icone/pollution.png"/ id="im7">
            <h3 class="h4 mb-2">La pollution ! ah enfete c'est quoi ? </h3>
            <br>
            <p class="text-muted mb-0">Tous absolument tous sur la polltuion </p>
          </div>
        </div>

        <div class="col-lg-3 col-md-6 text-center">
          <div class="mt-5">
           <style>#im7{width:100px; height:100px;}</style>
           <img src = "/static/img/portfolio2/icone/fight.png"/ id="im7">
            <h3 class="h4 mb-2">Notre solution</h3>
            <br>
            <p class="text-muted mb-0">Luttons</p>
          </div>
        </div>


        

        
      </div>
    </div>
  </section>





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











</html>
