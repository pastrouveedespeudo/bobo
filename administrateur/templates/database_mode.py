
{% include "navebarre.html" %}
{% block content %}
{% endblock %}


 <!-- Masthead -->
  <header class="masthead">
    <div class="container h-100">
      <div class="row h-100 align-items-center justify-content-center text-center">
        <div class="col-lg-10 align-self-end">
        <br><br><br><br><br>

           <style>#autre{margin-left:-965px;;margin-top:-100px;}</style>

           <h1 class="text-uppercase text-white font-weight-bold">Coté administrateur !</h1>


  
          <style>#h{font:Serif; color:white;}</style>
          <br>

        
           <hr class="divider my-4">
          </div>

          
          <div class="col-lg-8 align-self-baseline">
             <p class="text-white-75 font-weight-light mb-5"></p>














          
            <div id='interface'>

                <input type='button' value='voir la database' onclick='database()'>

            </div>



            <script>

                function database(){
                    
                    document.getElementById('interface').innerHTML = ''
                    document.getElementById('interface').innerHTML = "<input type='button' value='voir la database femme' onclick='femme()'>" +
                                                                    "&nbsp;&nbsp;" + 
                                                                    "<input type='button' value='voir la database homme' onclick='homme()'>"



                    }

            </script>


            
            <br><br><br><br><br><br><br><br><br><br><br><br>
            
            <input type='button' value='revenir en arriere' onclick='arriere()'>

            
            <script>
            
                function arriere(){
                    document.location.href="/administrateur/mode"; 
                }

                function femme(){
                    document.getElementById('interface').style.display = 'none';
                    document.getElementById('femme').style.display = 'block';
                }

                function homme(){
                    document.getElementById('interface').innerHTML = ''
                }
                
            </script>

            
        
      </div>
    </div>
  </div>
