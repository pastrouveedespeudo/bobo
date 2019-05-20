
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
          <h1 class="text-uppercase text-white font-weight-bold">Administrateur Pollution</h1>
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
  

      <center><input type='button' value='Retour Menu' id='menu' onclick='menu()'></center><br><br><br>
  
      <div class="row justify-content-center">
        <div class="col-lg-12 text-center">
          <h2 class="text-white mt-0"></h2>
          

        <div class="row">
        
         <div class="col-sm-12">
            <form method='POST' action='construction'>{% csrf_token %}
              <input type='button' value='Voir la database' id='Voir'>
            </form>
         </div>
        <br><br>

       </div>
       
      </div>
    </section>






    <script>

    function menu(){
      document.location.href="/admin_pollu/admin_pollu"; 
      }


    jQuery("#Voir").on("click", function(e){
            jQuery.ajax({
                data:{
                    'csrfmiddlewaretoken': '{{csrf_token}}' , 
                    'Voir':'Voir',
                    
             
                },
                type:"POST",
                url:"/admin_pollu/database"
            })
            .done(function(data){
                if (data.error){
                    jQuery("#monCadreAlert").text(data.error);
                    jQuery("#is_save");
                    
                    
                }
                else{
                    jQuery("#is_save").html(data.data);
                    jQuery("#monCadreAlert");
                    
  
                    
                    
                };
                
            });
        });
    
   </script>









  <!-- Call to Action Section -->
  <section class="page-section bg-dark text-white">
    <div class="container text-center">

      DATABASE ICIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII


                    
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
