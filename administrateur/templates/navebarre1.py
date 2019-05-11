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

    <style>
      #my{
        width:50px;
        height:50px;
    }
    </style>
    
    <div class="container">
    
      <img src="/static/img/portfolio/icone/my.png" id="my">
      <a class="navbar-brand js-scroll-trigger" href="/">My_Profil</a>
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      
      <img src="/static/img/portfolio2/icone/indian.png" id="my">
      <a class="navbar-brand js-scroll-trigger" href="/polution/polution">My_pollution</a>
      
      <button class="navbar-toggler navbar-toggler-right" type="button"
      data-toggle="collapse" data-target="#navbarResponsive"
      aria-controls="navbarResponsive" aria-expanded="false"
      aria-label="Toggle navigation">
      
        <span class="navbar-toggler-icon"></span>
        
      </button>

      
      <div class="collapse navbar-collapse" id="navbarResponsive">

      
        <ul class="navbar-nav ml-auto my-2 my-lg-0">
            
        {% if user.is_authenticated %}
        
          <style>#im1{width:50px; height:50px; margin-left:60px;}</style>

          <li class="nav-item">
            <a href = "/photo/photo">
              <img src="/static/img/portfolio/icone/photo.png" id="im1">
              <a class="nav-link js-scroll-trigger" href="/photo/photo">Prendre une photo</a>
            </a>
          </li>

          <style>#im2{width:50px; height:50px; margin-left:40px;}</style>
          
          <li class="nav-item">
           <a href = "/photo/mes_images">
            <img src="/static/img/portfolio/icone/mes_images.png" id="im2">
            <a class="nav-link js-scroll-trigger" href="/photo/mes_images">Mes images</a>
            </a>
          </li>

          <style>#im1{width:50px; height:50px; margin-left:45px;}</style>

          <li class="nav-item">
            <a href = "/photo/coupe">
              <img src="/static/img/portfolio/icone/coiffure.png" id="im1">
              <a class="nav-link js-scroll-trigger" href="/photo/coupe">Mes_coiffures</a>
            </a>
          </li>


          <style>#im3{width:50px; height:50px; margin-left:40px;}</style>

          
          <li class="nav-item">
           <a href = "/photo/habits">
            <img src="/static/img/portfolio/icone/vetements.png" id="im3">
            <a class="nav-link js-scroll-trigger" href="/photo/habits">Mes vetements</a>
            </a>
          </li>

          <li class="nav-item">
            <a href = "/photo/photo">
              <img src="/static/img/portfolio/icone/deco.png" id="im1">
              <a class="nav-link js-scroll-trigger" href="/photo/photo">Se déconnecter</a>
            </a>
          </li>
          
        </ul>

        {% else %}

          <style>#ima1{width:55px; height:50px; margin-left:17px;}</style>

          <li class="nav-item">
            <a href = "/photo/photo">
              <img src="/static/img/portfolio/icone/inscription.png" id="ima1">
              <a class="nav-link js-scroll-trigger" href="/accounts/register_view">S'inscrire</a>
            </a>
          </li>

          <style>#im2{width:50px; height:50px; margin-left:40px;}</style>
          
          <li class="nav-item">
           <a href = "/photo/mes_images">
            <img src="/static/img/portfolio/icone/login.png" id="im2">
            <a class="nav-link js-scroll-trigger" href="/accounts/login">Se connecter</a>
            </a>
          </li>

          <style>#im1{width:50px; height:50px; margin-left:45px;}</style>

          <li class="nav-item">
            <a href = "/photo/coupe">
              <img src="/static/img/portfolio/icone/coiffure.png" id="im1">
              <a class="nav-link js-scroll-trigger" href="/photo/coupe">Les coiffures</a>
            </a>
          </li>


          <style>#im3{width:50px; height:50px; margin-left:40px;}</style>

          
          <li class="nav-item">
           <a href = "/photo/habits">
            <img src="/static/img/portfolio/icone/vetements.png" id="im3">
            <a class="nav-link js-scroll-trigger" href="/photo/habits">Les vetements</a>
            </a>
          </li>
        </ul>

        {% endif %}
        
      </div>
    </div>
  </nav>


