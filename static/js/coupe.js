function favovo(){
};


function coupe_longue(){
  document.getElementById('placement').style.display = 'none';
  document.getElementById('bout_fermer_longue').style.display = 'block';

  document.getElementById('draggable19').style.display = 'block';
  document.getElementById('draggable18').style.display = 'block';
  document.getElementById('draggable').style.display = 'block';
  document.getElementById('draggable4').style.display = 'block';
  document.getElementById('draggable15').style.display = 'block';
  document.getElementById('draggable5').style.display = 'block';

};


function coupe_courte(){
  document.getElementById('placement').style.display = 'none';
  document.getElementById('bout_fermer_court').style.display = 'block';

  document.getElementById('draggable14').style.display = 'block';
  document.getElementById('draggable16').style.display = 'block';
};


function coupe_longue_coul(){
  document.getElementById('placement').style.display = 'none';
  document.getElementById('bout_fermer_longue_coul').style.display = 'block';

  document.getElementById('draggable10').style.display = 'block';
  document.getElementById('draggable11').style.display = 'block';
  document.getElementById('draggable6').style.display = 'block'; 
};



function coupe_courte_coul(){
  document.getElementById('placement').style.display = 'none';
  document.getElementById('bout_fermer_court_coul').style.display = 'block';

  document.getElementById('draggable3').style.display = 'block';
  document.getElementById('draggable9').style.display = 'block';
  document.getElementById('draggable12').style.display = 'block'; 
};




function barbe(){
  document.getElementById('placement').style.display = 'none';
  document.getElementById('bout_fermer_barbe').style.display = 'block';

  document.getElementById('draggable7').style.display = 'block';
  document.getElementById('draggable8').style.display = 'block';
};


function fermer1(){
  document.getElementById('placement').style.display = 'block';
  document.getElementById('bout_fermer_longue').style.display = 'none';

  document.getElementById('draggable19').style.display = 'none';
  document.getElementById('draggable18').style.display = 'none';
  document.getElementById('draggable').style.display = 'none';
  document.getElementById('draggable4').style.display = 'none';
  document.getElementById('draggable15').style.display = 'none';
  document.getElementById('draggable5').style.display = 'none';
};

function fermer2(){
  document.getElementById('placement').style.display = 'block';
  document.getElementById('bout_fermer_court').style.display = 'none';

  document.getElementById('draggable14').style.display = 'none';
  document.getElementById('draggable16').style.display = 'none';
};

function fermer3(){
  document.getElementById('placement').style.display = 'block';
  document.getElementById('bout_fermer_longue_coul').style.display = 'none';

  document.getElementById('draggable10').style.display = 'none';
  document.getElementById('draggable11').style.display = 'none';
  document.getElementById('draggable6').style.display = 'none'; 
};

function fermer4(){
  document.getElementById('placement').style.display = 'block';
  document.getElementById('bout_fermer_court_coul').style.display = 'none';

  document.getElementById('draggable3').style.display = 'none';
  document.getElementById('draggable9').style.display = 'none';
  document.getElementById('draggable12').style.display = 'none'; 
};
function fermer5(){
  document.getElementById('placement').style.display = 'block';
  document.getElementById('bout_fermer_barbe').style.display = 'none';

  document.getElementById('draggable7').style.display = 'none';
  document.getElementById('draggable8').style.display = 'none';
};        




  

