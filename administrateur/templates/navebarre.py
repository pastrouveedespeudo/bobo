<!DOCTYPE html>
  <html lang="en">

    <head>

      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <meta name="description" content="">
      <meta name="author" content="">

      <title>Magazine virtuel</title>

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


    <style>#my_prof{height:50px; height:50px;margin-left:-10px;}</style>
    <style>#my{width:50px;height:50px;}</style>
    <style>#im1{width:50px;height:50px;margin-left:55px;}</style>
    <style>#coif_nav{width:50px; height:50px; margin-left:30px;}</style>
    <style>#im2{width:50px;height:50px;margin-left:40px;}</style>
    <style>#im3{width:50px; height:50px; margin-left:40px;}</style>
    <style>#im4{width:50px;height:50px;margin-left:40px;}</style>
    <style>#h{font:Serif; color:white;}</style>
    <style>#im6{width:100px; height:100px;}</style>
    <style>#deco_nav{width:50px; height:50px; margin-left:46px;}</style>
    <style>#autre{margin-left:-965px;margin-top:-100px;}</style>
    <style>#h{font:Serif; color:white;}</style>
    <style>#momode{width:65px; height:50px;margin-left:90px;}</style>
        
    <div class="container">

      <img src="/static/img/portfolio/icone/my.png" id="my_prof">
      <a class="navbar-brand js-scroll-trigger" href="/">
        My_Profil
      </a>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  
      <img src="/static/img/portfolio2/icone/indian.png" id="my">
      <a class="navbar-brand js-scroll-trigger" href="/polution/polution">
        My_pollution
      </a>
      
      <button class="navbar-toggler navbar-toggler-right" type="button"
        data-toggle="collapse" data-target="#navbarResponsive"
        aria-controls="navbarResponsive" aria-expanded="false"
        aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
      </button>
      
      <div class="collapse navbar-collapse" id="navbarResponsive">

          <ul class="navbar-nav ml-auto my-2 my-lg-0">

              {% if user.is_authenticated %}

              <li class="nav-item">
                  <img src="/static/img/portfolio/icone/momode.png" id="momode">
                  <a class="nav-link js-scroll-trigger" href="/administrateur/tendance">
                    <center>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;La tendance du moment ?</center>
                  </a>
              </li>

              <li class="nav-item">
                  <img src="/static/img/portfolio/icone/coiffure.png" id="coif_nav">
                  <a class="nav-link js-scroll-trigger" href="/photo/coupe">
                    <center>Mes coiffures</center>
                  </a>
              </li>

              <li class="nav-item">
                  <img src="/static/img/portfolio/icone/vetements.png" id="im3">
                  <a class="nav-link js-scroll-trigger" href="/photo/habits">
                    <center>Mes vetements</center>
                  </a>
              </li>

              <li class="nav-item">
                  <img src="/static/img/portfolio/icone/deco.png" id="deco_nav">
                  <a class="nav-link js-scroll-trigger" href="/accounts/logout_view">
                    <center>Se déconnecter</center>
                  </a>
              </li>
      
          </ul>

            {% else %}

              <style>#ima1{width:55px; height:50px; margin-left:17px;}</style>
              <style>#im2{width:50px; height:50px; margin-left:40px;}</style>
              <style>#im1{width:50px; height:50px; margin-left:45px;}</style>
              <style>#im3{width:50px; height:50px; margin-left:40px;}</style>
              
              <li class="nav-item">
                  <img src="/static/img/portfolio/icone/inscription.png" id="ima1">
                  <a class="nav-link js-scroll-trigger" href="/accounts/register_view">
                    S'inscrire
                  </a>
              </li>

              <li class="nav-item">
                  <img src="/static/img/portfolio/icone/login.png" id="im2">
                  <a class="nav-link js-scroll-trigger" href="/accounts/login">
                    Se connecter
                  </a>
              </li>

              
              <li class="nav-item">
                  <img src="/static/img/portfolio/icone/coiffure.png" id="im1">
                  <a class="nav-link js-scroll-trigger" href="/photo/coupe">
                    Les coiffures
                  </a>
              </li>

              <li class="nav-item">
                  <img src="/static/img/portfolio/icone/vetements.png" id="im3">
                  <a class="nav-link js-scroll-trigger" href="/photo/habits">
                    Les vetements
                  </a>
              </li>
              
          </ul>

          {% endif %}

      
          
      </div>
    </div>
  </nav>
</html>
