
//HOME JS

//Here we stop the slider and display
//text of pictures.

// ---> VISUAL FUNCTION <--- si image un alors j'affiche ca sinon non

function stop(im){
  document.getElementById('marc').stop(); //stop the slider when the mouse is on the picture


  //for PICTURE NUMBER ONE we put the status, and give description of the project.
  if(im == 'im1'){
    document.getElementById('status').innerHTML = '<center>Status : Fini</center>';
    document.getElementById('description').innerHTML = '<center>' +
                                                        'Saisissez le nom d\'une ville ! ' +
                                                        'Nous r\u00e9cup\u00e9rons ses coordonn\u00e9es, le sens du vent, ' +
                                                        'calculons sa nouvelle trajectoire et ' +
                                                        'nous l\'affichons sur une carte google map.'
                                                        '</center>';
    document.getElementById('description').style.textAlign = 'justify';
  }

  //PICTURE NUMBER TWO
  else if(im == 'im2'){
    
    document.getElementById('status').innerHTML = '<center>Status : Fini</center>';
    document.getElementById('description').innerHTML = '<center>' +
                                                        'Saisissez une phrase ! ' +
                                                        'Nous la r\u00e9cup\u00e9rons et la traitons, ' +
                                                        'au choix une table de multiplication, ' +
                                                        'un affichage et une recherche de d\u00e9finition. ' +
                                                        "Banal, oui sauf que nous n'avons pas coder de fonction</center>";

    document.getElementById('description').style.textAlign = 'justify';
    
  }

  //PICTURE NUMBER THREE
  else if(im == 'im3'){
    
    document.getElementById('status').innerHTML = '<center>Status : En cours</center>';
    document.getElementById('description').innerHTML = '<center>' +
                                                        "Un jeux d'arcarde ! " +
                                                        'bas\u00e9 sur speech recognition de google, ' +
                                                        "J'ai besoin d'un bouclier et vite. " +
                                                        "SHIELDDD !!</center>";
    
    document.getElementById('description').style.textAlign = 'justify';
    
  }

  //PICTURE NUMBER FOUR
  else if(im == 'im4'){
    
    document.getElementById('status').innerHTML = '<center>Status : En cours</center>';
    document.getElementById('description').innerHTML = '<center>' +
                                                        'Saisissez une phrase ! ' +
                                                        'Nous la r\u00e9cup\u00e9rons et la traitons. ' +
                                                        'Nous vous donnons ensuite la fonction de chaque mot, ' +
                                                        'pronom, verbe, nominal...' +
                                                        "</center>";
    
    document.getElementById('description').style.textAlign = 'justify';
  }

  //PICTURE NUMBER FIVE
  else if(im == 'im5'){
    
    document.getElementById('status').innerHTML = '<center>Status : En cours</center>';
    
    document.getElementById('description').innerHTML = '<center>' +
                                                        'Un script qui permet ' +
                                                        'de dire les mots r\u00e9currents ' +
                                                        "d'un texte" +
                                                        "</center>";
    
    document.getElementById('description').style.textAlign = 'justify';
  }

  //PICTURE NUMBER SIX
  else if(im == 'im6'){
    
    document.getElementById('status').innerHTML = '<center>Status : Fini</center>';
    document.getElementById('description').innerHTML = '<center>' +
                                                        'Un script qui permet de dessiner ! ' +
                                                        'sommairement une voiture ' +
                                                        'par sa description ' +
                                                        '(4 roues, une caisse ect...' +
                                                        "</center>";
    
    document.getElementById('description').style.textAlign = 'justify';
  }

  //PICTURE NUMBER SEVEN
  else if(im == 'im7'){
    document.getElementById('status').innerHTML = '<center>Status : En cours de finition</center>';
    
    document.getElementById('description').innerHTML = "<center>Un magazine virtuel " +
                                                      "avec une rubrique mode et une rubrique de pollution. " +
                                                      "Avez vous d\u00e9j\u00e0 lu un magazine chez votre marchand de journaux ? Et... en ligne ?" +
                                                      "</center>";
    
    document.getElementById('description').style.textAlign = 'justify';
  }

  //PICTURE NUMBER TEN
  else if(im == 'im10'){
    document.getElementById('status').innerHTML = '<center>Status : Fini</center>';
    
    document.getElementById('description').innerHTML = "<center>Dk labyrinth " +
                                                      "Dk apprend tout seul \u00e0 se d\u00e9placer " +
                                                      "via un algorithme g\u00e9n\u00e9tique par Brute force " +
                                                      "qui n'est pas la meilleur solution</center>";
    
    document.getElementById('description').style.textAlign = 'justify';
  }

  //PICTURE NUMBER ELEVEN
  else if(im == 'im11'){
    document.getElementById('status').innerHTML = '<center>Status : Fini</center>';
    
    document.getElementById('description').innerHTML = "<center>Openfoodfact " +
                                                      "Un jeu o\u00f9 il faut choisir la meilleure bouffe. " +
                                                      "Ce projet contient un d\u00e9tecteur d'objet ! (permettant de d\u00e9tecter des m\u00eames objets par matching)" +
                                                      "</center>";
    
    document.getElementById('description').style.textAlign = 'justify';
  }




  
};


//When mouse is out the picture we reinitialise the description and status div to nothing
// ---> VISUAL FUNCTION <--- des que souris quitte alors jefface tout
function start(){
  document.getElementById('marc').start();
    document.getElementById('description').innerHTML = "";
  document.getElementById('status').innerHTML = "";
};


