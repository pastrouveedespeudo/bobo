


  //Functions who changes picture to an other picture and
  //the color of the text. (One function for one picture... yes not really smart...)
  // ---> Visual function <--- en gros tu passes dessus ca change l'image et le texte
  function mode_div3(div, image){
    document.getElementById(image).style.width = '70px';
    document.getElementById(image).style.height = '70px';
    document.getElementById(div).style.color = '#330000';
  };
  
  function mode_div4(div, color, image, largeur, hauteur){
    document.getElementById(image).style.width = largeur;
    document.getElementById(image).style.height = hauteur;
    document.getElementById(div).style.color = 'black';
  };
    
  function mode_div(div, image, largeur, hauteur){
    a = document.getElementById(image).width;
    b = document.getElementById(image).height;
    document.getElementById(image).width = a + largeur;
    document.getElementById(image).height = b + hauteur;
    document.getElementById(div).style.color = 'red'; 
  };
  
  function mode_div2(div, color, image, largeur, hauteur){
    document.getElementById(div).style.color = color;
    document.getElementById(image).width = largeur;
    document.getElementById(image).height = hauteur;
  };
  function change_image_tendance1(div, image){ 
    document.getElementById('p_mode').style.color = '#330000';
    document.getElementById('momode').src = "/static/img/portfolio/icone/momode2.png";
  };
  
  function change_image_tendance2(div, image){
    document.getElementById('p_mode').style.color = 'black';
    document.getElementById('momode').src = "/static/img/portfolio/icone/momode.png";
  };
  
  function change_image_coiff1(div, image){  
    document.getElementById('coif_p').style.color = '#330000';
    document.getElementById('coif_nav').src = "/static/img/portfolio/icone/coiffure2.png";
  };
  
  function change_image_coiff2(div, image){
    document.getElementById('coif_p').style.color = 'black';
    document.getElementById('coif_nav').src = "/static/img/portfolio/icone/coiffure.png";
  };
  
  function change_image_vetements1(div, image){   
    document.getElementById('p_vet').style.color = '#330000';
    document.getElementById('im3').src = "/static/img/portfolio/icone/vetements2.png";
  };
  
  function change_image_vetements2(div, image){
    document.getElementById('p_vet').style.color = 'black';
    document.getElementById('im3').src = "/static/img/portfolio/icone/vetements.png";
  };
  
  function change_image_logout1(div, image){  
    document.getElementById('p_deco').style.color = '#330000';
    document.getElementById('deco_nav').src = "/static/img/portfolio/icone/logout2.png";
  };
  
  function change_image_logout2(div, image){
    document.getElementById('p_deco').style.color = 'black';
    document.getElementById('deco_nav').src = "/static/img/portfolio/icone/deco.png";
  };
  
  function change_image_inscription1(div, image){  
    document.getElementById('p_inscri').style.color = '#330000';
    document.getElementById('ima1').src = "/static/img/portfolio/icone/yoyo.png";
  };
  
  function change_image_inscription2(div, image){
    document.getElementById('p_inscri').style.color = 'black';
    document.getElementById('ima1').src = "/static/img/portfolio/icone/inscription.png";
  };
  
  function change_image_co1(div, image){
    document.getElementById('p_con').style.color = '#330000';
    document.getElementById('im2').src = "/static/img/portfolio/icone/inscri.png";
  };
  
  function change_image_co2(div, image){
    document.getElementById('p_con').style.color = 'black';
    document.getElementById('im2').src = "/static/img/portfolio/icone/login.png";
  };
  
  function change_image_foiiiif1(div, image){ 
    document.getElementById('p_coicoif').style.color = '#330000';
    document.getElementById('im1').src = "/static/img/portfolio/icone/hairhair.png";
  };
  
  function change_image_foiiiif2(div, image){
    document.getElementById('p_coicoif').style.color = 'black';
    document.getElementById('im1').src = "/static/img/portfolio/icone/coiffure.png";
  };
  
  function change_image_drees1(div, image){
    document.getElementById('p_vetvet').style.color = '#330000';
    document.getElementById('im3').src = "/static/img/portfolio/icone/dressme.png";
  };
  
  function change_image_drees2(div, image){
    document.getElementById('p_vetvet').style.color = 'black';
    document.getElementById('im3').src = "/static/img/portfolio/icone/vetements.png";
  };