</header>





  <!-- Call to Action Section -->
  <section class="page-section bg-dark text-white">
    <div class="container text-center">
 
            <div id='femme' style='display:none'>

                <p>Database femme</p>


                





                
                
            </div>

                <div class="container">
                      <div class="row">

                        <div class="col-sm">
                        <img src='/static/bobo/2b.jpg' style='width:100px; height:100px;'><br>
                        <input type='image' src='/static/bobo/2a.jpg' style='width:100px; height:250px;'
                        id='2.jpg' onclick='info(id)'><br>
                        </div>

                        <div class="col-sm">
                        <img src='/static/bobo/3b.jpg' style='width:100px; height:100px;'><br>
                        <input type='image' src='/static/bobo/3a.jpg' style='width:100px; height:250px;'
                        id='3.jpg' onclick='info(id)'><br>
                        </div>

                        <div class="col-sm">
                        <img src='/static/bobo/4b.jpg' style='width:100px; height:100px;'><br>
                        <input type='image' src='/static/bobo/4a.jpg' style='width:100px; height:250px;'
                        id='4.jpg' onclick='info(id)'><br>
                        </div>

                        <div class="col-sm">
                        <img src='/static/bobo/5b.jpg' style='width:100px; height:100px;'><br>
                        <input type='image' src='/static/bobo/5a.jpg' style='width:100px; height:250px;'
                        id='5.jpg' onclick='info(id)'><br>
                        </div>

                        <div class="col-sm">
                        <img src='/static/bobo/6b.jpg' style='width:100px; height:100px;'><br>
                        <input type='image' src='/static/bobo/6a.jpg' style='width:100px; height:250px;'
                        id='6.jpg' onclick='info(id)'><br>
                        </div>

                        <div class="col-sm">
                        <img src='/static/bobo/7b.jpg' style='width:100px; height:100px;'><br>
                        <input type='image' src='/static/bobo/7a.jpg' style='width:100px; height:250px;'
                        id='7.jpg' onclick='info(id)'><br>
                        </div>

                        <div class="col-sm">
                        <img src='/static/bobo/8b.jpg' style='width:100px; height:100px;'><br>
                        <input type='image' src='/static/bobo/8a.jpg' style='width:100px; height:250px;'
                        id='8.jpg' onclick='info(id)'><br>
                        </div>  

                    </div>
                </div>




         
      <br><br>
      <div id='info_image'></div>
      
      <div id='vetement' style='float:left; display:none;'><strong>Vetement</strong></div>
      <div id='coupe' style='float:right; display:none;'><strong>Coupe</strong></div>

      <br><br>
      <div id='info_image_coupe' style='float:left;'></div>
      <br><div id='info_image_vetement' style='float:right;'></div>
      
      <br><br>  
      <div id='im_coupe' style='display:none; float:right;'><img id='image_into_coupe' src=''
                                                            style='width:60px; height:100px'></div>
                                                      
      <div id='im_vetement' style='display:none; float:left;'><img id='image_into_vetement' src=''
                                                            style='width:60px; height:100px'></div>

      
      <div id='couleur_cheuveux' style='float:right;'></div>

      <br><br><br><br><br><br>
      <div id='couleur_haut' style='float:left;'></div><br><br>
      <div id='couleur_bas' style='float:left;'></div>
      


      <br><br>
      VOULEZ VOUS VOIR A QUOI CORRESPOND CETTE COULEUR (liste_haut bas par exeple)
            console.log(LISTE_IMAGE[0]);
            console.log(LISTE_SEXE[0]);
            console.log(LISTE_HAUT[0]);
            console.log(LISTE_BAS[0]);

            
      <script>
      
        function info(id){

          LISTE = []
          
          var identifiant = document.getElementById(id).id;
    
          document.getElementById('info_image').innerHTML = identifiant;

          for(var i = 0; i < LISTE_IMAGE.length -1; i ++){
            
            var liste_image1 = String(LISTE_IMAGE[i]).slice(0,1);
            var liste_image2 = String(LISTE_IMAGE[i]).slice(2,);
            var image = liste_image1 + liste_image2;

            if(image == identifiant){
              console.log(image);
              LISTE.push(i);
              
              }
            }

          
          console.log(LISTE)
          console.log(LISTE[LISTE.length-2]);
          console.log(LISTE[LISTE.length-1]);
          
          document.getElementById('coupe').style.display='block';
          document.getElementById('vetement').style.display='block';
          
          document.getElementById('info_image_vetement').innerHTML = LISTE_IMAGE[LISTE[LISTE.length-1]];
          document.getElementById('info_image_coupe').innerHTML = LISTE_IMAGE[LISTE[LISTE.length-2]];
          
          
          document.getElementById('im_coupe').style.display = 'block';
          document.getElementById('im_vetement').style.display = 'block';

          document.getElementById('image_into_coupe').src = '/static/bobo/' +
                                                          LISTE_IMAGE[LISTE[LISTE.length-1]]


          document.getElementById('image_into_vetement').src = '/static/bobo/' +
                                                          LISTE_IMAGE[LISTE[LISTE.length-2]]

          document.getElementById('couleur_haut').innerHTML = '<input type="button" value="voir les couleurs du haut">';
          document.getElementById('couleur_bas').innerHTML = '<input type="button" value="voir les couleurs du bas">';
          

          }


      </script>



      
    <br><br><br><br><br><br><br><br>
    </div>
  </section>





  <script>
  
          var LISTE = []
          var LISTE_IMAGE = []
          var LISTE_SEXE = []
          var LISTE_HAUT = []
          var LISTE_BAS = []

       
  </script>




  {% for i in data %}
  {{i|slice:'1:2'}}

  <script>

    function decodeHtml(html) {
        var txt = document.createElement("textarea");
        txt.innerHTML = html;
        return txt.value;
    }


    LISTE_IMAGE.push([decodeHtml("{{i|slice:'1:2'}}").slice(2,-3)])
    LISTE_SEXE.push([decodeHtml("{{i|slice:'2:3'}}").slice(2,-3)])
    LISTE_HAUT.push([decodeHtml("{{i|slice:'4:5'}}").slice(2,-3)])
    LISTE_BAS.push([decodeHtml("{{i|slice:'5:6'}}").slice(2,-3)])
    
  </script>




  {% endfor %}

























