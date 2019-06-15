
LISTE_RESIZE = []
LISTE_RESIZE_TAILLE_HAUTEUR = []
LISTE_RESIZE_TAILLE_LARGEUR = []

LISTE1 = []

LISTE_INFO_COULEUR = []
var click = 0;
var click2 = 0;
var click_salopette = 0;
var click_jean = 0;
var click_toile = 0;



$( function() {
        $("#1, #2, #3, #4, #5, #6, #7, #8, #9, #10, #profil").draggable();
   });


  $( function() {
    $("#11, #22, #33, #44, #55, #66, #77, #88, #99, #1010, #1111, #1212").draggable();
  });


  $( function() {
     $("#111, #222, #333, #444, #555, #666, #777, #888, #999, #101010").draggable();
  });


 $( function() {
     $("#1111, #2222, #3333, #4444, #5555, #6666, #7777, #8888, #9999, #10101010").draggable();
});


function ajout_longueur(){
  
  var a = LISTE_RESIZE[LISTE_RESIZE.length -1]
  
  console.log(LISTE_RESIZE[LISTE_RESIZE.length -1])
  
  var b = document.getElementById(a).id
  console.log(b, 'b')
  
  var c = '#' + b
  console.log(c)
  var image = document.querySelector(c);
  var X = image.getAttribute("width");
  X = parseInt(X) ;
  console.log(X)
  var Y = image.getAttribute("height"); 		
  Y = parseInt(Y) ;
  console.log(Y)
  
  X += 0 ; 
  Y += 5 ;
  image.setAttribute('width', X);
  image.setAttribute('height',Y);
  var d = document.getElementById(b).style.height = Y;


  document.getElementById(b).style.width = X;
  
  LISTE1.push([b, X,Y]);

};


function ajout_largeur(){
  

  var a = LISTE_RESIZE[LISTE_RESIZE.length -1]
  var b = document.getElementById(a).id
  var c = '#' + b

  var image = document.querySelector(c);
  var X = image.getAttribute("width");
  X = parseInt(X) ;

  var Y = image.getAttribute("height"); 		
  Y = parseInt(Y) ;
 

  X += 5 ; 
  Y += 0 ;
  image.setAttribute('width', X);
  image.setAttribute('height',Y);
  LISTE1.push([b, X,Y]);
  console.log(LISTE1[LISTE1.length-1])
  console.log(X,Y)
  
};


function enlever_longueur(){
  var a = LISTE_RESIZE[LISTE_RESIZE.length -1]
  var b = document.getElementById(a).id
  var c = '#' + b

  var image = document.querySelector(c);
  var X = image.getAttribute("width");
  X = parseInt(X) ;

  var Y = image.getAttribute("height"); 		
  Y = parseInt(Y) ;
 

  X += 0 ; 
  Y -= 5 ;
  image.setAttribute('width', X);
  image.setAttribute('height',Y);
  LISTE1.push([b, X,Y]);

};

function enlever_largeur(){

  var a = LISTE_RESIZE[LISTE_RESIZE.length -1]
  var b = document.getElementById(a).id
  var c = '#' + b

  var image = document.querySelector(c);
  var X = image.getAttribute("width");
  X = parseInt(X) ;

  var Y = image.getAttribute("height"); 		
  Y = parseInt(Y) ;
 

  X -= 5 ; 
  Y += 0 ;
  image.setAttribute('width', X);
  image.setAttribute('height',Y);
  LISTE1.push([b, X,Y]);
  
};
    