jQuery("#sauve").on("click", function(e){

 e.preventDefault();
  jQuery.ajax({
      data:{
          'product':String(LISTE1[LISTE1.length -1]),
      },
      type:"POST",
      url:"/photo/coupe"
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

  



LISTE1 = []

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





var LISTECOUPE = []

var liste_liste = [draggable,draggable3,draggable4,draggable5,draggable6,draggable7,draggable8,draggable9,
                    draggable10,draggable11,draggable12,draggable14,draggable15,draggable16,draggable18,
                    draggable19]


function yo() {

  for(var i = 0; i <= liste_liste.length - 1; i++){
 
    var a = document.getElementById(liste_liste[i].id).offsetLeft;
    var b = document.getElementById(liste_liste[i].id).offsetTop;

    if(a >= 10 && a <= 349 & b >=130 && b <= 410 ){
      
      LISTECOUPE.push(liste_liste[i].id)
      document.getElementById("coupedecheveux").value = LISTECOUPE[LISTECOUPE.length - 1];
  
      
      document.getElementById("jaime").submit();
    }
  
   };
  
   for (var i = 0; i <= LISTE_FAV_FAV.length - 1; i++){

     var a = document.getElementById(LISTE_FAV_FAV[LISTE_FAV_FAV.length-1]);

     var b = a.offsetLeft;
     var c = a.offsetTop;
 
     if(b >= 460 && b <= 580 & c >=60 && c <= 220 ){

        document.getElementById("coupedecheveux").value = LISTE_FAV_FAV[LISTE_FAV_FAV.length - 1];
    
        document.getElementById("jaime").submit();

        
     };
   };

};


const constraints = {video: true};

(function() {
  const video = document.querySelector('#basic video');
  const captureVideoButton = document.querySelector('#basic .capture-button');
  let localMediaStream;

  function handleSuccess(stream) {
    localMediaStream = stream;
    video.srcObject = stream;
  }

  captureVideoButton.onclick = function() {
    navigator.mediaDevices.getUserMedia(constraints).
      then(handleSuccess).catch(handleError);
  };

  document.querySelector('#stop-button').onclick = function() {
    video.pause();
    localMediaStream.stop();
  };
})();

(function() {
  const captureVideoButton =
    document.querySelector('#screenshot .capture-button');
  const screenshotButton = document.querySelector('#screenshot-button');
  const img = document.querySelector('#screenshot img');
  const video = document.querySelector('#screenshot video');

  const canvas = document.createElement('canvas');

  captureVideoButton.onclick = function() {
    navigator.mediaDevices.getUserMedia(constraints).
      then(handleSuccess).catch(handleError);
  };


  screenshotButton.onclick = video.onclick = function() {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    // Other browsers will fall back to image/png
    img.src = canvas.toDataURL('image/webp');
  };


  function handleSuccess(stream) {
    screenshotButton.disabled = false;
    video.srcObject = stream;
  }
})();


(function() {
  const captureVideoButton =
    document.querySelector('#cssfilters .capture-button');
  const cssFiltersButton = document.querySelector('#basic');
  const video = document.querySelector('#basic video');

  let filterIndex = 0;
  const filters = [
    'grayscale',
    ''
  ];


  captureVideoButton.onclick = function() {
    navigator.mediaDevices.getUserMedia(constraints).
      then(handleSuccess).catch(handleError);
  };


  cssFiltersButton.onclick = video.onclick = function() {
    video.className = filters[filterIndex++ % filters.length];
  };


  function handleSuccess(stream) {
    video.srcObject = stream;
  }
})();



  function coiffeur(){
    document.getElementById('CONTENEUR').style.display = "none";
    document.getElementById('coifcoif').style.display = "block";
  };

  function gym(){
    document.getElementById('CONTENEUR').style.display = "none";
    document.getElementById('gymgym').style.display = "block";

 };



function return_choice_coif(){
    document.getElementById('the_map').style.display = 'none';
    document.getElementById('mapmap').style.display = 'block';

    }

function return_choice_gym(){
    document.getElementById('the_map').style.display = 'none';
    document.getElementById('mapmap_gym').style.display = 'block';

    }


function menu_map(){
    document.getElementById('mapmap').style.display = 'none';
    document.getElementById('mapmap_gym').style.display = 'none';
    document.getElementById('CONTENEUR').style.display = 'block';
    document.getElementById('the_map').style.display = 'none';
    document.getElementById('the_map_gym').style.display = 'none';


};

function menuuu(){
    document.getElementById('coifcoif').style.display = 'none';
    document.getElementById('CONTENEUR').style.display = 'block';
    document.getElementById('gymgym').style.display = 'none';
};



LISTE_COIFURE = []


jQuery("#coif2").on("click", function(e){
    
    document.getElementById('gifou').style.display = 'block';
    var a = document.getElementById('coif1').value;

LISTE = []

 e.preventDefault();
  jQuery.ajax({
      data:{
          'hairdresser':a,
      },
      type:"POST",
      url:"/photo/coupe"
  })
  .done(function(data){
      if (data.error){
          jQuery("#monCadreAlert").text(data.error);
          jQuery("#is_save");
          
          
      }
      else{
          jQuery("#is_save").html(data.data);
          jQuery("#monCadreAlert");
          document.getElementById('gifou').style.display = 'none';
          document.getElementById('coifcoif').style.display = 'none';
          document.getElementById('mapmap').style.display = 'block';
          document.getElementById('info').style.display = 'block';
          document.getElementById('p_am_pm').style.display = 'block';

          
          
          
          var c = 0
          var c1 = 0
          var nom = ''
          for(var i = 0; i < data.length; i ++){

            
            if(data[i] == "'" && data[c1+1] == ']' && data[c1+2] == '['){
              LISTE.push([nom])
              c+=1
              nom = ''
            }
            else if (data[i] == "'" || data[i] == "["){
              {}
            }
            else if(data[i] == ']'){
              {}
            }
            else if(data[i] == ',' && data[c1+1] == ' ' && data[c1+2] == '['){
              LISTE.push([nom])
              c+=1
              nom = ''
            }
            else if(data[i] == ','){
              {}
            }
            else if(data[i] == '"'){
              {}

            }
            else{
              nom += data[i]
            };
            c1 += 1

          };

          console.log(LISTE)
          console.log('000000000000000')

        
                    
        var a = 0
        if(LISTE[0] == undefined){a += 1};
        if(LISTE[1] == undefined){a += 1};
        if(LISTE[2] == undefined){a += 1};
        if(LISTE[3] == undefined){a += 1};
        if(LISTE[4] == undefined){a += 1};
        if(LISTE[5] == undefined){a += 1};
        if(LISTE[6] == undefined){a += 1};
        if(LISTE[7] == undefined){a += 1};
        if(a>4){
              document.getElementById('info1').style.display = 'none';
              a = 0
        }
        else{
                
            var info_coiffeur1 =  "<br><br><strong>" + LISTE[0] + " :</strong><br><br>" +
                                  LISTE[1] + "<br>" +
                                  LISTE[2] + "<br>" +
                                  LISTE[3] + "<br>" +
                                  LISTE[4] + "<br>" +
                                  LISTE[5] + "<br>" +
                                  LISTE[6] + "<br>" +
                                  LISTE[7] + "<br><br>" +
                                  "<input type='button' value='Voir la map' onclick='declencheur1_f()'>";
                                  
    

                  
             document.getElementById('info1').innerHTML = info_coiffeur1;                   
            };           



        var b = 0
        if(LISTE[8] == undefined){b += 1};
        if(LISTE[9] == undefined){b += 1};
        if(LISTE[10] == undefined){b += 1};
        if(LISTE[11] == undefined){b += 1};
        if(LISTE[12] == undefined){b += 1};
        if(LISTE[13] == undefined){b += 1};
        if(LISTE[14] == undefined){b += 1};
        if(LISTE[15] == undefined){b += 1};
        if(b>4){
              document.getElementById('info2').style.display = 'none';
              b = 0
        }
        else{
            
            var info_coiffeur2 =  "<br><br><strong>" + LISTE[8] + "</strong><br><br>" +
                                  LISTE[9]  + "<br>" +
                                  LISTE[10]  + "<br>" +
                                  LISTE[11] + "<br>" +
                                  LISTE[12] + "<br>" +
                                  LISTE[13] + "<br>" +
                                  LISTE[14] + "<br>" +
                                  LISTE[15] + "<br><br>" +
                                 "<input type='button' value='Voir la map' onclick='declencheur2_f()'>";
                                  
            document.getElementById('info2').innerHTML = info_coiffeur2;
      

        }


        var c = 0
        if(LISTE[16] == undefined){c += 1};
        if(LISTE[17] == undefined){c += 1};
        if(LISTE[18] == undefined){c += 1};
        if(LISTE[19] == undefined){c += 1};
        if(LISTE[20] == undefined){c += 1};
        if(LISTE[21] == undefined){c += 1};
        if(LISTE[22] == undefined){c += 1};
        if(LISTE[23] == undefined){c += 1};
        if(c>4){
              document.getElementById('info3').style.display = 'none';
              c = 0
        }
        else{
            
            var info_coiffeur3 =  "<br><br><strong>" + LISTE[16] + "</strong><br><br>" +
                                  LISTE[17] + "<br>" +
                                  LISTE[18] + "<br>" +
                                  LISTE[19] + "<br>" +
                                  LISTE[20] + "<br>" +
                                  LISTE[21] + "<br>" +
                                  LISTE[22] + "<br>" +   
                                  LISTE[23] + "<br><br>" +
                                  "<input type='button' value='Voir la map' onclick='declencheur3_f()'>";
                                 

            document.getElementById('info3').innerHTML = info_coiffeur3;
        
         }


        var d = 0
        if(LISTE[24] == undefined){d += 1};
        if(LISTE[25] == undefined){d += 1};
        if(LISTE[26] == undefined){d += 1};
        if(LISTE[27] == undefined){d += 1};
        if(LISTE[28] == undefined){d += 1};
        if(LISTE[29] == undefined){d += 1};
        if(LISTE[30] == undefined){d += 1};
        if(LISTE[31] == undefined){d += 1};
        if(d>4){
            document.getElementById('info4').style.display = 'none';
            d = 0
        }
        else{              

            var info_coiffeur4 =  "<br><br><strong>" + LISTE[24] + "</strong><br><br>" + 
                                  LISTE[25] + "<br>" +
                                  LISTE[26] + "<br>" +
                                  LISTE[27] + "<br>" +
                                  LISTE[28] + "<br>" +
                                  LISTE[39] + "<br>" +
                                  LISTE[30] + "<br>" +
                                  LISTE[31] + "<br><br>" +
                                  "<input type='button' value='Voir la map' onclick='declencheur4_f()'>";
                                  
            
            document.getElementById('info4').innerHTML = info_coiffeur4;
                                  
        }

                                      
        LISTE_COIFURE.push([LISTE[0], LISTE[8], LISTE[16], LISTE[24]]);
 
        var a = document.getElementById('info1');
        var b = document.getElementById('info2');
        var c = document.getElementById('info3');
        var d = document.getElementById('info4');

        if(a.style.display == 'none' && b.style.display == 'none' && c.style.display == 'none' && d.style.display == 'none'){

            document.getElementById('aucas_ou_coif').innerHTML = "<center><h3><br><br>Veuillez nous excusez nous n'avons rien trouv\u00e9</h3></center>";
            document.getElementById('cons').style.display = 'none';
            document.getElementById('coifcoifcoif').style.display = 'none';
        
        }
        
        

      };
  });
});




jQuery("#gym2").on("click", function(e){
    
    document.getElementById('gifou_gym').style.display = 'block';
    var a = document.getElementById('gym1').value;

    LISTE_GYM = []
    LISTE_GYMGYM = []

 e.preventDefault();
  jQuery.ajax({
      data:{
          'gymnastic':a,
      },
      type:"POST",
      url:"/photo/coupe"
  })
  .done(function(data){
      if (data.error){
          jQuery("#monCadreAlert").text(data.error);
          jQuery("#is_save");
          
          
      }
      else{
          jQuery("#is_save").html(data.data);
          jQuery("#monCadreAlert");
          document.getElementById('gifou_gym').style.display = 'none';
          document.getElementById('gymgym').style.display = 'none';
          document.getElementById('mapmap_gym').style.display = 'block';
          console.log(data)

          var c = 0
          var c1 = 0
          var nom = ''
          
          for (var i = 0; i < data.length; i++){
            
            if(data[i] == "'" && data[c1+1] == ']' && data[c1+2] == '['){
              LISTE_GYM.push([nom])
              c+=1
              nom = ''
            }
            else if (data[i] == "'" || data[i] == "["){
              {}
            }
            else if(data[i] == ']'){
              {}
            }
            else if(data[i] == ',' && data[c1+1] == ' ' && data[c1+2] == '['){
              LISTE_GYM.push([nom])
              c+=1
              nom = ''
            }
            else if(data[i] == ','){
              {}
            }
            else if(data[i] == '"'){
              {}

            }
            else{
              nom += data[i]
            };
            c1 += 1

          };

          console.log(LISTE_GYM)
          console.log('000000000000000')

       var e = 0
       if(LISTE_GYM[0] == undefined){e += 1}
       if(LISTE_GYM[1] == undefined){e += 1}
       if(LISTE_GYM[2] == undefined){e += 1}
       if(LISTE_GYM[3] == undefined){e += 1}
       if(LISTE_GYM[4] == undefined){e += 1}
       if(LISTE_GYM[5] == undefined){e += 1}
       if(LISTE_GYM[6] == undefined){e += 1}
       if(LISTE_GYM[7] == undefined){e += 1}
       if(e > 4){
            document.getElementById('info1_gym').style.display = 'none';
            e = 0
        }

      else{
        var info_gym1 =  "<br><br><strong>" + LISTE_GYM[0] + " :</strong><br><br>" +
                              LISTE_GYM[1] + "<br>" +
                              LISTE_GYM[2] + "<br>" +
                              LISTE_GYM[3] + "<br>" +
                              LISTE_GYM[4] + "<br>" +
                              LISTE_GYM[5] + "<br>" +
                              LISTE_GYM[6] + "<br>" +
                              LISTE_GYM[7] + "<br><br>" +
                              "<input type='button' value='Voir la map' onclick='declencheur_gym1f()'>";
        
         document.getElementById('info1_gym').innerHTML = info_gym1;                     
    }     
                              





       var f = 0
       if(LISTE_GYM[8] == undefined){f += 1}
       if(LISTE_GYM[9] == undefined){f += 1}
       if(LISTE_GYM[10] == undefined){f += 1}
       if(LISTE_GYM[11] == undefined){f += 1}
       if(LISTE_GYM[12] == undefined){f += 1}
       if(LISTE_GYM[13] == undefined){f += 1}
       if(LISTE_GYM[14] == undefined){f += 1}
       if(LISTE_GYM[15] == undefined){f += 1}
       if(f > 4){
            document.getElementById('info2_gym').style.display = 'none';
            f = 0
        }
        else{


        var info_gym2 =  "<br><br><strong>" + LISTE_GYM[8] + "</strong><br><br>" +
                              LISTE_GYM[9]  + "<br>" +
                              LISTE_GYM[10]  + "<br>" +
                              LISTE_GYM[11] + "<br>" +
                              LISTE_GYM[12] + "<br>" +
                              LISTE_GYM[13] + "<br>" +
                              LISTE_GYM[14] + "<br>" +
                              LISTE_GYM[15] + "<br><br>" +
                              "<input type='button' value='Voir la map' onclick='declencheur_gym2f()'>";

            document.getElementById('info2_gym').innerHTML = info_gym2;
        }




       var g = 0
       if(LISTE_GYM[16] == undefined){g += 1}
       if(LISTE_GYM[17] == undefined){g += 1}
       if(LISTE_GYM[18] == undefined){g += 1}
       if(LISTE_GYM[19] == undefined){g += 1}
       if(LISTE_GYM[20] == undefined){g += 1}
       if(LISTE_GYM[21] == undefined){g += 1}
       if(LISTE_GYM[22] == undefined){g += 1}
       if(LISTE_GYM[23] == undefined){g += 1}
       if(g > 4){
            document.getElementById('info3_gym').style.display = 'none';
            g = 0
        }
        else{
            var info_gym3 =  "<br><br><strong>" + LISTE_GYM[16] + "</strong><br><br>" +
                                  LISTE_GYM[17] + "<br>" +
                                  LISTE_GYM[18] + "<br>" +
                                  LISTE_GYM[19] + "<br>" +
                                  LISTE_GYM[20] + "<br>" +
                                  LISTE_GYM[21] + "<br>" +
                                  LISTE_GYM[22] + "<br>" +
                                  LISTE_GYM[23] + "<br><br>" +
                                  "<input type='button' value='Voir la map' onclick='declencheur_gym3f()'>";

            document.getElementById('info3_gym').innerHTML = info_gym3;
        }


                         
       var h = 0
       if(LISTE_GYM[24] == undefined){h += 1}
       if(LISTE_GYM[25] == undefined){h += 1}
       if(LISTE_GYM[26] == undefined){h += 1}
       if(LISTE_GYM[27] == undefined){h += 1}
       if(LISTE_GYM[28] == undefined){h += 1}
       if(LISTE_GYM[29] == undefined){h += 1}
       if(LISTE_GYM[30] == undefined){h += 1}
       if(LISTE_GYM[31] == undefined){h += 1}
       if(h > 4){
            document.getElementById('info4_gym').style.display = 'none';
            h = 0
        }
        else{
            
            var info_gym4 =  "<br><br><strong>" + LISTE_GYM[24] + "</strong><br><br>" + 
                                  LISTE_GYM[25] + "<br>" +
                                  LISTE_GYM[26] + "<br>" +
                                  LISTE_GYM[27] + "<br>" +
                                  LISTE_GYM[28] + "<br>" +
                                  LISTE_GYM[29] + "<br>" +
                                  LISTE_GYM[30] + "<br>" +
                                  LISTE_GYM[31] + "<br><br>" +
                                  "<input type='button' value='Voir la map' onclick='declencheur_gym4f()'>";
                                  
            document.getElementById('info4_gym').innerHTML = info_gym4;
        }



        var a = document.getElementById('info1_gym')
        var b = document.getElementById('info2_gym')
        var c = document.getElementById('info3_gym')
        var d = document.getElementById('info4_gym')

        
        if(a.style.display == 'none' && b.style.display == 'none' && c.style.display == 'none' && d.style.display == 'none'){
            
            document.getElementById('aucas_ou').innerHTML = "<center><h3>Veuillez nous excusez nous n'avons rien trouv\u00e9</h3></center>";
            document.getElementById('p_am_pm').style.display = 'none';
            document.getElementById('info').style.display = 'none';
        }

        LISTE_GYMGYM.push([LISTE_GYM[0], LISTE_GYM[8], LISTE_GYM[16], LISTE_GYM[24]]);
 
                        
        
        
        
        
        

      };
      
  });
});





  jQuery("#declencheur1").on("click", function(e){
      
     var b = document.getElementById('coif1').value;
     document.getElementById('mapmap').style.display = 'none';
     document.getElementById('oups').innerHTML = '';
     
     e.preventDefault();
      jQuery.ajax({
          data:{
              'buttony':String(LISTE[0]),
              'country':b,

          },
          type:"POST",
          url:"/photo/coupe"
      })
      .done(function(data){
          if (data.error){
              jQuery("#monCadreAlert").text(data.error);
              jQuery("#is_save");
              
              
          }
          else{
              jQuery("#is_save").html(data.data);
              jQuery("#monCadreAlert");
             

              liste_lat = []
              console.log(data)


              if (data == "Oups nous n'avons rien trouvé"){
             
      
                document.getElementById('the_map').style.display = 'block';
                document.getElementById('oups').innerHTML = "Nous n'avons rien trouvé désolé";
                
                document.getElementById('map').style.display = 'none';  
                document.getElementById('lapmap').style.display = 'none';
                
                document.getElementById('button_lamap_gym').style.display = 'none';
                document.getElementById('button_lamap').style.display = 'block';
                }
              else{
          
                  pos = ''
                  for (var i = 0; i < data.length; i++){
                      console.log(data[i])
                      if (data[i] == ' '){
                        liste_lat.push(pos)
                        pos = ''
                      }
                      else{
                         pos += data[i]
                     } 
                  }
                  liste_lat.push(pos)
                  console.log(liste_lat)
                  console.log("fini")
                  
                  document.getElementById('the_map').style.display = 'block';
                  document.getElementById('button_lamap_gym').style.display = 'none';
       
                  document.getElementById('button_lamap').style.display = 'block';
                  initMap(parseFloat(liste_lat[0]), parseFloat(liste_lat[1]));
                  
            };
          };
          
      });
  });

  


  jQuery("#declencheur2").on("click", function(e){
      
     var b = document.getElementById('coif1').value;
     document.getElementById('mapmap').style.display = 'none';
     document.getElementById('oups').innerHTML = '';

     e.preventDefault();
      jQuery.ajax({
          data:{
              'buttony':String(LISTE[8]),
              'country':b,
          },
          type:"POST",
          url:"/photo/coupe"
      })
      .done(function(data){
          if (data.error){
              jQuery("#monCadreAlert").text(data.error);
              jQuery("#is_save");
              
              
          }
          else{
              jQuery("#is_save").html(data.data);
              jQuery("#monCadreAlert");
              
              liste_lat = []
              console.log(data)

              if (data == "Oups nous n'avons rien trouvé"){
     
                document.getElementById('the_map').style.display = 'block';
                document.getElementById('oups').innerHTML = "Nous n'avons rien trouvé désolé";
                
                document.getElementById('map').style.display = 'none';  
                document.getElementById('lapmap').style.display = 'none';
                
                document.getElementById('button_lamap_gym').style.display = 'none';
                document.getElementById('button_lamap').style.display = 'block';
                }
              else{
                


              pos = ''
              for (var i = 0; i < data.length; i++){
                  console.log(data[i])
                  if (data[i] == ' '){
                    liste_lat.push(pos)
                    pos = ''
                  }
                  else{
                     pos += data[i]
                 } 
              }
              liste_lat.push(pos)
              console.log(liste_lat)
              document.getElementById('the_map').style.display = 'block';
              document.getElementById('button_lamap_gym').style.display = 'none';
              document.getElementById('button_lamap').style.display = 'block';
              
              initMap(parseFloat(liste_lat[0]), parseFloat(liste_lat[1]));
              
           };   
          };
          
      });
  });



  jQuery("#declencheur3").on("click", function(e){
   
    var b = document.getElementById('coif1').value;
    document.getElementById('mapmap').style.display = 'none';
    document.getElementById('oups').innerHTML = '';
    
     e.preventDefault();
      jQuery.ajax({
          data:{
              'buttony':String(LISTE[16]),
              'country':b,
              
       
          },
          type:"POST",
          url:"/photo/coupe"
      })
      .done(function(data){
          if (data.error){
              jQuery("#monCadreAlert").text(data.error);
              jQuery("#is_save");
              
              
          }
          else{
              jQuery("#is_save").html(data.data);
              jQuery("#monCadreAlert");
              
              liste_lat = []
              console.log(data)

              if (data == "Oups nous n'avons rien trouvé"){
           
                document.getElementById('the_map').style.display = 'block';
                document.getElementById('oups').innerHTML = "Nous n'avons rien trouv\u00e9 d\u00e9sol\u00e9";
                
                document.getElementById('map').style.display = 'none';  
    
                document.getElementById('lapmap').style.display = 'none';
                document.getElementById('button_lamap_gym').style.display = 'none';
                
                document.getElementById('button_lamap').style.display = 'block';
                
                }
              else{

              pos = ''
              for (var i = 0; i < data.length; i++){
                  console.log(data[i])
                  if (data[i] == ' '){
                    liste_lat.push(pos)
                    pos = ''
                  }
                  else{
                     pos += data[i]
                 } 
              }
              liste_lat.push(pos)
              console.log(liste_lat)
              
              document.getElementById('the_map').style.display = 'block';
              document.getElementById('button_lamap_gym').style.display = 'none';
              
              document.getElementById('button_lamap').style.display = 'block';
              initMap(parseFloat(liste_lat[0]), parseFloat(liste_lat[1]));
              
              
            };  
          };
          
      });
  });




  jQuery("#declencheur4").on("click", function(e){

     var b = document.getElementById('coif1').value;
     document.getElementById('mapmap').style.display = 'none';
     document.getElementById('oups').innerHTML = '';
     
     e.preventDefault();
      jQuery.ajax({
          data:{
               'buttony':String(LISTE[24]),
               'country':b, 
              
       
          },
          type:"POST",
          url:"/photo/coupe"
      })
      .done(function(data){
          if (data.error){
              jQuery("#monCadreAlert").text(data.error);
              jQuery("#is_save");
              
              
          }
          else{
              jQuery("#is_save").html(data.data);
              jQuery("#monCadreAlert");
              
              liste_lat = []
              console.log(data)

              if (data == "Oups nous n'avons rien trouvé"){
              
                document.getElementById('the_map').style.display = 'block';
                document.getElementById('oups').innerHTML = "Nous n'avons rien trouv\u00e9 d\u00e9sol\u00e9";
                
                document.getElementById('map').style.display = 'none';  
        
                document.getElementById('lapmap').style.display = 'none';
                document.getElementById('button_lamap_gym').style.display = 'none';
                
                document.getElementById('button_lamap').style.display = 'block';
                }
              else{


              pos = ''
              for (var i = 0; i < data.length; i++){
                  console.log(data[i])
                  if (data[i] == ' '){
                    liste_lat.push(pos)
                    pos = ''
                  }
                  else{
                     pos += data[i]
                 } 
              }
              liste_lat.push(pos)
              console.log(liste_lat)
              document.getElementById('the_map').style.display = 'block';
              document.getElementById('button_lamap_gym').style.display = 'none';
              document.getElementById('button_lamap').style.display = 'block';
              initMap(parseFloat(liste_lat[0]), parseFloat(liste_lat[1]));
              
            };  
          };
          
      });
  });













  jQuery("#declencheur_gym1").on("click", function(e){
 
     var b = document.getElementById('gym1').value;
     document.getElementById('oups').innerHTML = '';
     document.getElementById('button_lamap').style.display = 'none';
     
     e.preventDefault();
      jQuery.ajax({
          data:{
               'buttony_gym':String(LISTE_GYM[0]),
               'country_gym':b, 
              
       
          },
          type:"POST",
          url:"/photo/coupe"
      })
      .done(function(data){
          if (data.error){
              jQuery("#monCadreAlert").text(data.error);
              jQuery("#is_save");
              
              
          }
          else{
              jQuery("#is_save").html(data.data);
              jQuery("#monCadreAlert");
              
              liste_lat = []
              console.log(data)
              
              if (data == "Oups nous n'avons rien trouvé"){

                document.getElementById('button_lamap_gym').style.display = 'block';
              
                document.getElementById('the_map').style.display = 'block';
                document.getElementById('oups').innerHTML = "Nous n'avons rien trouv\u00e9 désol\u00e9";
                
                document.getElementById('map').style.display = 'none';  
                document.getElementById('lapmap').style.display = 'none';


              }
              else{

              pos = ''
              for (var i = 0; i < data.length; i++){
            
                  if (data[i] == ' '){
                    liste_lat.push(pos)
                    pos = ''
                  }
                  else{
                     pos += data[i]
                 } 
              }
              liste_lat.push(pos)
              console.log(liste_lat)
              
              document.getElementById('the_map').style.display = 'block';
              document.getElementById('button_lamap').style.display = 'none';
              
              initMap(parseFloat(liste_lat[0]), parseFloat(liste_lat[1]));
             document.getElementById('button_lamap_gym').style.display = 'block';
             document.getElementById('button_lamap').style.display = 'none';
              
            };
          };
          
      });
  });




  jQuery("#declencheur_gym2").on("click", function(e){

     var b = document.getElementById('gym1').value;
     document.getElementById('oups').innerHTML = '';
     document.getElementById('button_lamap').style.display = 'none';
     
     e.preventDefault();
      jQuery.ajax({
          data:{
               'buttony_gym':String(LISTE_GYM[8]),
               'country_gym':b, 
              
       
          },
          type:"POST",
          url:"/photo/coupe"
      })
      .done(function(data){
          if (data.error){
              jQuery("#monCadreAlert").text(data.error);
              jQuery("#is_save");
              
              
          }
          else{
              jQuery("#is_save").html(data.data);
              jQuery("#monCadreAlert");
              console.log(data)
               if (data == "Oups nous n'avons rien trouvé"){


                document.getElementById('button_lamap_gym').style.display = 'block';
             
                document.getElementById('the_map').style.display = 'block';
                document.getElementById('oups').innerHTML = "Nous n'avons rien trouv\u00e9 désol\u00e9";
                
                document.getElementById('map').style.display = 'none';  
                document.getElementById('lapmap').style.display = 'none';

                
   
                }
              else{

              pos = ''
              for (var i = 0; i < data.length; i++){
                  console.log(data[i])
                  if (data[i] == ' '){
                    liste_lat.push(pos)
                    pos = ''
                  }
                  else{
                     pos += data[i]
                 } 
              }
              liste_lat.push(pos)
              console.log(liste_lat)
              
              document.getElementById('the_map').style.display = 'block';
              document.getElementById('button_lamap').style.display = 'none';
              document.getElementById('button_lamap_gym').style.display = 'block';
  
              initMap(parseFloat(liste_lat[0]), parseFloat(liste_lat[1]));
          };
          };
      });
  });



  jQuery("#declencheur_gym3").on("click", function(e){

     var b = document.getElementById('gym1').value;
     document.getElementById('oups').innerHTML = '';
     document.getElementById('button_lamap').style.display = 'none';
     
     e.preventDefault();
      jQuery.ajax({
          data:{
               'buttony_gym':String(LISTE_GYM[16]),
               'country_gym':b, 
              
       
          },
          type:"POST",
          url:"/photo/coupe"
      })
      .done(function(data){
          if (data.error){
              jQuery("#monCadreAlert").text(data.error);
              jQuery("#is_save");
              
              
          }
          else{
              jQuery("#is_save").html(data.data);
              jQuery("#monCadreAlert");
              
                if (data == "Oups nous n'avons rien trouvé"){


                document.getElementById('button_lamap_gym').style.display = 'block';
          
                document.getElementById('the_map').style.display = 'block';
                document.getElementById('oups').innerHTML = "Nous n'avons rien trouv\u00e9 désol\u00e9";
                
                document.getElementById('map').style.display = 'none';  
                document.getElementById('lapmap').style.display = 'none';

                
                
                }
              else{

              pos = ''
              for (var i = 0; i < data.length; i++){
                  console.log(data[i])
                  if (data[i] == ' '){
                    liste_lat.push(pos)
                    pos = ''
                  }
                  else{
                     pos += data[i]
                 } 
              }
              liste_lat.push(pos)
              console.log(liste_lat)
              
              document.getElementById('the_map').style.display = 'block';
              document.getElementById('button_lamap').style.display = 'none';
              document.getElementById('button_lamap_gym').style.display = 'block';
             document.getElementById('button_lamap').style.display = 'none';
              initMap(parseFloat(liste_lat[0]), parseFloat(liste_lat[1]));
            };    
          };
          
      });
  });





  jQuery("#declencheur_gym4").on("click", function(e){
      
     document.getElementById('button_lamap').style.display = 'none';
     var b = document.getElementById('gym1').value;
     document.getElementById('oups').innerHTML = '';
     
     e.preventDefault();
      jQuery.ajax({
          data:{
               'buttony_gym':String(LISTE_GYM[24]),
               'country_m':b, 
              
       
          },
          type:"POST",
          url:"/photo/coupe"
      })
      .done(function(data){
          if (data.error){
              jQuery("#monCadreAlert").text(data.error);
              jQuery("#is_save");
              
              
          }
          else{
              jQuery("#is_save").html(data.data);
              jQuery("#monCadreAlert");
              
              if (data == "Oups nous n'avons rien trouvé"){

                document.getElementById('button_lamap_gym').style.display = 'block';
                
                document.getElementById('the_map').style.display = 'block';
                document.getElementById('oups').innerHTML = "Nous n'avons rien trouv\u00e9 désol\u00e9";
                
                document.getElementById('map').style.display = 'none';  
                document.getElementById('lapmap').style.display = 'none';

                
     
                
                }
              else{

              pos = ''
              for (var i = 0; i < data.length; i++){
                  console.log(data[i])
                  if (data[i] == ' '){
                    liste_lat.push(pos)
                    pos = ''
                  }
                  else{
                     pos += data[i]
                 } 
              }
              liste_lat.push(pos)
              console.log(liste_lat)
              
              document.getElementById('the_map').style.display = 'block';
              document.getElementById('button_lamap').style.display = 'none';
              
              document.getElementById('button_lamap_gym').style.display = 'block';
              document.getElementById('button_lamap').style.display = 'none';
              
              initMap(parseFloat(liste_lat[0]), parseFloat(liste_lat[1]));
              
            };  
          };
          
      });
  });







   function declencheur_gym1f(){

    document.getElementById('declencheur_gym1').click()
    document.getElementById('mapmap_gym').style.display = 'none';

    };


   function declencheur_gym2f(){

    document.getElementById('declencheur_gym2').click()
    document.getElementById('mapmap_gym').style.display = 'none';

    };


    function declencheur_gym3f(){

    document.getElementById('declencheur_gym3').click()
    document.getElementById('mapmap_gym').style.display = 'none';

    };



    function declencheur_gym4f(){
    document.getElementById('declencheur_gym4').click()
    document.getElementById('mapmap_gym').style.display = 'none';


    };





         
  function mapo1(){
   
    document.getElementById('declencheur1').click()
    document.getElementById('mapmap').style.display = 'none';
    

    };

  function mapo2(){
    document.getElementById('declencheur2').click()
    document.getElementById('mapmap').style.display = 'none';


    };

  function mapo3(){
    document.getElementById('declencheur3').click()
    document.getElementById('mapmap').style.display = 'none';


    };

  function mapo4(){
    document.getElementById('declencheur4').click()
    document.getElementById('mapmap').style.display = 'none';


    };







    var map;

    function initMap(lattitude, longitude) {

      document.getElementById('map').style.display = 'block';

      lattitude = parseFloat(lattitude)
      longitude = parseFloat(longitude)
      
      map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: lattitude, lng: longitude},
        zoom: 17
      });
      
     var marq1 = {lat: parseFloat(lattitude), lng: parseFloat(longitude)};
      
      var marker1 = new google.maps.Marker({
        position: marq1,
        map: map,
      });

    }



    function stop(div, im, im_src){
   
      document.getElementById(div).style.display = 'block';
      document.getElementById(im).src = im_src

    };

    function start(div, im, im_src){
      document.getElementById(div).style.display = 'none';
      document.getElementById(im).src = im_src
    };

  


    function declencheur1_f(){
        document.getElementById('declencheur1').click()
    }

    function declencheur2_f(){
        document.getElementById('declencheur2').click()
    }

    function declencheur3_f(){
        document.getElementById('declencheur3').click()
    }

    function declencheur4_f(){
        document.getElementById('declencheur4').click()
    }


    function image(){
        document.getElementById("image1").src  = src="/static/img/portfolio/thumbnails/1.jpg";  
    };

  $( function() {
      $("#draggable, #draggable2, #draggable3, #draggable4, #draggable5").draggable();
    } );
  $( function() {
      $("#draggable6, #draggable7, #draggable8, #draggable9, #draggable10, #draggable11").draggable();
    } );
  $( function() {
      $("#draggable12, #draggable14, #draggable15, #draggable16, #draggable18, #draggable19, #draggable_favoris").draggable();
    } );



  $( function() {
      $("#favdraggable, #favdraggable2, #favdraggable3, #favdraggable4, #favdraggable5").draggable();
    } );
  $( function() {
      $("#favdraggable6, #favdraggable7, #favdraggable8, #favdraggable9, #favdraggable10, #favdraggable11").draggable();
    } );
  $( function() {
      $("#favdraggable12, #favdraggable14, #favdraggable15, #favdraggable16, #favdraggable18, #favdraggable19, #draggable_favoris").draggable();
    } );


    LISTE_RESIZE = []
    LISTE_RESIZE_TAILLE_HAUTEUR = []
    LISTE_RESIZE_TAILLE_LARGEUR = []
    
    function nom_image(id, hauteur, largeur){
      LISTE_RESIZE.push(id)
      console.log(id)
      var a = document.getElementById(id).height;
      var b = document.getElementById(id).width;

      LISTE1.push([id, b, a])

    LISTE_FAV_FAV = []
    LISTE_FAV_FAV.push(id)

   
    var a = document.getElementById(id);

    var b = a.offsetLeft;
    var c = a.offsetTop;
 
    
    if(b >= 460 && b <= 580 & c >=60 && c <= 220 ){
    }
  }


function ya(){
      var a = document.getElementById("coupe1").offsetLeft;
      var b = document.getElementById("coupe1").offsetTop;
      console.log(a,b)
};