liste_info_prix = [['bb1' ,'xxx', '<a href="" style="color:white;">www.xxx.fr</a>', '2550 euros', 'en stock', 'xxx', '<img src="/static/img/portfolio/vetement/femme/bas_blanc/1.png" style="height:200px>"'],
                   ['bb2' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '5520 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_blanc/2.2.png style='height:200px'>"],
                   ['bb3' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '280 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_blanc/3.png' style='height:200px'>"],
                   ['bb4' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '25580 euros', 'épuisé', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_blanc/4.png' style='height:200px'>"],
                   ['bb5' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '280 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_blanc/5.png' style='height:200px'>"],
                   ['bb6' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '290 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_blanc/6.png'> style='height:200px'>"],
                   ['bb7' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '20 euros', 'épuisé', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_blanc/7.png' style='height:200px'>"],
                   ['bb8' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '20 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_blanc/8.png' style='height:200px'>"],
                   ['bb9' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '290 euros', 'épuisé', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_blanc/9.png' style='height:200px'>"],
                   ['bb10' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '23660 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_blanc/10.png style='height:200px'>"],
                   ['bbl1' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '20 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_bleu/1.png' style='height:200px'>"],
                   ['bbl2' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '280 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_bleu/2.png' style='height:200px'>"],
                   ['bbl3' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '47 euros', 'en stock', 'xxx', " <img src='/static/img/portfolio/vetement/femme/bas_bleu/3.png' style='height:200px'>"],
                   ['bbl4' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '240 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_bleu/4.png' style='height:200px'>"],
                   ['bbl5' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '274874 euros', 'épuisé', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_bleu/5.png' style='height:200px'>"],
                   ['bbl6' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '26848 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_bleu/6.png' style='height:200px'>"],
                   ['bbl17' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '2048 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_bleu/7.png' style='height:200px'>"],
                   ['bbl8' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '2064548 euros', 'en stock', 'xxx', " <img src='/static/img/portfolio/vetement/femme/bas_bleu/8.png' style='height:200px'>"],
                   ['bbl10' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '2588 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_bleu/10.png' style='height:200px'>"],
                   ['bbl11' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '255 euros', 'épuisé', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_bleu/11.png' style='height:200px'>"],
                   ['bbl12' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '550 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/bas_bleu/12.png' style='height:200px'>"],
                   ['hb1' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '2088 euros', 'épuisé', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_blanc/1.png' style='height:200px'>"],
                   ['hb2' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '2000 euros', 'épuisé', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_blanc/2.png' style='height:200px'>"],
                   ['hb3' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '2155 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_blanc/3.png' style='height:200px'>"],
                   ['hb4' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '2015 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_blanc/4.png' style='height:200px'>"],
                   ['hb5' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '20789 euros', 'épuisé', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_blanc/5.png' style='height:200px'>"],
                   ['hb7' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '2121 euros', 'épuisé', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_blanc/6.png' style='height:200px'>"],
                   ['hb8' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '1987 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_blanc/7.png' style='height:200px'>"],
                   ['hb9' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '231 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_blanc/9.png' style='height:200px'>"],
                   ['hb10' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '890 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_blanc/10.png' style='height:200px'>"],
                   ['hg1' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '17 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_gris/1.png' style='height:200px'>"],
                   ['hg2' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '202102 euros', 'épuisé', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_gris/2.png' style='height:200px'>"],
                   ['hg3' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '2084 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_gris/3.png' style='height:200px'>"],
                   ['hg4' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '200 euros', 'épuisé', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_gris/4.png' style='height:200px'>"],
                   ['hg5' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '23 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_gris/5.png' style='height:200px'>"],
                   ['hg6' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '15 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_gris/6.png' style='height:200px'>"],
                   ['hg7' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '17 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_gris/7.png' style='height:200px'>"],
                   ['hg8' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '18 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_gris/8.png' style='height:200px'>"],
                   ['hg9' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '19 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_gris/9.png' style='height:200px'>"],
                   ['hg10' ,'xxx', '<a href="" style="color:white;">www.my_profil.com</a>', '21 euros', 'en stock', 'xxx', "<img src='/static/img/portfolio/vetement/femme/haut_gris/10.png' style='height:200px'>"],
                   ]



function inf(image){

for(var i = 0; i < liste_info_prix.length; i ++){
  if(image == liste_info_prix[i][0]){
 
    document.getElementById('name').innerHTML = 'Nom: ' + liste_info_prix[i][5]
    document.getElementById('store').innerHTML = 'Magasin: ' + liste_info_prix[i][1]
    document.getElementById('online').innerHTML = 'En ligne: ' + liste_info_prix[i][2]
    document.getElementById('price').innerHTML = 'Prix: ' + liste_info_prix[i][3]
    document.getElementById('stock').innerHTML =  'En stock: ' + liste_info_prix[i][4]
    document.getElementById('mage').innerHTML =  liste_info_prix[i][6]
  }
}


};



function nom_image(id_im){
  console.log(id_im)
  var a = document.getElementById(id_im).height;
  var b = document.getElementById(id_im).width;
  
  LISTE_RESIZE.push(id_im)
  LISTE1.push([id_im, a, b])

  
  console.log(LISTE_RESIZE)
  console.log(LISTE1)

  inf(id_im)
};



  var HAUT = 'habit_bas_blanc'
  var BAS = 'habit_bas_blanc'
  function coul(couleur){

    document.getElementById('couleur').style.display = 'block';
    document.getElementById('couleur').innerHTML = 'Vous etes donc ' + couleur;

    if(couleur == 'brune'){
      document.getElementById('info_mode').innerHTML = 'Le haut blanc et le bas bleu !'
    }
    else if(couleur == 'blonde'){
      document.getElementById('info_mode').innerHTML = 'Le haut gris et le bas bleu !';
    }
    else if(couleur == 'chatain'){
      document.getElementById('info_mode').innerHTML = 'Le haut blanc et le bas blanc !';
    } 
    else if(couleur == 'rousse'){
      document.getElementById('info_mode').innerHTML = 'Le haut blanc et le bas blanc !';
    }
    else if(couleur == 'noire'){
      document.getElementById('info_mode').innerHTML = 'Le haut blanc et le bas bleu !';
    }
   

    var a = document.getElementById('couleur').innerHTML;
   
  };



  jQuery("#brune, #blonde, #chatain, #rousse, #noire").on("click", function(e){
    
    var a = document.getElementById('couleur').innerHTML;
    var b = document.getElementById('recherche').innerHTML;
    

    
    document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Appuyer sur votre couleur de cheveux, et choississez une catégorie d'habit</i></strong></p>"
    

    
     e.preventDefault();
     
      jQuery.ajax({
          data:{
              'csrfmiddlewaretoken': 'vrS3jiKMco5HjUgoQlNOQtDEUWWnq0Dg9jqGC5ECVvtI5mWHXmWtvrZBN09F9AMP' , 
              'a':a,
              'b':b
          },
          type:"POST",
          url:"/photo/habits"
      })
      .done(function(data){
          if (data.error){
              jQuery("#monCadreAlert").text(data.error);
              jQuery("#is_save");
              
              
          }
          else{
              jQuery("#habit").html(data.data);
              jQuery("#monCadreAlert");
              console.log(data);
              liste1 = [[],[]]
              var c = 0;
              for(var i = 0; i < data.length; i ++){
          
                liste1[c].push(data[i])
                if(data[i] == ' '){
                    c += 1
                  }

                }

              var haut = 'habit_haut_' + liste1[0].join('').slice(0,-1)
              var bas = 'habit_bas_' + liste1[1].join('')
              HAUT = haut
              BAS = bas
              
              console.log(liste1[liste1.length - 1].join(''))
              console.log(liste1[liste1.length - 2].join(''))

              LISTE_INFO_COULEUR.push(liste1[liste1.length - 1].join(''))
              LISTE_INFO_COULEUR.push(liste1[liste1.length - 2].join(''))

            

          };
          
      });
  });




function voir_pantalon(){
  

  if(click % 2 == 0){

    document.getElementById('pantalon_div').innerHTML = "<br><input type='button' value='Pantalon'" +
                                                        'style="border:3px solid black;font-family:segoe print;"' +
                                                         "onclick='voir_pantalon()'><br><br>" +
                                                        "<div>"+
                                                        "<input type='button' value='Salopette' id='salopette'"+
                                                          'style=" border:3px solid black;font-family:segoe print;"'+
                                                          "onclick='voir_salopette()'>&nbsp&nbsp" +
                                                        "</div><br>" +
                                                        "<div>" +
                                                        "<input type='button' value='Jeans' id='jean'" +
                                                          'style=" border:3px solid black;font-family:segoe print;"' +
                                                          "onclick='voir_jean()'>" +
                                                       "</div><br>" +
                                                        "<div>" +
                                                        "<input type='button' value='Toile' id='toile'" +
                                                          'style=" border:3px solid black;font-family:segoe print;"' +
                                                          "onclick='voir_toile()'>" +
                                                        "</div><br>";

    click += 1
    }
  else{
    document.getElementById('pantalon_div').innerHTML = "<br><input type='button' value='Pantalon'" +
                                                        'style="border:3px solid black;font-family:segoe print;"' +
                                                         "onclick='voir_pantalon()'><br><br>";
    click += 1
  };
};



function voir_shirt(){

  if(click2 % 2 == 0){

    document.getElementById('tshirt').innerHTML = "<br><input type='button' value='tshirt'" +
                                                        'style="border:3px solid black;font-family:segoe print;"' +
                                                         "onclick='voir_shirt()'><br><br>" +
                                                        "<div>"+
                                                        "<input type='button' value='manche longue' id='longue'"+
                                                          'style=" border:3px solid black;font-family:segoe print;"'+
                                                          "onclick='voir_t_longue()'>&nbsp&nbsp" +
                                                        "</div>" +
                                                        "<div>" +
                                                        "<input type='button' value='manche courte' id='courte'" +
                                                          'style=" border:3px solid black;font-family:segoe print;"' +
                                                          "onclick='voir_t_courte()'>" +
                                                       "</div><br>" +
                                                        "<div>" +
                                                        "<input type='button' value='laine' id='laine'" +
                                                          'style=" border:3px solid black;font-family:segoe print;"' +
                                                          "onclick='voir_t_laine()'>" +
                                                        "</div><br>";

    click2 += 1
    }
  else{
    document.getElementById('tshirt').innerHTML = "<br><input type='button' value='tshirt'" +
                                                        'style="border:3px solid black;font-family:segoe print;"' +
                                                         "onclick='voir_shirt()'><br><br>";
    click2 += 1
  };
};







function voir_t_longue(){
  
  document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Appuyer sur votre couleur de cheveux, et choississez une catégorie d'habit</i></strong></p>"

  if(LISTE_INFO_COULEUR == ''){
        document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Sélectionnez une couleur de cheveux</i></strong></p>"
        click_t_longue -= 1
  };

  click_t_longue += 1

  liste_t_longue_blanche = ['hb9']
  liste_t_longue_gris = ['hg7', 'hg5', 'hg4']
  
  


  if(click_t_longue % 2 == 1){
    if (LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 1] == 'blanc '){
      for (var i = 0; i < liste_t_longue_blanche.length; i ++){
        document.getElementById(liste_t_longue_blanche[i]).style.display = 'block';
      }
    }
    else if(LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 1] == 'gris '){
      for (var i = 0; i < liste_t_longue_gris.length; i ++){
        document.getElementById(liste_t_longue_gris[i]).style.display = 'block';
      }
    } 
  }
  
  else if(click_t_longue % 2 == 0){
    if (LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 1] == 'blanc '){
      for (var i = 0; i < liste_t_longue_blanche.length; i ++){ 
        document.getElementById(liste_t_longue_blanche[i]).style.display = 'none';
      }
    }
    else if(LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 1] == 'gris '){
      for (var i = 0; i < liste_t_longue_gris.length; i ++){ 
        document.getElementById(liste_t_longue_gris[i]).style.display = 'none';
      } 
    }
  }


  
};




function voir_t_courte(){
  
  document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Appuyer sur votre couleur de cheveux, et choississez une catégorie d'habit</i></strong></p>"

  if(LISTE_INFO_COULEUR == ''){
        document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Sélectionnez une couleur de cheveux</i></strong></p>"
        click_t_courte -= 1
  };

  click_t_courte += 1

  liste_t_courte = ['hb3','hb4', 'hb5', 'hb7', 'hb8','hb2']
  liste_t_courte_gris = ['hg1', 'hg2', 'hg3', 'hg6', 'hg10', 'hg9', 'hg8']

  if(click_t_courte % 2 == 1){
    if (LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 1] == 'blanc '){
      for (var i = 0; i < liste_t_courte.length; i ++){
        document.getElementById(liste_t_courte[i]).style.display = 'block';
      }
    }
    else if(LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 1] == 'gris '){
      for (var i = 0; i < liste_t_courte_gris.length; i ++){
        document.getElementById(liste_t_courte_gris[i]).style.display = 'block';
      }
    } 
  }
  
  else if(click_t_longue % 2 == 0){
    if (LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 1] == 'blanc '){
      for (var i = 0; i < liste_t_courte.length; i ++){ 
        document.getElementById(liste_t_courte[i]).style.display = 'none';
      }
    }
    else if(LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 1] == 'gris '){
      for (var i = 0; i < liste_t_courte_gris.length; i ++){ 
        document.getElementById(liste_t_courte_gris[i]).style.display = 'none';
      } 
    }
  }
};











function voir_t_laine(){

  
  document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Appuyer sur votre couleur de cheveux, et choississez une catégorie d'habit</i></strong></p>"

  if(LISTE_INFO_COULEUR == ''){
        document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Sélectionnez une couleur de cheveux</i></strong></p>"
        click_t_laine -= 1
  };

  click_t_laine += 1

  liste_t_laine = ['hb1','hb10']


  if(click_t_laine % 2 == 1){
    if (LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 1] == 'blanc '){
      for (var i = 0; i < liste_t_laine.length; i ++){
        document.getElementById(liste_t_laine[i]).style.display = 'block';
      }
    }
    else if(LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 2] == 'gris '){
      for (var i = 0; i < liste_t_longue_blanche.length; i ++){
        document.getElementById(liste_t_longue_blanche[i]).style.display = 'block';
      }
    } 
  }
  
  else if(click_t_laine % 2 == 0){
    for (var i = 0; i < liste_t_laine.length; i ++){
      document.getElementById(liste_t_laine[i]).style.display = 'none';
      document.getElementById(liste_t_longue_blanche[i]).style.display = 'none';
    }
  }
};





  function voir_salopette(){

    document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Appuyer sur votre couleur de cheveux, et choississez une catégorie d'habit</i></strong></p>"
    
    if(LISTE_INFO_COULEUR == ''){
      document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Sélectionnez une couleur de cheveux</i></strong></p>"
      click_salopette += -1
    };
    
    if(LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 2] == 'blanc'){
      document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Nous ne disposons pas de salopette blanche</i></strong></p>"
    };

    click_salopette += 1

    if(click_salopette % 2 == 1){
      if (LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 2] == 'bleu'){
        document.getElementById('bbl10').style.display = 'block';
      }
    }
    else if(click_salopette % 2 == 0){
      document.getElementById('bbl10').style.display = 'none';
    
   }
  };



  function voir_jean(){
    
    document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Appuyer sur votre couleur de cheveux, et choississez une catégorie d'habit</i></strong></p>"
    
    if(LISTE_INFO_COULEUR == ''){
      document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Sélectionnez une couleur de cheveux</i></strong></p>"
      click_jean -= 1
    };

    click_jean += 1
    
    liste_jean_bleu = ['bbl1', 'bbl2','bbl6','bbl17', 'bbl8', 'bbl11', 'bbl12', 'bbl4']
    
    liste_jean_blanc = ['bb1', 'bb2', 'bb6','bb5', 'bb8', 'bb9', 'bb10']

    if(click_jean % 2 == 1){
      if (LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 2] == 'bleu'){
        for (var i = 0; i < liste_jean_bleu.length; i ++){
          document.getElementById(liste_jean_bleu[i]).style.display = 'block';
        }
      }
      else if(LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 2] == 'blanc'){
        for (var i = 0; i < liste_jean_blanc.length; i ++){
          document.getElementById(liste_jean_blanc[i]).style.display = 'block';
        }
      } 
    }
    
    else if(click_jean % 2 == 0){
      for (var i = 0; i < liste_jean_bleu.length; i ++){
        document.getElementById(liste_jean_bleu[i]).style.display = 'none';
        document.getElementById(liste_jean_blanc[i]).style.display = 'none';
      }
    }
  };




  function voir_toile(){

    document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Appuyer sur votre couleur de cheveux, et choississez une catégorie d'habit</i></strong></p>"

    if(LISTE_INFO_COULEUR == ''){
      document.getElementById('info_oups').innerHTML = "<p id='info_oups'><strong><i>Sélectionnez une couleur de cheveux</i></strong></p>"
      click_toile -= 1
    };

    click_toile += 1
    
    liste_toile_bleu = ['bbl3','bbl5','bbl9']

    liste_toile_blanc = ['bb3', 'bb4', 'bb7']
    
    
    if(click_toile % 2 == 1){
      if (LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 2] == 'bleu'){
        for (var i = 0; i < liste_toile_bleu.length; i ++){
          document.getElementById(liste_toile_bleu[i]).style.display = 'block';
        }
      }
      else if(LISTE_INFO_COULEUR[LISTE_INFO_COULEUR.length - 2] == 'blanc'){
        for (var i = 0; i < liste_toile_blanc.length; i ++){
          document.getElementById(liste_toile_blanc[i]).style.display = 'block';
        }
      } 
    }
    
    else if(click_toile % 2 == 0){
      for (var i = 0; i < liste_toile_bleu.length; i ++){
        document.getElementById(liste_toile_bleu[i]).style.display = 'none';
        document.getElementById(liste_toile_blanc[i]).style.display = 'none';
      }
    }
  };



